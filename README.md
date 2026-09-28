# Lorebook HxH — Vina (Kurta × Zoldyck)

A SillyTavern pack for the original character **Vina** — Kurapika's childhood friend from
Lukso Province, trained in the assassin arts alongside Killua Zoldyck. It ships:

| # | File | What it is |
|---|------|------------|
| 🎨 | `theme/Vina - Kurta x Zoldyck.json` | A SillyTavern **UI theme** (import-ready, custom CSS embedded) |
| 🎨 | `theme/vina-custom.css` | The same custom CSS, un-minified, for editing |
| 📖 | `lorebook/Vina_HxH.json` | A full **World Info / lorebook** for Vina + a weather-director entry |
| 🌦️ | `lorebook/Weather_Director.json` | **Weather only** — just the `[wx:]` director entry, to drop into your *own* world without touching your canon |
| 🌦️ | `lorebook/Weather_Director_HxH.json` | Weather-only, **tuned for the v47/v48 HxH book** (declares the tag META so it obeys `★02 ANTI_OOC` / `★03 STYLE`, references the `303` climate canon) |
| 📚 | `lorebook/HxH_Lorebook_v48.json` | The user's **full 644-entry HxH book with the weather emitter already merged in** (now 645 entries, `00 SYS ★ 05`). Import this one file and weather is wired in. |
| 🌦️ | `weather/Hide-Weather-Tag.regex.json` | A **Regex** that hides the `[wx:]` tag from the chat (display-only; overlay still reads it) |
| 📚 | `lorebook/HxH_UNIFIED_v69_LEAN.json` | HxH UNIFIED v68 + **หมวดเน็นละเอียด** 9 entry (UID 7, 620, 99600–99606) · ตัดตัวอย่างหลังอาร์คยอร์คนิวออก |
| 📚 | `lorebook/Nen_Encyclopedia_HxH.json` | เฉพาะหมวดเน็น 9 entry แยกไฟล์ ไว้แนบคู่ lorebook อื่น (ถ้าใช้ v69 แล้วไม่ต้องแนบซ้ำ) |
| 🎮 | `preset/HxH_Hunter_RPG_Opus5_v1.json` | **Hunter RPG preset** for Claude Opus 5 — togglable RPG mode, HUD, quests, fate dice, Hard Mode, UI regex embedded |
| 🎮 | `preset/HxH_RPG_UI.regex.json` | The same UI regex scripts as a separate file (for reference / manual import) |

> **Note on the "Sullivan / Surilvan" spelling:** this is intentional in-world lore (entry `10` — *Surilvan* is the primary family name, *Sullivan* is William's branch spelling; both are valid), **not** a typo, so v48 leaves it untouched.

It's built to pair with the [**st-weather-overlay**](https://github.com/xo-nara/st-weather-overlay)
extension so the sky reacts to the story.

---

## 🎨 The theme — "Lore Tome"

A dark reading-tome look that fuses Vina's two halves:

- **Kurta** → scarlet (awakened eyes), warm parchment body text, aged gold headings, Lukso forest green.
- **Zoldyck** → near-black tome, electric violet italics, Killua-cyan accents, cold steel.

Design choices aimed at *reading lore comfortably*: serif justified body, ornamental `❖` dividers,
scarlet-glowing spoken quotes, gold clan headings, and translucent message "pages" so an ambient
weather overlay glows softly through from behind.

**Install**

1. In SillyTavern open **User Settings** (the top gear/user icon).
2. Next to *UI Theme* click the **import** (📥) button.
3. Select `theme/Vina - Kurta x Zoldyck.json`.
4. Pick **Vina - Kurta x Zoldyck** from the theme dropdown.

To tweak colours, edit the CSS variables at the top of `theme/vina-custom.css`
(`--vina-scarlet`, `--vina-lightning`, …) and paste the file back into
*User Settings → Custom CSS*, or re-import after re-embedding it.

---

## 📖 The lorebook

Import via **World Info → Import** and select `lorebook/Vina_HxH.json`, then attach it to
Vina's character card (or set it as a global lorebook).

Entries:

- **Vina — Core Profile** *(always on)* — who she is in one paragraph.
- **Appearance**, **Personality**, **Voice & Mannerisms** — keyword-triggered detail.
- **Lukso & Kurapika** — the childhood-friend backstory (triggers on `Kurapika`, `Kurta`, `Lukso`…).
- **Zoldyck & Killua** — assassin training (triggers on `Killua`, `Zoldyck`, `assassin`…).
- **Nen & Combat** — Transmuter; aura-wire hatsu *"Loom of Silence"* (triggers on `Nen`, `fight`, `wire`…).
- **SYSTEM — Ambient Weather Tag** *(always on)* — drives the weather overlay (see below).

> The backstory is written to be flexible — adjust her age, Nen type, or the exact reunion
> details to fit your canon by editing the entry `content` fields.

---

## 🌦️ Weather — driving st-weather-overlay

This pack does **not** re-implement weather; it makes Vina's world *speak* the tag language that
[xo-nara/st-weather-overlay](https://github.com/xo-nara/st-weather-overlay) already understands.

**1. Install the overlay** — in SillyTavern: *Extensions → Install extension →* paste
`https://github.com/xo-nara/st-weather-overlay` → enable **Ambient Weather Overlay**.

**2. Keep Auto Mode on** (Free Mode **off**) in the extension settings so it reads tags from messages.

**3. The lorebook does the rest.** The always-on *SYSTEM — Ambient Weather Tag* entry instructs the
model to end every reply with one tag:

```
[wx: <precipitation> <intensity> <wind> <time>]
```

| field | values |
|-------|--------|
| precipitation | `none` · `rain` · `snow` · `storm` |
| intensity | `light` · `heavy` |
| wind | `calm` · `breezy` · `strong` |
| time | `dawn` · `day` · `dusk` · `night` |

Examples: `[wx: rain light breezy dusk]` · `[wx: storm heavy strong night]` ·
`[wx: snow heavy calm day]` · `[wx: none calm calm dawn]`

The overlay parses the tag, syncs on edits/swipes/deletes, and renders matching particles, tint and
ambient audio. Because the theme's message pages are semi-transparent, rain and lightning read through
the story instead of sitting on top of it.

> Prefer to steer the sky by hand? Turn on **Free Mode** in the extension and use its dropdowns —
> the lorebook tag is simply ignored while Free Mode is active.

### Already have your own Vina world? Use the weather-only file

If you already run your own character card / lorebook and only want the weather behaviour, **don't**
import the full `Vina_HxH.json` (its lore may clash with your canon). Instead:

1. **World Info → Import** → `lorebook/Weather_Director.json` — one always-on entry, no story lore.
2. Attach it to your world (or set it global). Done — your existing canon is untouched.

### Hiding the tag from the chat

If `[wx: ...]` shows up as visible text in replies, import `weather/Hide-Weather-Tag.regex.json` via
**Extensions → Regex → Import**. It is set to *markdown/display only* (`placement: AI output`,
`markdownOnly: true`), so the tag disappears from view **but stays in the raw message** for the overlay
to parse. Do not make it "prompt only" or delete the raw text, or the overlay will stop reacting.

---

## 🎮 Hunter RPG preset (Claude Opus 5) — `preset/HxH_Hunter_RPG_Opus5_v1.json`

พรีเซ็ต SillyTavern สำหรับเล่น Lorebook **HxH UNIFIED v68** แบบเกม RPG — ต่อยอดจาก `ST_Claude_Preset_v11_HxH_v68`
(authority chain · Thai prose · NPC/Scheme engine · no-romance lock ยังอยู่ครบ) แล้วเพิ่มชั้นเกมที่เปิด/ปิดได้ทีละโมดูล

### ติดตั้ง

1. **API Connections** → Chat Completion → source **Claude** → model **`claude-opus-5`**
2. **AI Response Configuration** (แท็บซ้ายสุด) → Import preset → เลือกไฟล์ `preset/HxH_Hunter_RPG_Opus5_v1.json`
3. ตอน import ST จะถามว่าให้เปิด **regex ที่มากับพรีเซ็ต** ไหม → กด **อนุญาต** (นี่คือตัววาด UI การ์ด Hunter)
   ถ้า ST เวอร์ชันของคุณไม่รองรับ regex ในพรีเซ็ต ให้ import `preset/HxH_RPG_UI.regex.json` ผ่าน *Extensions → Regex* แทน
4. แนบ lorebook `HxH_UNIFIED_v68` ตามเดิม

> **หมายเหตุ Opus 5:** Opus 5 ไม่รองรับ assistant prefill และไม่รับ `temperature/top_p/top_k` —
> พรีเซ็ตนี้ปล่อย prefill ว่างไว้แล้ว ถ้า ST ขึ้น error 400 เรื่อง sampling/`budget_tokens` ให้อัปเดต SillyTavern เป็นเวอร์ชันล่าสุด
> (เวอร์ชันเก่าส่งพารามิเตอร์ที่รุ่นนี้ไม่รับ) · `max tokens` ตั้งไว้ 12000 เพราะรวม thinking ด้วย

### โมดูล (Prompt Manager)

| โมดูล | ค่าเริ่ม | ทำอะไร |
|---|---|---|
| 💪 Competence Floor | ✅ | กันวีน่าอ่อนเกินจริง: ไต่ระดับพลัง (คนธรรมดา/มาเฟีย < เธอ < บอดี้การ์ดเน็น < คิลัว/คุราปิก้า < แมงมุม) · ทักษะโซลดิ๊กไม่มีราคา · อาการป่วยโผล่เฉพาะเมื่อมีตัวกระตุ้น ≤1 ครั้ง/ฉาก · ล็อกตัวละครหลัก (กอน/คิลัว/คุราปิก้า/เลโอลีโอ) ให้เก่งตามแคนอน ไม่เจ็บจากเรื่องธรรมดาเช่นกระโดดตึก |
| 🎮 RPG Core — Hunter Status HUD | ✅ | HP (ค่าเลือด) · VITAL (พลังชีวิต) · AURA · MIND + ประเภทเน็น · สภาวะ · อายุขัยที่จ่ายไป · ยาเหลือ · ของ · เงิน · หนี้บุญคุณ · ตำแหน่ง/เวลา |
| 🪶 Mini HUD | ⬜ | ประหยัด token: การ์ดย่อ แสดงแบบเต็มเฉพาะเทิร์นที่ของ/เงิน/ที่อยู่เปลี่ยน |
| 📜 Quest Board | ✅ | ★ เควสหลัก (ดึงจาก STORY STATE / แผนลับ / แคนอนยอร์คนิว) · ◇ เควสรองจาก NPC · ⚄ เควสสุ่มมีเวลาจำกัด · ✔/✘ ผลลัพธ์ถาวร |
| 🎲 Fate Dice | ✅ | ST ทอย `{{roll:1d20}}`/`1d100` ให้จริงทุกเทิร์น — GM ตั้ง DC ก่อนดูลูกเต๋า · d100 ≤ 15 = เควสสุ่มโผล่ |
| ☠️ Hard Mode — Hunter Exam | ✅ | ศัตรูฉลาดตามแคนอน · ไม่มีแผน = แพ้ · ข้อมูลมีราคา · ทรัพยากรจำกัด · ถูกจับ/ตายได้ · ไม่มี power-up |
| ⚔️ Nen Combat & Tactics | ✅ | Ryu/Ko/Ken/Zetsu/En, ความได้เปรียบระหว่างสายเน็น, ท่าที่ถูกเห็นแล้วถูกแก้ทางได้ |
| 🎬 Title Card | ✅ | การ์ดชื่อตอนแบบมังงะโทงาชิ `No.47 ◆ สิบคืน` ตอนเปลี่ยนฉาก |
| 🎯 Action Hints | ⬜ | ตัวเลือก 3 ทางพร้อมความเสี่ยง (ไม่บอกว่าทางไหนถูก) |
| 🟢🟡🟠 Length | 🟡 | ความยาวร้อยแก้ว 2–3 / 3–5 / 5–7 ย่อหน้า — เปิดทีละอัน |

**ปิดทุกโมดูลในกลุ่ม 🎮** = กลับเป็นโหมดนิยายล้วนแบบ v11 (ประหยัด token ที่สุด)

### ประหยัด token

- Regex `🪶 ตัด HUD/Quest เก่า` ลบบล็อกเกมออกจาก **prompt** ทุกข้อความยกเว้นข้อความ AI ล่าสุด → โมเดลเห็นแค่ค่าสถานะปัจจุบัน ไม่เห็นประวัติ HUD ทั้งแชท
- โมเดลเขียน HUD แบบย่อ (`[[HP 82/100 82%]]`) — การ์ดสวย ๆ สร้างฝั่งหน้าจอโดย regex ไม่เสีย output token กับ HTML/CSS

### รูปแบบที่โมเดลเขียน → สิ่งที่คุณเห็น

```
<hxh_status>
◈ วีน่า เซอร์ลิแวน「The Timeless Doll」 · 特質系 สายพิเศษ
[[HP 71/100 71%]]
[[VITAL 64/100 64%]]
[[AURA 38/100 38%]]
[[MIND 45/100 45%]]
⚠ ลมหายใจตื้น · เลือดกำเดาไหลเมื่อชั่วโมงก่อน
⏳ อายุขัยที่จ่ายไป ≈3–5 วัน (+0)
💊 ยา Chronos-End: 10 คืน
📍 โรงแรมเบทาเคิล ห้อง 1204 · 28 ส.ค. 1999 23:40
</hxh_status>
<hxh_quest>
★ สิบคืน — หาแหล่งยาก่อนเม็ดสุดท้ายหมด · เบาะแส: ขวดพิมพ์ฝ่ายเวชกรรมประจำตระกูล · ⏱7 ก.ย.
</hxh_quest>
```

แสดงผลเป็นการ์ด *Hunter License* สีทอง-ดำ มีแถบ HP แดง · VITAL เขียว · AURA ม่วง · MIND ฟ้า, ป้าย `HUNTER × HUNTER`
และ Quest Log แบบเว็บฮันเตอร์

---

## Credits

- Weather overlay: **st-weather-overlay** by *xo.nara* — https://github.com/xo-nara/st-weather-overlay
- *Hunter × Hunter* © Yoshihiro Togashi. Vina is a fan original character; Kurapika, Killua and the
  Zoldyck/Kurta clans are used for non-commercial fan roleplay.
