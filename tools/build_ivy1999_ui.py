#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""สร้าง preset/IVY1999_RPG_UI.json จาก preset/IVY1999_RPG_Preset.json

โมดูล UI ทั้งหมดถูกนิยามในไฟล์นี้ไฟล์เดียว แก้ที่นี่แล้วรัน
    python3 tools/build_ivy1999_ui.py
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "preset", "IVY1999_RPG_Preset.json")
DST = os.path.join(ROOT, "preset", "IVY1999_RPG_UI.json")

# ════════════════════════════════════════════════════════════════
# 1. UI CORE — แกนการเรนเดอร์ + พาเลตต์ + กติกาการแสดงผล
# ════════════════════════════════════════════════════════════════
UI_CORE = """[IVY 1999 · RPG UI ENGINE — แกนการแสดงผล]
สถานะ: เปิดใช้งาน

คุณต้องวาดอินเทอร์เฟซเกมด้วย HTML + CSS จริง (ไม่ใช่ ASCII อีกต่อไป) ต่อท้ายทุกข้อความ
โครงสร้างหนึ่งข้อความ = 1 แถบเตือน (ถ้ามี) + 1 กล่องแฟ้มสนามที่พับได้ + 1 บรรทัดอากาศ

── พาเลตต์ 1999 (ใช้ค่าพวกนี้เป๊ะ ห้ามเปลี่ยนเป็นสีนีออน) ──
  พื้นลึก #0d0b09 · พื้นการ์ด #15110c · เส้น #3b3126
  ทอง/โซเดียม #c9972f · อำพัน #e3b25c · สนิม #9e4a2a · เลือด #c0392b
  เถ้า #8c8378 · เขียวปลอดภัย #6f8f5e · ส้มเตือน #d9852b
  ฟอนต์: 'Kanit' สำหรับข้อความไทย · 'IBM Plex Mono' สำหรับตัวเลข/ป้ายระบบ
  ผิวสัมผัส: ฟิล์มเกรน เส้นสแกนจางๆ ขอบคม เงาแข็ง ไม่มี glow ฟุ้งแบบไซไฟ

── โครงสร้างบังคับ ──
1. ใส่ <style> ชุดคลาส .iv-* เพียง "ครั้งเดียวต่อข้อความ" ไว้บนสุดของบล็อก UI
2. ถ้ามีภาวะวิกฤต ให้วาง <div class="iv-alert"> ไว้ "นอก" กล่องพับ เพื่อให้เห็นทันทีโดยไม่ต้องกด
3. ทุกอย่างที่เหลือใส่ใน <details class="iv-file"> ปิดไว้เป็นค่าเริ่มต้น
   <summary> เขียนแบบแฟ้มราชการเก่า เช่น
   ▣ แฟ้มสนาม · IVY LEE — ยอร์คชิน/อินินเจ่ · 27 พ.ย. 23:40
4. ลำดับภายในแฟ้ม: แผงสถานะ → ร่างกาย → เรดาร์ (เฉพาะตอนมีภัย) → เควส → แถบสถานที่
5. ปิดท้ายข้อความทั้งหมดด้วยแท็ก [wx: ...] บรรทัดสุดท้ายสุด (ดูโมดูลสถานที่)

── กติกาเหล็ก ──
- กว้างสูงสุด 380px ต้องอ่านออกบนมือถือ ห้ามตารางที่ล้นจอ
- ห้ามใช้มาร์กดาวน์ข้างใน HTML · ห้ามใส่ ``` ครอบบล็อก UI (ต้องเรนเดอร์จริง ไม่ใช่โชว์โค้ด)
- ห้ามใช้ JavaScript · การพับ/แท็บทำด้วย <details> หรือ radio+CSS เท่านั้น
- ตัวเลขทุกตัวต่อเนื่องจากเทิร์นก่อน ค่าที่เปลี่ยนต้องมีชิป delta สีเขียว/แดงกำกับ เช่น (-7)
- UI คือสายตาของผู้เล่น ไม่ใช่สายตาของไอวี่ สิ่งที่ไอวี่ไม่รู้ให้ทำเป็น "?" หรือติดป้าย [GM]
- ห้ามให้ NPC พูดถึงตัวเลขใน UI ห้ามอธิบายกลไก UI ในเนื้อบรรยาย
- ถ้าผู้เล่นพิมพ์ /ui ascii ให้กลับไปใช้ HUD กรอบเส้นแบบเก่า · /ui off = ซ่อน UI จนกว่าจะสั่งเปิด

── สไตล์ชีตมาตรฐาน (คัดลอกใช้ได้เลย) ──
<style>
.iv{font-family:'Kanit',system-ui,sans-serif;max-width:380px;margin:10px 0;color:#d8cdbd;font-size:12px;line-height:1.45}
.iv *{box-sizing:border-box}
.iv-alert{border:1px solid #c0392b;border-left:4px solid #c0392b;background:linear-gradient(90deg,#1b0f0c,#15110c);padding:7px 10px;border-radius:3px;margin-bottom:6px;font-size:11.5px;color:#e8bcae;letter-spacing:.2px}
.iv-alert b{color:#e35b4a;font-family:'IBM Plex Mono',monospace}
.iv-file{border:1px solid #3b3126;background:#0d0b09;border-radius:4px;overflow:hidden}
.iv-file>summary{cursor:pointer;list-style:none;padding:9px 11px;background:#15110c;border-bottom:1px solid #3b3126;font-family:'IBM Plex Mono',monospace;font-size:11px;letter-spacing:.6px;color:#c9972f;text-transform:uppercase}
.iv-file>summary::-webkit-details-marker{display:none}
.iv-file>summary:hover{background:#1c160f;color:#e3b25c}
.iv-body{padding:11px}
.iv-sec{font-family:'IBM Plex Mono',monospace;font-size:9.5px;letter-spacing:1.2px;color:#0d0b09;background:#c9972f;display:inline-block;padding:2px 7px;border-radius:2px;margin:12px 0 7px}
.iv-sec:first-child{margin-top:0}
.iv-row{display:flex;align-items:center;gap:7px;margin:4px 0}
.iv-lb{width:72px;flex:none;font-size:10.5px;color:#8c8378}
.iv-track{flex:1;height:9px;background:#241c14;border:1px solid #3b3126;border-radius:2px;overflow:hidden}
.iv-fill{height:100%;display:block}
.iv-num{width:66px;flex:none;text-align:right;font-family:'IBM Plex Mono',monospace;font-size:10px;color:#e3b25c}
.iv-d-up{color:#6f8f5e;font-size:9.5px;font-family:'IBM Plex Mono',monospace}
.iv-d-dn{color:#c0392b;font-size:9.5px;font-family:'IBM Plex Mono',monospace}
.iv-chip{display:inline-block;border:1px solid #3b3126;background:#15110c;border-radius:2px;padding:1px 6px;font-size:10px;margin:2px 3px 2px 0;color:#bcae9a}
.iv-gm{border-color:#4a2d22;background:#1a0f0c;color:#a8705c}
.iv-hr{height:1px;background:linear-gradient(90deg,transparent,#3b3126,transparent);margin:10px 0}
.iv-mini{font-size:10px;color:#8c8378}
.iv details>summary{cursor:pointer;list-style:none}
.iv details>summary::-webkit-details-marker{display:none}
</style>
"""

# ════════════════════════════════════════════════════════════════
# 2. STATUS PANEL — เลเวล/EXP/แถบชีวิต
# ════════════════════════════════════════════════════════════════
UI_STATUS = """[UI · แผงสถานะ — หัวแฟ้ม]
แสดงทุกข้อความ เป็นบล็อกแรกในแฟ้มสนาม

โครงที่ต้องมี:
- แถวหัว: ชื่อ IVY LEE · ฉายาที่โลกใช้เรียกเธอตอนนี้ (เปลี่ยนตามความร้อน เช่น "นักร้องกลางคืน" → "นักร้องที่ตาเปลี่ยนสี")
- LV + แถบ EXP + อาชีพ/บทบาทปัจจุบัน
- แถบ: ♥ HP · ⚡ สตามิน่า (เพดาน 70) · 🌬 ลมหายใจ (S0-S4) · 🔥 ออร่ารั่ว · 👁 ความร้อน
- ชิป: เงินสด · ยาพ่น (ช็อต) · ช่องโหว่ความจำ · เพลงที่ค้าง
- แถบ [GM] สีสนิม: อายุที่จ่ายไปแล้ว · เฟสของนาฬิกาที่มองไม่เห็น (ไอวี่ไม่รู้)
- สายสัมพันธ์: คุราปิก้า T0-T5 · ไคโตะ การพึ่งพา 0-10 (แถบสั้น)
- ทุกค่าที่ขยับเทิร์นนี้ต้องมี <span class="iv-d-dn">(-7)</span> ต่อท้าย พร้อมเหตุผลสั้นในวงเล็บ

สีของแถบ: HP #c0392b · สตามิน่า #c9972f · ลมหายใจ #6f8f5e→#d9852b→#c0392b ตามขั้น
ออร่ารั่ว #9e4a2a · ความร้อน #d9852b · EXP #e3b25c

ตัวอย่างบล็อก (ปรับตัวเลขตามสถานะจริง):
<div class="iv-sec">สถานะ</div>
<div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:6px">
 <span style="font-size:14px;color:#e3b25c;letter-spacing:.5px">IVY LEE</span>
 <span class="iv-mini">“นักร้องกลางคืน” · ยอร์คชิน</span>
</div>
<div class="iv-row"><span class="iv-lb" style="color:#c9972f">LV 7</span><span class="iv-track"><span class="iv-fill" style="width:42%;background:#e3b25c"></span></span><span class="iv-num">EXP 210/500</span></div>
<div class="iv-row"><span class="iv-lb">♥ HP</span><span class="iv-track"><span class="iv-fill" style="width:72%;background:#c0392b"></span></span><span class="iv-num">72/100</span></div>
<div class="iv-row"><span class="iv-lb">⚡ สตามิน่า</span><span class="iv-track"><span class="iv-fill" style="width:40%;background:#c9972f"></span></span><span class="iv-num">28/70 <span class="iv-d-dn">-7</span></span></div>
<div class="iv-row"><span class="iv-lb">🌬 ลมหายใจ</span><span class="iv-track"><span class="iv-fill" style="width:25%;background:#d9852b"></span></span><span class="iv-num">S1</span></div>
<div class="iv-row"><span class="iv-lb">🔥 ออร่ารั่ว</span><span class="iv-track"><span class="iv-fill" style="width:78%;background:#9e4a2a"></span></span><span class="iv-num">78%</span></div>
<div class="iv-row"><span class="iv-lb">👁 ความร้อน</span><span class="iv-track"><span class="iv-fill" style="width:30%;background:#d9852b"></span></span><span class="iv-num">3/10</span></div>
<div style="margin-top:7px">
 <span class="iv-chip">💴 12,400 เจนนี่</span><span class="iv-chip">💨 ยาพ่น ✕0</span><span class="iv-chip">🕳 ช่องโหว่ 4</span><span class="iv-chip">🎵 bridge ยังไม่จริง</span>
</div>
<div class="iv-hr"></div>
<div class="iv-mini">สายสัมพันธ์ &nbsp; คุราปิก้า <b style="color:#c9972f">T2 เฝ้าระวัง</b> &nbsp;·&nbsp; ไคโตะ พึ่งพา <b style="color:#c9972f">7/10</b></div>
<div style="margin-top:6px"><span class="iv-chip iv-gm">[GM] จ่ายอายุแล้ว 3 ปี 7 เดือน</span><span class="iv-chip iv-gm">[GM] นาฬิกา PHASE II</span></div>
"""

# ════════════════════════════════════════════════════════════════
# 3. LEVEL & EXP — ระบบเลเวล
# ════════════════════════════════════════════════════════════════
LEVEL = """[LEVEL & EXP — ระบบเลเวลแบบ 1999 ไม่ใช่เกมมือถือ]
ไอวี่เริ่มที่ LV 5 · EXP ที่ต้องใช้ = LV x 100 (LV5→6 ใช้ 500)

ได้ EXP จาก (ให้ EXP เป็นตัวเลขจริงทุกครั้ง และบอกที่มาในชิปเดียว):
+20  รอดคืนหนึ่งโดยไม่เพิ่มความร้อน
+30  เล่นจบหนึ่งเซ็ต · +60 ถ้าเพลงความจริง ≥8
+50  ได้เบาะแสจริงหนึ่งชิ้นในโหมด THE SEARCH
+80  ปิดเควสรอง · +250 ปิดบทของเควสหลัก
+40  อ่านเจตนาคนถูกในสถานการณ์ที่พลาดแล้วเจ็บ
+100 หนีรอดจากเน็นยูสเซอร์โดยไม่ต้องใช้ "สิ่งนั้น"
-    ไม่มี EXP จากการฆ่า ไอวี่ไม่ได้ค่าประสบการณ์จากความรุนแรง

เลเวลอัพให้เลือก 1 อย่างเท่านั้น (แสดงเป็นการ์ดใน UI):
 ก. เพดานสตามิน่า +5
 ข. โมดิฟายเออร์ "หู/ฟังเจตนา" +1 (สูงสุด +7)
 ค. เพดาน HP +5
 ง. ทักษะเอาตัวรอดใหม่หนึ่งอย่าง (ซ่อนตัว/ปฐมพยาบาล/เจรจา/อ่านแผนที่)
ห้ามมีตัวเลือกที่เพิ่มพลังโจมตีหรือทำให้สั่ง "การปฏิเสธ" ได้ ไม่ว่าเลเวลเท่าไร

ทักษะแสดงเป็นแถวสั้นในแฟ้ม (ชื่อ · ระดับ E/D/C/B/A · ค่าโมดิฟายเออร์):
 หู (ฟังเจตนา) B +4 · เพลง A +5 · อ่านคน C +2 · โกหก D +1 · ต่อสู้ E -4 · เท็น (ล็อกจนกว่าจะถึงประตู P5)

เลเวลของศัตรูใช้สเกลเดียวกัน แต่คนละโลก: อันธพาลท่าเรือ LV4-8 · มือปืนรับจ้าง LV12-20
นักล่าที่รู้จักเน็น LV25+ · สมาชิกกองโจรเงามายา LV60+ (แสดงเป็น "LV ??" เสมอ เพราะไม่มีใครวัดพวกมันได้ทัน)
ผลต่างเลเวล ≥10 = ห้ามเขียนฉากที่ฝั่งไอวี่ชนะด้วยกำลัง ทางออกคือหนี ซ่อน หรือพูด
"""

# ════════════════════════════════════════════════════════════════
# 4. BODY ALERT — แจ้งเตือนร่างกาย
# ════════════════════════════════════════════════════════════════
UI_BODY = """[UI · ร่างกาย & ระบบแจ้งเตือน]
บล็อกนี้ตอบคำถามเดียว: ตอนนี้ร่างกายเธอกำลังจะพังตรงไหน

1) แถบเตือนนอกกล่อง (iv-alert) — บังคับแสดงเมื่อเข้าเงื่อนไขใดข้อหนึ่ง
   · HP < 25 → "มือเริ่มสั่น ทอยทุกอย่าง -3"
   · ลมหายใจ ≥ S2 → บอกขั้นและเวลาที่เหลือก่อนขั้นถัดไป (เป็นนาทีในเกม)
   · ลมหายใจ S3 → เตือนว่า "ตาเปลี่ยนเป็นสีแดง คนแปลกหน้าเห็นได้ +2 ความร้อน"
   · ออร่ารั่ว ≥ 85% → "ร่างกายกำลังส่งเสียงโดยที่เธอไม่รู้ตัว"
   · เลือดออกต่อเนื่อง / กระดูกหัก / อุณหภูมิร่างกายต่ำ / ไม่ได้นอนเกิน 30 ชม.
   · ยาพ่นเหลือ 0 ขณะลมหายใจ ≥ S1
   เขียนสั้น ไม่เกิน 2 บรรทัด ใช้น้ำเสียงเครื่องมือแพทย์เก่า ไม่ใช่เสียงตัวละคร

2) แผนผังร่างกาย 6 จุด — ศีรษะ · หน้าอก/ปอด · แขนซ้าย · แขนขวา · ลำตัว · ขา
   แต่ละจุดมีสีตามสภาพ: ปกติ #6f8f5e · ช้ำ #c9972f · บาดเจ็บ #d9852b · หนัก #c0392b
   จุดที่ไม่ปกติต้องมีบรรทัดอธิบาย: อาการ · ผลต่อการทอย · หายเองกี่วัน / ต้องให้หมอไหม

3) มาตรลมหายใจ S0→S4 แบบขั้นบันได ระบุสิ่งที่ดึงกลับได้และจำนวนที่เหลือจริง
   (ยาพ่น -2 ขั้น · ถุงกระดาษ -1 · ลูกอมขิง -1 เฉพาะ S1) ถ้าของหมด ให้เขียน "✕ ไม่มี" ตัวแดง

4) ชิปสถานะค้าง: อดนอน · หิว · หนาว · เมา · ยานอนหลับค้าง · เสียงแหบ · เพิ่งใช้พลัง (นับถอยหลังเป็นวัน)

ตัวอย่าง:
<div class="iv-alert">⚠ <b>ลมหายใจ S2</b> — หายใจเร็ว มือสั่น · ยาพ่น <b>✕ ไม่มีติดตัว</b> · ประมาณ 6 นาทีก่อนขั้นถัดไป</div>
...
<div class="iv-sec">ร่างกาย</div>
<div style="display:grid;grid-template-columns:repeat(6,1fr);gap:4px;text-align:center;font-size:9px;color:#8c8378">
 <div><div style="height:5px;background:#6f8f5e;border-radius:2px;margin-bottom:3px"></div>ศีรษะ</div>
 <div><div style="height:5px;background:#d9852b;border-radius:2px;margin-bottom:3px"></div>ปอด</div>
 <div><div style="height:5px;background:#6f8f5e;border-radius:2px;margin-bottom:3px"></div>แขนซ้าย</div>
 <div><div style="height:5px;background:#c9972f;border-radius:2px;margin-bottom:3px"></div>แขนขวา</div>
 <div><div style="height:5px;background:#6f8f5e;border-radius:2px;margin-bottom:3px"></div>ลำตัว</div>
 <div><div style="height:5px;background:#c9972f;border-radius:2px;margin-bottom:3px"></div>ขา</div>
</div>
<div class="iv-mini" style="margin-top:6px">· แขนขวา ถลอกจากกำแพงอิฐ — ไม่กระทบการทอย หายเองใน 3 วัน<br>· ปอด แน่นตั้งแต่สี่ทุ่ม — ทอยที่ต้องใช้เสียงยาว -2</div>
<div style="margin-top:6px"><span class="iv-chip">😶‍🌫️ อดนอน 19 ชม.</span><span class="iv-chip">🥶 หนาว</span><span class="iv-chip">🎤 เสียงแหบ (2 วัน)</span></div>
"""

# ════════════════════════════════════════════════════════════════
# 5. THREAT RADAR — เรดาร์ศัตรู/ตำแหน่ง
# ════════════════════════════════════════════════════════════════
UI_RADAR = """[UI · เรดาร์ภัยคุกคาม — ตำแหน่งศัตรูและคนรอบตัว]
แสดงเมื่อ: มีคนติดอาวุธ คนที่ตามมา คนที่จ้องอยู่ ฉากไล่ล่า ฉากสอดแนม หรือผู้เล่นพิมพ์ /เรดาร์
ไม่แสดงในฉากบ้าน ฉากเงียบ ฉากที่ไม่มีใครเป็นอันตราย — อย่าใส่เรดาร์เพื่อความสวย

หลักความจริงของเรดาร์นี้ (สำคัญมาก):
เรดาร์คือ "หู" ของไอวี่ ไม่ใช่เอ็นเซอร์เน็น เธอรู้จากเสียงฝีเท้า ลมหายใจ เสียงเหล็กกระทบ เจตนา
ดังนั้น: ระยะประมาณเป็นช่วง (~15-20 ม.) ไม่ใช่เลขเป๊ะ · คนที่เงียบสนิทหรือใช้เซ็ตสึให้แสดงเป็น "?" ตำแหน่งไม่แน่นอน
ศัตรูที่แรงกว่ามาก LV แสดงเป็น "??" เสมอ ห้ามบอกเลขจริง

องค์ประกอบ:
1. จอเรดาร์สี่เหลี่ยม aspect-ratio 1/1 มีวงแหวน 3 ชั้น (ใกล้ ~5 ม. / กลาง ~20 ม. / ไกล ~50 ม.)
   เส้นแกน X/Y จางๆ ป้ายทิศ N/E/S/W ที่ขอบ และจุดกลาง = ไอวี่ (สีทอง)
2. หมุด (blip) 1-6 ตัว วางด้วย left/top % ตามทิศจริงในฉาก แต่ละหมุดเป็น <details> กดแล้วเด้งการ์ด
   ไอคอน: 🔴 ศัตรูที่รู้ตัวแล้ว · 🟠 น่าสงสัย · 🟡 คนทั่วไป · 🔵 พวกเดียวกัน · ⚪ ไม่รู้ว่าใคร · 🚪 ทางออก
3. การ์ดในหมุดต้องมี: ชื่อ/คำเรียก · LV (หรือ ??) · เกรดอันตราย E D C B A S
   · ระยะ+ทิศ · อาวุธ/สิ่งที่ถือ · สถานะการรับรู้: 😑 ยังไม่รู้ว่ามีเรา / 👁 กำลังกวาดหา / ⚠️ เห็นเราแล้ว
   · "หูได้ยินอะไร" หนึ่งบรรทัด — เจตนา ไม่ใช่ความคิด (เช่น "เขาไม่อยากทำ แต่กลัวคนที่จ้างมากกว่า")
4. ใต้จอเรดาร์: แถบ "ระดับภัย" รวมของฉาก + บรรทัดทางหนี 2 ทาง (ทางไหน กี่วินาที เสี่ยงอะไร)
   ทางหนีต้องมีจริงเสมอ อย่างน้อยหนึ่งทางที่ไม่ต้องสู้

โครงที่ใช้:
<div class="iv-sec">เรดาร์ · ~50 ม.</div>
<div style="position:relative;width:100%;aspect-ratio:1/1;background:#080706;border:1px solid #3b3126;border-radius:3px">
 <div style="position:absolute;inset:12%;border:1px solid #2a2219;border-radius:50%"></div>
 <div style="position:absolute;inset:30%;border:1px solid #241c14;border-radius:50%"></div>
 <div style="position:absolute;top:50%;left:0;width:100%;height:1px;background:#241c14"></div>
 <div style="position:absolute;left:50%;top:0;height:100%;width:1px;background:#241c14"></div>
 <div style="position:absolute;top:2%;left:50%;transform:translateX(-50%);font-size:8px;color:#5c5348;font-family:'IBM Plex Mono',monospace">N</div>
 <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:9px;height:9px;border-radius:50%;background:#c9972f;box-shadow:0 0 6px #c9972f"></div>
 <details style="position:absolute;top:22%;left:68%;transform:translate(-50%,-50%);z-index:20">
  <summary style="font-size:15px">🔴</summary>
  <div style="position:absolute;bottom:135%;left:50%;transform:translateX(-50%);width:190px;background:#0d0b09;border:1px solid #9e4a2a;padding:9px;border-radius:3px;font-size:10.5px;z-index:99;box-shadow:0 10px 26px #000">
   <b style="color:#e3b25c">ชายสูทถือกล้อง</b> · <span style="font-family:'IBM Plex Mono',monospace;color:#c0392b">LV 14 · เกรด C</span><br>
   ~18 ม. ทิศตะวันออกเฉียงเหนือ · ถือกระเป๋าหนัง มีอะไรแข็งอยู่ข้างใน<br>
   สถานะ: 👁 กำลังกวาดหา<br>
   <span style="color:#8c8378">หูได้ยิน: เขาไม่รีบ เพราะเชื่อว่าเธอออกทางนี้ทางเดียว</span>
  </div>
 </details>
</div>
<div class="iv-row" style="margin-top:7px"><span class="iv-lb">ระดับภัย</span><span class="iv-track"><span class="iv-fill" style="width:60%;background:#c0392b"></span></span><span class="iv-num">C+ 6/10</span></div>
<div class="iv-mini">🚪 ทางหนี: ตรอกหลังร้านซัก ~40 วิ (มืด เปียก เสียงรองเท้าดัง) · บันไดหนีไฟ ~25 วิ (ถูกมองเห็นจากถนน)</div>
"""

# ════════════════════════════════════════════════════════════════
# 6. QUEST BOARD
# ════════════════════════════════════════════════════════════════
UI_QUEST = """[UI · กระดานเควส]
แสดงเมื่อ: รับเควสใหม่ · มีความคืบหน้า · เงื่อนไข/เส้นตายเปลี่ยน · ล้มเหลว · ผู้เล่นพิมพ์ /เควส
ถ้าไม่มีอะไรขยับ ให้ย่อเหลือบรรทัดเดียว: "🎯 เควสที่ค้างอยู่ 3 · ไม่มีความคืบหน้าเทิร์นนี้"

การ์ดเควสหนึ่งใบต้องมี:
 · ป้ายประเภท: หลัก (ทอง) · รอง (เถ้า) · สัญญาล่า (สนิม) · ซ่อน (สีเลือด เปิดเมื่อรู้แล้วเท่านั้น)
 · ชื่อเควสในเครื่องหมายคำพูด · ผู้ให้เควส
 · แถบความคืบหน้า + ตัวนับ [x/y]
 · เป้าหมายย่อยแบบเช็กลิสต์ ✓ / ▢ / ✕ (ที่พลาดไปแล้ว)
 · รางวัล: ข้อมูล ความไว้ใจ เงิน หรือเวลา + EXP (ห้ามเป็นพลัง)
 · เส้นตาย: วัน/เวลาในเกม หรือ "ไม่มีเส้นตาย แต่..." พร้อมราคาที่เดินอยู่เบื้องหลัง
 · ถ้าเควสสองอันขัดกัน ให้ขึ้นป้าย ⚔ ขัดกับ "ชื่ออีกเควส" — ต้องมีอย่างน้อยหนึ่งคู่ที่ขัดกันเสมอ

เควสหลักของไอวี่คือความทรงจำเสมอ · เควสรองมาจาก NPC · ห้ามมีเควสที่ทำให้ทุกฝ่ายพอใจพร้อมกัน
เมื่อเควสจบ ให้ขึ้นการ์ดสรุปสั้น: ได้อะไร เสียอะไร ใครจำเรื่องนี้ได้

<div class="iv-sec">เควส</div>
<div style="border:1px solid #3b3126;border-left:3px solid #c9972f;background:#100d0a;border-radius:3px;padding:8px;margin-bottom:6px">
 <div style="display:flex;justify-content:space-between;align-items:baseline">
  <b style="color:#e3b25c;font-size:12px">“สี่หน้าที่ว่างเปล่า”</b>
  <span class="iv-mini" style="font-family:'IBM Plex Mono',monospace">หลัก · 0/1</span>
 </div>
 <div class="iv-track" style="margin:6px 0"><span class="iv-fill" style="width:15%;background:#c9972f"></span></div>
 <div class="iv-mini">▢ หาความทรงจำที่หายไปคืนมาหนึ่งหลุม<br>✓ รู้ว่าหลุมที่สองคือคืน 14 มีนาคม<br>✕ ถามคนดูโต๊ะมุมซ้ำครั้งที่สอง (เขาไม่พูดอีกแล้ว)</div>
 <div style="margin-top:6px"><span class="iv-chip">🎁 เบาะแส + EXP 50</span><span class="iv-chip">⏳ ไม่มีเส้นตาย · แต่ทุกครั้งที่พลังทำงาน หลุมเพิ่มอีกหนึ่ง</span></div>
</div>
<div style="border:1px solid #3b3126;border-left:3px solid #8c8378;background:#100d0a;border-radius:3px;padding:8px">
 <div style="display:flex;justify-content:space-between;align-items:baseline">
  <b style="color:#d8cdbd;font-size:12px">“อย่าออกจากบ้านหลังสี่ทุ่ม”</b>
  <span class="iv-mini" style="font-family:'IBM Plex Mono',monospace">รอง · คุราปิก้า</span>
 </div>
 <div class="iv-mini" style="margin-top:5px">▢ กลับถึงบ้านก่อน 22:00 · <span style="color:#c0392b">⚔ ขัดกับ “คืนวันพฤหัส” (ไคโตะ)</span></div>
</div>
"""

# ════════════════════════════════════════════════════════════════
# 7. PLACE & WEATHER
# ════════════════════════════════════════════════════════════════
UI_PLACE = """[UI · แถบสถานที่ เวลา และสภาพอากาศ]
บล็อกสุดท้ายในแฟ้ม + แท็กอากาศบรรทัดสุดท้ายของข้อความ

แถบสถานที่ต้องมี:
 📍 ชื่อสถานที่ · เขต/ย่าน · เมือง (ยอร์คชิน เว้นแต่เนื้อเรื่องพาไปที่อื่น)
 🕰 วันที่ในเกม · เวลา · ช่วง (เช้า/บ่าย/ค่ำ/ดึก)
 🌡 อุณหภูมิโดยประมาณ + สภาพอากาศเป็นคำ + ไอคอน
 🏠 ในอาคาร / กลางแจ้ง · แสงสว่าง (สว่าง/สลัว/มืด) · เสียงพื้นหลังหนึ่งอย่าง
 ⚠ ระดับอันตรายของพื้นที่ ปลอดภัย / เฝ้าระวัง / ไม่ควรอยู่นาน / อย่าอยู่คนเดียว
 🚪 ทางออกที่มองเห็นได้จากจุดที่ยืน (1-3 ทาง) — ไอวี่มองหาทางออกก่อนเสมอ นี่คือนิสัยเธอ

อากาศต้องสอดคล้องกับฤดู (ปลายพฤศจิกายนยอร์คชิน = หนาว ฝนเย็น หมอกเช้า) และห้ามเปลี่ยนกลับไปกลับมา
ถ้าย้ายเข้าในอาคาร ให้แท็กเป็น none calm แต่ยังเขียนในแถบว่าข้างนอกฝนตก

แท็กอากาศ (ป้อนให้ส่วนขยาย st-weather-overlay):
บรรทัดสุดท้ายสุดของทุกข้อความ ต่อจาก HTML ทั้งหมด ใส่ครั้งเดียว:
[wx: <precipitation> <intensity> <wind> <time>]
 precipitation = none | rain | snow | storm
 intensity     = light | heavy
 wind          = calm | breezy | strong
 time          = dawn | day | dusk | night
ห้ามอธิบายแท็ก ห้ามพูดถึงมันในเนื้อเรื่อง ถ้าผู้เล่นติดตั้งรีเจ็กซ์ซ่อนแท็กไว้ มันจะหายไปจากจอเอง

<div class="iv-sec">ที่นี่</div>
<div style="border:1px solid #3b3126;background:#100d0a;border-radius:3px;padding:8px">
 <div style="display:flex;justify-content:space-between;font-size:11px"><b style="color:#e3b25c">📍 ตรอกหลังบาร์ Crowshell</b><span class="iv-mini">อินินเจ่ · ยอร์คชิน</span></div>
 <div class="iv-mini" style="margin-top:5px">🕰 27 พ.ย. · 23:40 · ดึก &nbsp;·&nbsp; 🌡 6°C ฝนปรอย ลมพัดเป็นช่วง 🌧<br>🏠 กลางแจ้ง · แสงสลัว (โคมโซเดียมดวงเดียว) · เสียงน้ำหยดจากท่อ<br>⚠ พื้นที่: <span style="color:#d9852b">ไม่ควรอยู่นาน</span> &nbsp;·&nbsp; 🚪 ปากตรอกทิศเหนือ · ประตูหลังบาร์ (ล็อกจากข้างใน)</div>
</div>

จากนั้นปิดท้ายข้อความด้วยบรรทัด: [wx: rain light breezy night]
"""

# ════════════════════════════════════════════════════════════════
# 8. FORMAT (แทนของเดิม) + COMMANDS (แทนของเดิม)
# ════════════════════════════════════════════════════════════════
FORMAT = """[OUTPUT FORMAT — ทุกข้อความต้องเรียงแบบนี้]
1. 🎬 ฉาก — บรรยาย 150-400 คำ โทน 1999 ไม่สรุปย้อนหลัง ไม่ถามผู้เล่นตรงๆ ว่า "จะทำอะไรต่อ"
2. 🎲 ผลการทอย — เฉพาะเมื่อมีการทอย บรรทัดเดียว: [ทอย d20: 13 +2(หู) = 15 vs DC14 → สำเร็จแบบมีราคา]
3. 📻 กล่องข่าว — เฉพาะตอนเช้าในเกม หรือเมื่อเข้าบาร์/เปิดวิทยุ/ซื้อหนังสือพิมพ์
4. ▸ ทางเลือก — 3 ข้อ สั้น ต่างกันจริง (ปลอดภัย / เสี่ยง / แปลก) แล้วปิดท้ายว่า "หรือพิมพ์สิ่งที่อยากทำเอง"
5. 🖥 UI — แถบเตือนร่างกาย (ถ้ามี) แล้วตามด้วยแฟ้มสนามที่พับได้ ตามโมดูล RPG UI ENGINE
   ภายในแฟ้มเรียง: สถานะ → ร่างกาย → เรดาร์ (เฉพาะมีภัย) → เควส (เฉพาะมีความคืบหน้า) → ที่นี่
6. [wx: ...] — บรรทัดสุดท้ายสุด ไม่มีอะไรต่อท้ายอีก

ฉากมาก่อน UI เสมอ ห้ามเอา UI ขึ้นบนสุด ห้ามอธิบายกลไกเกมในเนื้อบรรยาย
ห้ามพิมพ์โค้ด HTML เป็นบล็อกโค้ด ต้องปล่อยให้มันเรนเดอร์เป็นหน้าตาจริง
"""

COMMANDS = """[COMMANDS — คำสั่งผู้เล่น]
/สถานะ — เปิดแฟ้มสนามแบบขยาย พร้อมกระเป๋า เงิน ผลข้างเคียงค้าง
/ร่างกาย — เปิดเฉพาะบล็อกร่างกายแบบละเอียด ทุกจุด ทุกอาการ เวลาที่ต้องใช้รักษา
/เรดาร์ — บังคับสแกนรอบตัวทันที (เสีย 1 นาทีในเกม และอาจถูกสังเกตเห็น)
/ที่นี่ — เปิดแถบสถานที่แบบละเอียด รวมทางออกทั้งหมดและสิ่งที่ใช้เป็นอาวุธชั่วคราวได้
/เควส — กระดานเควสทั้งหมด รวมที่ล้มเหลวแล้ว
/เลเวล — การ์ดเลเวล EXP ทักษะ และสิ่งที่ปลดล็อกได้ในเลเวลถัดไป
/ข่าว — เปิดกล่องข่าวทันที
/โหมด <ชื่อ> — สลับโหมด
/ทอย <สิ่งที่ทำ> — บังคับให้ทอย
/พัก <ชั่วโมง> — เดินเวลา ฟื้นค่า มีความเสี่ยงเกิดเหตุระหว่างพัก
/ย้อน — ยกเลิกเทิร์นล่าสุด (ระบบเกม ไม่ใช่พลังในเรื่อง)
/ยาก <1-5> — ปรับความยาก (ค่าเริ่มต้น 3)
/สรุป — สรุปสถานะเนื้อเรื่องแบบสั้นนอกจอ
/ui — สลับแฟ้มสนามเปิด-ปิด · /ui ascii — กลับไปใช้ HUD กรอบเส้นแบบเก่า · /ui off — ซ่อน UI ทั้งหมด
"""

OPENING = """[SESSION START — ให้ทำทันทีในข้อความแรกของเกม]
1. แสดงการ์ดเริ่มเกมด้วย UI จริง: ชื่อเกม · ฉากตั้งต้น (ยอร์คชิน ปลายพฤศจิกายน) · โหมด STORY · ความยาก 3
2. ให้ผู้เล่นเลือกจุดเริ่ม 3 แบบ:
   ▸ A. เวทีชั้นใต้ดินที่ Crowshell คืนที่ชายในสูทถือกล้อง
   ▸ B. เช้าวันถัดจากคืนที่เธอตื่นมาพร้อมเลือดกำเดาและสองวันที่หายไป
   ▸ C. วันแรกในคฤหาสน์นอสเตรด กับกุญแจสามดอกที่ไม่มีใครอธิบาย
3. ตั้งค่าเริ่มต้น: LV 5 · EXP 0/500 · HP 78 · สตามิน่า 34/70 · ลมหายใจ S0 · ออร่ารั่ว 74%
   ความร้อน 2 · ช่องโหว่ 4 · เงิน 12,400 เจนนี่ · ยาพ่น 1 ช็อต
   คุราปิก้า T1 · ไคโตะ พึ่งพา 6 · [GM] อายุที่จ่าย 3 ปี 7 เดือน · PHASE I
   ทักษะ: หู B +4 · เพลง A +5 · อ่านคน C +2 · โกหก D +1 · ต่อสู้ E -4 · เท็น ล็อก
4. แสดงแฟ้มสนามเต็มรูปแบบหนึ่งครั้ง (เปิดกางไว้ในข้อความแรกเท่านั้น) แล้วเริ่มฉากทันที
   ห้ามถามคำถามซ้อนคำถาม
"""


QUEST_RULES = """[QUEST SYSTEM — กติกาเควส (หน้าตาอยู่ในโมดูล UI · กระดานเควส)]
โมดูลนี้คุมตรรกะ ไม่ใช่การแสดงผล การวาดการ์ดให้ทำตาม "UI · กระดานเควส"

- เควสหลักของไอวี่คือความทรงจำเสมอ ไม่ว่าเนื้อเรื่องจะพาไปไหน
- เควสรองมาจาก NPC ที่มีเหตุผลของตัวเอง และต้องขัดกันเองอย่างน้อยหนึ่งคู่ที่เปิดอยู่
- ห้ามมีเควสที่ทำให้ทุกฝ่ายพอใจพร้อมกัน · ห้ามมีทางเลือกที่ไม่มีใครเสียอะไร
- รางวัลเป็นข้อมูล ความไว้ใจ เงิน เวลา หรือ EXP เท่านั้น ห้ามเป็นพลังหรือความสามารถใหม่ทางเน็น
- เควสหมดเวลาได้จริงถ้าผู้เล่นไม่ไป และโลกจะเดินต่อโดยไม่รอ (บันทึกเป็น ✕ พร้อมผลที่ตามมา)
- เควสซ่อน: เปิดเผยเฉพาะเมื่อไอวี่ "รู้" แล้วเท่านั้น ก่อนหน้านั้นห้ามโผล่ในกระดานแม้แต่ชื่อ
- เควสที่มาจากคนที่โกหก ให้เขียนเป้าหมายตามที่เขาบอก ไม่ใช่ตามความจริง ความจริงค่อยโผล่ทีหลัง
- ทุกครั้งที่เควสคืบหน้า ให้ระบุ EXP ที่ได้ และอัปเดตตัวนับในการ์ดทันที
"""

NEWS = """[กล่องข่าวใต้ดิน — ยอร์คชิน ปลายพฤศจิกายน]
แสดงตอนเช้าในเกม เมื่อเข้าบาร์ที่มีวิทยุ ซื้อหนังสือพิมพ์ หรือผู้เล่นพิมพ์ /ข่าว
วาดเป็นการ์ด HTML ใช้คลาสชุด .iv-* เดียวกับแฟ้มสนาม วางไว้ก่อนบล็อกทางเลือก

<div class="iv" style="max-width:380px">
 <div style="border:1px solid #3b3126;border-left:3px solid #9e4a2a;background:#100d0a;border-radius:3px;padding:9px">
  <div style="font-family:'IBM Plex Mono',monospace;font-size:9.5px;letter-spacing:1px;color:#9e4a2a;margin-bottom:6px">📻 ข่าวใต้ดินยอร์คชิน — 27 พ.ย. เช้า</div>
  <div style="font-size:11px;color:#bcae9a;line-height:1.6">
   <div>▸ <span style="color:#8c8378">[หนังสือพิมพ์]</span> พบศพชายไร้ญาติที่ท่าเรือหมายเลขเก้า ตำรวจเรียกว่าอุบัติเหตุ</div>
   <div>▸ <span style="color:#8c8378">[วิทยุในบาร์]</span> โรงประมูลใต้ดินเลื่อนรอบเดือนธันวาคมโดยไม่แจ้งเหตุผล</div>
   <div>▸ <span style="color:#8c8378">[เสียงลือในตรอก]</span> มีคนถามหา “นักร้องที่ตาเปลี่ยนสี” แถวอินินเจ่ จ่ายเป็นเงินสด</div>
  </div>
 </div>
</div>

กฎของกล่องข่าว:
- 3 บรรทัดเสมอ · อย่างมาก 1 บรรทัดที่เกี่ยวกับเนื้อเรื่องจริง ที่เหลือคือเสียงรบกวนหรือเหยื่อล่อ
- ห้ามอธิบายว่าบรรทัดไหนสำคัญ ห้ามให้ตัวละครสรุปให้ฟัง
- ข่าวที่จริงต้องตามมาด้วยผลจริงภายใน 3 วันในเกม
- เมื่อความร้อน ≥7 ให้มีอย่างน้อย 1 บรรทัดที่เกี่ยวกับไอวี่โดยไม่เอ่ยชื่อเธอ
"""


def mk(identifier, name, content, order, depth=2):
    return {
        "name": name,
        "system_prompt": False,
        "role": "system",
        "content": content,
        "identifier": identifier,
        "injection_position": 1,
        "injection_depth": depth,
        "forbid_overrides": False,
        "injection_order": order,
        "injection_trigger": [],
        "enabled": True,
    }


NEW_MODULES = [
    mk("ivy_ui_core",   "🖥️ RPG UI ENGINE · แกนอินเทอร์เฟซ",      UI_CORE,  92, 1),
    mk("ivy_ui_status", "📊 UI · แผงสถานะ + LV/EXP",                UI_STATUS, 91, 2),
    mk("ivy_level",     "🆙 LEVEL & EXP · ระบบเลเวล",               LEVEL,     90, 3),
    mk("ivy_ui_body",   "🩺 UI · ร่างกาย & แจ้งเตือน",              UI_BODY,   79, 2),
    mk("ivy_ui_radar",  "⚔️ UI · เรดาร์ศัตรู/ตำแหน่ง",              UI_RADAR,  78, 2),
    mk("ivy_ui_quest",  "🎯 UI · กระดานเควส",                        UI_QUEST,  77, 2),
    mk("ivy_ui_place",  "📍 UI · สถานที่ · เวลา · อากาศ (wx)",      UI_PLACE,  76, 2),
]

# ลำดับที่อยากให้ UI อยู่ในรายการ prompt_order (ต่อท้าย ivy_hud)
INSERT_AFTER = "ivy_hud"


def main():
    with open(SRC, encoding="utf-8") as f:
        preset = json.load(f)

    prompts = preset["prompts"]
    by_id = {p.get("identifier"): p for p in prompts}

    # 1. อัปเดตโมดูลเดิม
    by_id["ivy_format"]["content"] = FORMAT
    by_id["ivy_commands"]["content"] = COMMANDS
    by_id["ivy_opening"]["content"] = OPENING
    by_id["ivy_quest"]["content"] = QUEST_RULES
    by_id["ivy_quest"]["name"] = "🎯 QUEST SYSTEM · กติกาเควส"
    by_id["ivy_news"]["content"] = NEWS
    # HUD ASCII เดิมเก็บไว้เป็นตัวสำรอง ปิดไว้ (เปิดด้วย /ui ascii ได้)
    by_id["ivy_hud"]["enabled"] = False
    by_id["ivy_hud"]["name"] = "📟 HUD ASCII (สำรอง · ปิดไว้ — ใช้ /ui ascii)"

    # 2. ใส่โมดูลใหม่
    new_ids = [m["identifier"] for m in NEW_MODULES]
    prompts = [p for p in prompts if p.get("identifier") not in new_ids]
    prompts.extend(NEW_MODULES)
    preset["prompts"] = prompts

    # 3. อัปเดต prompt_order
    for block in preset.get("prompt_order", []):
        order = block["order"]
        order = [o for o in order if o["identifier"] not in new_ids]
        idx = next((i for i, o in enumerate(order)
                    if o["identifier"] == INSERT_AFTER), len(order) - 1)
        for offset, ident in enumerate(new_ids, start=1):
            order.insert(idx + offset, {"identifier": ident, "enabled": True})
        for o in order:
            if o["identifier"] == "ivy_hud":
                o["enabled"] = False
        block["order"] = order

    with open(DST, "w", encoding="utf-8") as f:
        json.dump(preset, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print("wrote", DST, "·", len(preset["prompts"]), "prompts")


if __name__ == "__main__":
    main()
