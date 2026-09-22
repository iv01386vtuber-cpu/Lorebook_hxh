#!/usr/bin/env python3
"""
สร้าง HxH UNIFIED v60 LEAN จาก v59 WI MINIMAL

สิ่งที่ทำ (ดูเหตุผลเต็มใน docs/ANALYSIS_v59.md):
 1. ซ่อมระบบอ้างอิง UID ที่พังทั้งหมด (v59 มี 62/119 ลิงก์ที่ชี้ผิดเป้า)
 2. ตัดกองวิกิภาษาอังกฤษที่ไม่ได้ใช้ออกเป็นไฟล์แยก (archive) — ไม่ลบทิ้ง
 3. ยุบ always-on 11 entry (~7.9k tok/เทิร์น) เหลือ 5 entry (~2.9k tok/เทิร์น)
 4. ผ่าคีย์: ชื่อตัวละครเปล่า ๆ อยู่บน entry เดียวต่อคน (เลิกยิงพร้อมกัน 13 entry)
 5. ล็อกเฟสอนาคต (F/G) ด้วย keysecondary กันสปอยล์รั่วเข้าฉากปัจจุบัน
 6. จัด order เป็นชั้น ๆ ให้ลำดับตัดทิ้งตอนงบล้นเป็นของที่ตั้งใจ ไม่ใช่ของสุ่ม
 7. บีบช่องว่าง/เส้นคั่นตกแต่งที่กินโทเคนฟรี

ใช้: python3 tools/build_v60_lean.py <v59.json> <outdir>
"""
import json, re, sys, os
from collections import defaultdict

SRC = sys.argv[1]
OUT = sys.argv[2] if len(sys.argv) > 2 else "lorebook"

book = json.load(open(SRC, encoding="utf-8"))
E = list(book["entries"].values())
by_uid = {v["uid"]: v for v in E}


def toks(s):
    th = len(re.findall(r"[฀-๿]", s))
    return int(th / 2.2 + (len(s) - th) / 3.6)


def is_wiki(v):
    return bool(re.search(r"9[0-7] LORE-", v.get("comment", "")))


# ─────────────────────────────────────────────────────────────
# 1. แผนที่ "เลขในคอมเมนต์ (legacy)" -> uid จริง
# ─────────────────────────────────────────────────────────────
const_before = sum(toks(v["content"]) for v in E
                   if v.get("constant") and not v.get("disable"))
n_const_before = sum(1 for v in E if v.get("constant") and not v.get("disable"))
before = sum(toks(v["content"]) for v in E)

# v59 ใช้เลขอ้างอิงถึง 3 ระบบปนกัน: uid จริง / เลขในคอมเมนต์ / เลขในหัวข้อ "### NN —"
# ที่เหลือจากฉบับเก่ากว่านั้นอีก ต้องแมปด้วยมือ
MANUAL_LEGACY = {"401": 64, "402": 66, "404": 67, "105b": 99107, "700": 40652}
legacy = {}
for v in E:                                   # ชั้น 3: หัวข้อในเนื้อหา
    for m in re.finditer(r"^#{2,4}\s*(?:★\s*)?(\d+[a-z]?)\s*—", v["content"], re.M):
        legacy.setdefault(m.group(1), v["uid"])
for v in E:                                   # ชั้น 2: เลขในคอมเมนต์ (ทับชั้น 3)
    m = re.search(r"·\s*[^\w\s]*\s*(\d+[a-z]?)\s*—", v["comment"])
    if m:
        legacy[m.group(1)] = v["uid"]
legacy.update(MANUAL_LEGACY)                  # ชั้น 1: แมปมือ

fix_log, lost_log = [], defaultdict(set)


SURVIVING = set()   # uid ที่อ้างอิงถึงได้จริง (เติมหลังคัด entry แล้ว)

EN = re.compile(r"[A-Za-z]{4,}")
TH = re.compile(r"[\u0E00-\u0E7F]+")


def bag(text):
    """ถุงคำสองภาษา: อังกฤษนับเป็นคำ / ไทยไม่มีช่องว่างจึงนับเป็น 4-gram ตัวอักษร"""
    b = set(w.lower() for w in EN.findall(text))
    for run in TH.findall(text):
        b.update(run[i:i + 4] for i in range(max(1, len(run) - 3)))
    return b


# เคสที่สกอร์อัตโนมัติแยกไม่ออก แต่ตรวจด้วยมือแล้วชัด: (เลข ref, คำในบริบท, uid เป้า)
CONTEXT_RULES = [
    ("55", re.compile(r"Uvogin|\u0e2d\u0e39\u0e42\u0e1a\u0e01\u0e34\u0e19"), 54),
    ("31", re.compile(r"\u0e2b\u0e21\u0e31\u0e49\u0e19|engagement|Fianc", re.I), 45),
    ("50", re.compile(r"forensic|Recognition", re.I), 50),
    ("51", re.compile(r"Recognition", re.I), 50),
]

_prof = {}


def profile(u):
    """คลังคำของ entry ปลายทาง ใช้ให้คะแนนว่า ref ตัวไหนน่าจะหมายถึงอันนี้"""
    if u not in _prof:
        v = by_uid[u]
        _prof[u] = bag(v["comment"] + " " + " ".join(v.get("key", []))
                       + " " + v["content"][:800])
    return _prof[u]


def fix_refs(v):
    """v59 ใช้เลขสองระบบปนกัน (เลขเก่าในคอมเมนต์ vs uid จริง) ทำให้ลิงก์ชี้ผิดเป้า
    เพียบ. ตรงนี้เลือกเป้าที่ 'เข้ากับบริบทรอบ ๆ ลิงก์' มากที่สุด แล้วเขียนเป็น uid จริง
    ตัวที่หาเป้าไม่ได้เลย = entry ที่ถูกลบไปแล้ว -> ตัดลิงก์ทิ้ง"""
    src = v["content"]

    def sub(m):
        r = m.group(1)
        cands = []
        if legacy.get(r) in SURVIVING:
            cands.append(legacy[r])
        if r.isdigit() and int(r) in SURVIVING and int(r) not in cands:
            cands.append(int(r))
        if not cands:
            lost_log[r].add(v["uid"])
            return "\x00"
        ctxs = src[max(0, m.start() - 130): m.start() + 60]
        for rr, pat, tgt in CONTEXT_RULES:
            if rr == r and tgt in SURVIVING and pat.search(ctxs):
                cands = [tgt]
                break
        if len(cands) > 1:
            ctx = bag(ctxs)
            cands.sort(key=lambda u: len(ctx & profile(u)), reverse=True)
        if str(cands[0]) != r:
            fix_log.append((v["uid"], r, cands[0]))
        return f"UID {cands[0]}"

    c = re.sub(r"UID\s*#?\s*(\d+[a-z]?)", sub, src)
    # ลบร่องรอยของลิงก์ที่ชี้ไปหา entry ที่ถูกลบไปแล้ว ให้โมเดลไม่ต้องตามหาผี
    c = re.sub(r"\s*\([^()\n]*\x00[^()\n]*\)", "", c)
    c = re.sub(r"\s*[\u00b7\u2014\u2192]\s*(?:\u0e14\u0e39|see|cf\.?|\u0e15\u0e32\u0e21)?\s*\x00", "", c, flags=re.I)
    c = re.sub(r"\s*(?:\u0e14\u0e39|see|cf\.?|\u0e15\u0e32\u0e21)?\s*\x00", "", c, flags=re.I)
    c = re.sub(r"[ \t]{2,}", " ", c)
    c = re.sub(r"\(\s*\)|\[\s*\]", "", c)
    c = re.sub(r"\s+([,.;:])", r"\1", c)
    v["content"] = c
    return v


# ─────────────────────────────────────────────────────────────
# 2. คัดกองวิกิ: เก็บเฉพาะที่ถูกอ้างถึงจริงในเนื้อเรื่อง + คู่มือ RP ภาษาไทย
# ─────────────────────────────────────────────────────────────
custom = [v for v in E if not is_wiki(v)]
wiki = [v for v in E if is_wiki(v)]
blob = "\n".join(v["content"] + " " + v["comment"] for v in custom)

MUST = {
    "Chrollo", "Hisoka", "Illumi", "Silva", "Zeno", "Kikyo", "Milluki", "Kalluto",
    "Alluka", "Nanika", "Machi", "Feitan", "Nobunaga", "Phinks", "Uvogin",
    "Pakunoda", "Shizuku", "Bonolenov", "Franklin", "Kortopi", "Shalnark",
    "Neon", "Senritsu", "Melody", "Leorio", "Kurapika", "Killua", "Tserriednich",
    "Canary", "Cheadle", "Izunavi", "Pairo", "Sheila", "Zebro", "Mike", "Netero",
    "Ging", "Kite", "Biscuit", "Wing", "Zushi", "Basho", "Pietro", "Squala",
    "Dalzollene", "Eliza", "Baise", "Amane", "Gotoh", "Tsubone", "Hanzo",
    "Pariston", "Komugi", "Meruem", "Neferpitou", "Shaiapouf", "Menthuthuyoupi",
    "Knov", "Morel", "Woble", "Oito", "Yorknew", "Kakin", "Meteor City",
    "Lukso", "Nancha", "Southernpiece", "Greed Island", "Heavens Arena",
    "Dark Continent", "Hunter Association", "Zodiacs", "Mafia Community",
    "Ten Dons", "Chimera Ant", "Whale Island", "Lingon",
}
# ชื่อสั้น/คำกำกวมที่ยิงมั่วในข้อความอังกฤษ ("On", "Ai", "In", "Q", "Don", "Spot"…)
NOISE_KEY = re.compile(r"^(?:[A-Za-z]{1,3}|Spot|Leech|Kurt|Shadow|Rice|Bill|Sandra|Sheila)$")


def wiki_keep(v):
    tag = re.search(r"\[([A-Z\-]+)\]", v["comment"])
    tag = tag.group(1) if tag else ""
    if tag in ("RP-GUIDE", "MEDICAL", "SKILL", "LAW", "PROFESSION"):
        return True
    if re.search(r"[฀-๿]", v["comment"]):      # คู่มือที่เขียนเองเป็นไทย
        return True
    if "[DISABLED" in v["comment"]:
        return False
    for k in v.get("key", []):
        k = k.strip()
        if len(k) < 4 or NOISE_KEY.match(k):
            continue
        if any(m in k for m in MUST):
            return True
        if re.search(r"(?<![A-Za-z])" + re.escape(k) + r"(?![A-Za-z])", blob):
            return True
    return False


# entry วิกิที่ถูกอ้างถึงตรง ๆ จากเนื้อเรื่อง -> ต้องเก็บไว้ ไม่งั้นลิงก์ขาด
FORCE_KEEP_WIKI = {428, 459, 476, 500, 504, 511, 512, 518, 537, 540, 545, 546, 548, 551}
wiki_keep_set = [v for v in wiki if wiki_keep(v) or v["uid"] in FORCE_KEEP_WIKI]
wiki_drop_set = [v for v in wiki if not wiki_keep(v)]

# ─────────────────────────────────────────────────────────────
# 3. ทิ้งของซ้ำ/ของปิดไว้
# ─────────────────────────────────────────────────────────────
DROP_UIDS = {
    99124,          # สำเนาคำต่อคำของ 643 (คีย์ชุดเดียวกันเป๊ะ = แย่งงบกันเอง)
    482, 491, 585,  # ติดป้าย DISABLED ไว้อยู่แล้ว
}

kept = [v for v in custom if v["uid"] not in DROP_UIDS] + \
       [v for v in wiki_keep_set if v["uid"] not in DROP_UIDS]

# ─────────────────────────────────────────────────────────────
# 4. ผ่าคีย์
# ─────────────────────────────────────────────────────────────
BARE = {
    "kura": ["Kurapika", "คุราปิก้า", "Chain User", "ผู้ใช้โซ่", "Kurapica",
             "Curarpikt", "Emperor Time", "Chained Avenger"],
    "kill": ["Killua", "Killua Zoldyck", "คิรัวร์", "คิลัว", "คิลลัว",
             "Tsundere Assassin", "Godspeed"],
    "vina": ["Vina", "Vina Surilvan", "Vina Sullivan", "วีน่า", "Timeless Doll",
             "ตุ๊กตาไร้กาลเวลา", "Half-Kurta"],
}
OWNER = {"kura": 99101, "kill": 99110, "vina": 99108}

ADD_KEYS = {
    99103: ["คุราปิก้าหึง", "Kurapika jealousy", "หวงวีน่า", "ถอยห่าง", "self-isolation"],
    99104: ["ประวัติคุราปิก้า", "Kurapika biography", "อดีตคุราปิก้า", "โซ่ห้าเส้น",
            "Judgment Chain", "Chain Jail", "Nostrade bodyguard"],
    99105: ["มุมมองคุราปิก้า", "Kurapika POV", "ในใจคุราปิก้า", "Kurapika thinks"],
    628:   ["hidden devotion", "สิ่งที่เขาทำลับหลัง", "คุราปิก้าดูแลวีน่า",
            "Kurapika devotion", "แอบดูแล", "ของที่ส่งมาไม่มีโน้ต"],
    614:   ["Kurapika psychology"],
    99111: ["ประวัติคิลัว", "Killua biography", "อดีตคิลัว", "เข็มอิลลูมิ", "หนีออกจากบ้าน"],
    99121: ["คิลัวสู้", "Killua fight", "ไฟต์คิลัว", "Killua combat"],
    99122: ["คิลัวเขิน", "Killua flustered", "คิลัวอ่อนลง", "หูแดง"],
    629:   ["Killua hidden devotion", "สิ่งที่คิลัวทำลับหลัง", "คิลัวแอบดูแล",
            "ขนมยี่ห้อเดิม"],
    99109: ["วีน่าเด็ก", "Vina child", "Vina pre-massacre"],
}

# entry ที่มีแต่ชื่อเปล่าเป็นคีย์ ถ้าถอดชื่อออกจะตายสนิท -> ต้องมี ADD_KEYS รองรับ
for v in kept:
    u = v["uid"]
    keys = [k.strip() for k in v.get("key", [])]
    for grp, names in BARE.items():
        if u != OWNER[grp]:
            keys = [k for k in keys if k not in names]
    keys += ADD_KEYS.get(u, [])
    # กัน key สั้น/กำกวมที่ยิงมั่ว
    keys = [k for k in keys if not NOISE_KEY.match(k) or k in ("V6", "V5", "Nen")]
    v["key"] = sorted(set(keys), key=keys.index) if keys else v.get("key", [])

# คีย์ที่กว้างเกินจนดูดของผิดยุคเข้าฉาก
by_uid[716]["key"] = ["Kurapika Vina", "คุราปิก้า วีน่า", "วีน่า คุราปิก้า",
                      "โรแมนติก", "confession", "สารภาพรัก", "แต่งงาน", "หมั้น"]
by_uid[99130]["key"] = ["[PRESENT]", "[NOW]"]
by_uid[99305]["key"] = ["ตาสีเพลิงวีน่า", "Vina scarlet eyes", "ตาวีน่าแดง",
                        "ตาแดงเต็มดวง"]
by_uid[717]["key"] = [k for k in by_uid[717]["key"] if k not in ("หึง", "หวง", "อ้อน",
                                                                "งอน", "เขิน", "ภาระ")] + \
                     ["วีน่าหึง", "วีน่างอน", "วีน่าอ้อน", "สกินชิพ", "แตะตัว"]

# ─────────────────────────────────────────────────────────────
# 5. ล็อกเฟส: อนาคตต้องประกาศชื่อเฟสก่อนถึงจะยิง
# ─────────────────────────────────────────────────────────────
GATE = {
    "E":  ([99001], ["Phase E", "เฟส E", "สงครามเงียบ", "Silent War"]),
    "F":  ([60, 65, 66, 627, 99125], ["Phase F", "เฟส F", "Black Whale", "แบล็กเวล",
                                      "เรือดำ", "ขึ้นเรือ"]),
    "G":  ([99300, 99301, 99302, 99303, 99304, 99305, 99306, 99307],
           ["Phase G", "เฟส G", "คืนร่าง", "หลังคืนร่าง", "the return"]),
    "A":  ([20009, 20011], ["Phase A", "เฟส A", "หมู่บ้านคูรุตะ", "ก่อนสังหารหมู่",
                            "pre-massacre"]),
}
for _, (uids, sec) in GATE.items():
    for u in uids:
        if u in by_uid:
            by_uid[u]["selective"] = True
            by_uid[u]["selectiveLogic"] = 0          # AND ANY: primary + secondary
            by_uid[u]["keysecondary"] = sec

# ─────────────────────────────────────────────────────────────
# 6. ชั้นความสำคัญ (order) — สูง = รอดตอนงบล้น
# ─────────────────────────────────────────────────────────────
def tier(v):
    c, u = v["comment"], v["uid"]
    if v.get("constant"):                       return 1000
    if u in (99130, 99299, 99200):              return 980
    if u in OWNER.values():                     return 700   # โปรไฟล์หลัก 3 คน
    if re.search(r"30 CHAR|👤", c):              return 650
    if re.search(r"50 REL|💞", c):               return 600
    if re.search(r"MASTER BLOCK|MASTER OVERRIDE|CANON LOCK", c): return 620
    if re.search(r"70 TIME", c):                return 500
    if re.search(r"10 WORLD", c):               return 450
    if re.search(r"ZOLDYCK BOOK|PHASE-A BOOK", c): return 400
    if re.search(r"80 VISUAL|90 STYLE|🎨", c):   return 250
    if is_wiki(v):                              return 100
    return 300


# ─────────────────────────────────────────────────────────────
# 7. ยุบ always-on
# ─────────────────────────────────────────────────────────────
OLD_CONST = [0, 1, 2, 3, 613, 716, 99130, 99200, 99299]
for u in OLD_CONST:
    by_uid[u]["constant"] = False
by_uid[0]["key"] = ["[CORE FULL]", "world anchor", "โครงโลก"]
by_uid[1]["key"] = ["[STYLE]", "iceberg", "สไตล์การเขียน"]
by_uid[99200]["key"] = ["[CANON LOCK]", "สีตาคุราปิก้า", "สายตาไพโร", "Dino Hunter",
                        "การสอบออกนอกเผ่า", "ออกไปด้วยกัน"]
by_uid[99299]["key"] = ["[PHASE]", "เฟสไหน", "phase arbiter"]

NEW_CONST = json.load(open(os.path.join(os.path.dirname(__file__),
                                        "v60_core_constants.json"), encoding="utf-8"))

# Omega layer: ย่อ
by_uid[4]["content"] = re.sub(r"\n{2,}", "\n", by_uid[4]["content"])

# ─────────────────────────────────────────────────────────────
# 8. ประกอบ + บีบช่องว่าง
# ─────────────────────────────────────────────────────────────
def squeeze(s):
    s = re.sub(r"[ \t]+\n", "\n", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    s = re.sub(r"^[─━=_]{6,}$", "", s, flags=re.M)     # เส้นคั่นตกแต่ง
    s = re.sub(r"\n{3,}", "\n\n", s)
    s = re.sub(r"★{3,}", "★★", s)
    return s.strip()


# เป้าอ้างอิงที่ถือว่าถูกต้อง = entry เนื้อเรื่องทั้งหมด + คู่มือ RP ภาษาไทย
# + วิกิที่ถูกอ้างถึงตรง ๆ.  ตัวละครวิกิอังกฤษไม่นับ เพราะ "UID 401" ในเนื้อเรื่อง
# หมายถึง entry เก่าที่ถูกลบไปแล้ว ไม่ได้หมายถึง Zebro
SURVIVING.update(v["uid"] for v in kept if not is_wiki(v))
SURVIVING.update(v["uid"] for v in wiki_keep_set
                 if re.search(r"[\u0E00-\u0E7F]", v["comment"])
                 or v["uid"] in FORCE_KEEP_WIKI)
SURVIVING.update(v["uid"] for v in NEW_CONST)
for v in kept:
    fix_refs(v)
    v["content"] = squeeze(v["content"])
    v["order"] = tier(v)
    v["excludeRecursion"] = True

out_entries = NEW_CONST + kept
for i, v in enumerate(out_entries):
    v["displayIndex"] = i
    v.setdefault("addMemo", True)
    v.setdefault("probability", 100)
    v.setdefault("useProbability", True)
    v.setdefault("disable", False)
    v.setdefault("position", 0)
    v.setdefault("selective", True)
    v.setdefault("selectiveLogic", 0)
    v.setdefault("keysecondary", [])

after = sum(toks(v["content"]) for v in out_entries)
const_after = sum(toks(v["content"]) for v in out_entries if v.get("constant"))

lean = {
    "name": "HxH UNIFIED v60 LEAN",
    "description": (
        "[v60.0 — LEAN REBUILD ของ v59]\n"
        f"· always-on: {const_before} → {const_after} tok/เทิร์น (ยุบ {n_const_before} entry เหลือ "
        f"{sum(1 for v in out_entries if v.get('constant'))})\n"
        f"· entries: {len(E)} → {len(out_entries)} (ย้ายวิกิอังกฤษที่ไม่ได้ใช้ "
        f"{len(wiki_drop_set)} รายการไปไฟล์ archive แยก)\n"
        f"· ขนาดรวม: ~{before} → ~{after} tok\n"
        "· ซ่อมลิงก์ UID ที่ชี้ผิดเป้าทั้งหมด (v59 พัง 62/119 ลิงก์)\n"
        "· ชื่อตัวละครเปล่า ๆ = คีย์ของ entry เดียวต่อคน (เลิกยิงพร้อมกัน 13 entry)\n"
        "· Phase E/F/G + Phase A book ต้องประกาศชื่อเฟสก่อนถึงจะยิง (keysecondary)\n"
        "· order จัดเป็นชั้น: constant 1000 > anchor 980 > core 700 > rel 600 > "
        "time 500 > world 450 > visual 250 > wiki 100\n"
        "เนื้อเรื่องทั้งหมดยังเป็นของเดิม — ไม่มีการเขียนพล็อตใหม่"
    ),
    "scan_depth": 4,
    "token_budget": 10000,
    "recursive_scanning": False,
    "extensions": {},
    "entries": {str(v["uid"]): v for v in out_entries},
}

archive = {
    "name": "HxH v60 — Wiki Archive (optional)",
    "description": "กองวิกิ HxH ภาษาอังกฤษที่ถูกแยกออกจาก v60 LEAN "
                   "(ไม่ถูกอ้างถึงในเนื้อเรื่องเลย). นำเข้าเป็นเล่มเสริมได้ถ้าต้องการ.",
    "scan_depth": 2, "token_budget": 2000, "recursive_scanning": False,
    "extensions": {},
    "entries": {str(v["uid"]): dict(v, order=100, displayIndex=i)
                for i, v in enumerate(wiki_drop_set)},
}

os.makedirs(OUT, exist_ok=True)
json.dump(lean, open(f"{OUT}/HxH_UNIFIED_v60_LEAN.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
json.dump(archive, open(f"{OUT}/HxH_v60_Wiki_Archive.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)

print(f"entries      {len(E)} -> {len(out_entries)}   (archive {len(wiki_drop_set)})")
print(f"always-on    {const_before} -> {const_after} tok/turn")
print(f"book total   ~{before} -> ~{after} tok")
print(f"UID refs ซ่อม {len(fix_log)} จุด | ตัดทิ้ง(ชี้ไปหาของที่ไม่มี) {len(lost_log)} เลข")
print("  เลขที่หาเป้าไม่เจอ:", ", ".join(sorted(lost_log, key=lambda x: (len(x), x))))
