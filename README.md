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
| 🎮 | `preset/IVY1999_RPG_UI.json` | **IVY 1999 · RPG UI** — เพรสเซ็ต SillyTavern พร้อม UI แบบเกม RPG (เรดาร์ศัตรู · เลเวล/EXP · เควส · แจ้งเตือนร่างกาย · สถานที่/อากาศ) |
| 🎮 | `preset/IVY1999_RPG_Preset.json` | เพรสเซ็ตตั้งต้น (HUD แบบ ASCII) เก็บไว้เทียบ |
| 👁️ | `preview/ivy1999-ui-preview.html` | หน้าพรีวิว เปิดในเบราว์เซอร์เพื่อดูหน้าตา UI ก่อนใช้จริง |
| 🛠️ | `tools/build_ivy1999_ui.py` | สคริปต์ประกอบเพรสเซ็ต UI จากเพรสเซ็ตตั้งต้น |
| 🌦️ | `weather/Hide-Weather-Tag.regex.json` | A **Regex** that hides the `[wx:]` tag from the chat (display-only; overlay still reads it) |

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

## 🎮 IVY 1999 · RPG UI — อินเทอร์เฟซแบบเกม

เพรสเซ็ต `preset/IVY1999_RPG_UI.json` ต่อยอดจากเพรสเซ็ต IVY 1999 เดิม โดยเปลี่ยน HUD กรอบเส้น
แบบ ASCII เป็น **UI จริงที่เรนเดอร์ด้วย HTML/CSS ในกล่องข้อความ** โทน 1999 (ทอง–สนิม–โซเดียม บนพื้นดำ)

ดูหน้าตาก่อนได้ที่ **`preview/ivy1999-ui-preview.html`** (เปิดด้วยเบราว์เซอร์ธรรมดา)

### มีอะไรบ้าง

| โมดูล | ทำอะไร |
|-------|--------|
| 🖥️ **RPG UI ENGINE** | แกนการวาด: พาเลตต์ ฟอนต์ สไตล์ชีต `.iv-*` และกติกา — ทุกอย่างอยู่ในแฟ้มที่ *พับได้* กว้างไม่เกิน 380px อ่านบนมือถือได้ |
| 📊 **แผงสถานะ + LV/EXP** | LV · แถบ EXP · HP · สตามิน่า · ลมหายใจ · ออร่ารั่ว · ความร้อน · เงิน · สายสัมพันธ์ · แถบ `[GM]` ที่ตัวละครไม่รู้ ค่าที่ขยับมีชิป `(-7)` กำกับพร้อมเหตุผล |
| 🆙 **LEVEL & EXP** | ระบบเลเวลจริง (LV×100 EXP ต่อระดับ) ได้ EXP จากการรอด เบาะแส เพลง เควส — **ไม่มี EXP จากการฆ่า** และไม่มีตัวเลือกเลเวลอัพที่เพิ่มพลังโจมตี |
| 🩺 **ร่างกาย & แจ้งเตือน** | แถบเตือนสีเลือด *นอก* กล่องพับ (HP<25, ลมหายใจ ≥S2, ออร่ารั่ว ≥85%, เลือดออก, ยาพ่นหมด) + ผังร่างกาย 6 จุดพร้อมผลต่อการทอยและเวลาที่ต้องใช้รักษา |
| ⚔️ **เรดาร์ศัตรู** | จอเรดาร์ ~50 ม. มีวงแหวน/แกน/ทิศ · หมุดกดได้ 1–6 ตัว บอก **LV · เกรดอันตราย E–S · ระยะ+ทิศ · อาวุธ · รู้ตัวเราหรือยัง** · แถบระดับภัยรวม และ **ทางหนี 2 ทางเสมอ** |
| 🎯 **กระดานเควส** | การ์ดเควสหลัก/รอง/สัญญาล่า/ซ่อน มีแถบความคืบหน้า เช็กลิสต์ ✓▢✕ รางวัล เส้นตาย และป้าย ⚔ เมื่อเควสสองอันขัดกัน |
| 📍 **สถานที่ · เวลา · อากาศ** | ชื่อสถานที่/ย่าน · วันเวลา · อุณหภูมิ+สภาพอากาศ · ในอาคาร/กลางแจ้ง · ระดับอันตรายของพื้นที่ · ทางออกที่มองเห็น แล้วปิดท้ายข้อความด้วยแท็ก `[wx: ...]` |
| 📻 **กล่องข่าว** | เปลี่ยนเป็นการ์ด HTML สไตล์เดียวกัน |

### เรดาร์ทำงานยังไง (จุดที่ทำให้ไม่หลุดคาแรกเตอร์)

เรดาร์คือ **"หู" ของไอวี่ ไม่ใช่เซนเซอร์เน็น** — เธออ่านจากเสียงฝีเท้า ลมหายใจ และเจตนา ดังนั้น:

- ระยะเป็นช่วงโดยประมาณ (`~18 ม.`) ไม่ใช่ตัวเลขเป๊ะ
- คนที่ใช้เซ็ตสึหรือเงียบสนิท → หมุด ⚪ ตำแหน่งไม่นิ่ง พร้อม `LV ??`
- ศัตรูที่แรงกว่ามาก (กองโจรเงามายา ฯลฯ) แสดง `LV ??` เสมอ และผลต่างเลเวล ≥10 แปลว่า **ห้ามเขียนฉากที่ชนะด้วยกำลัง** — ทางออกคือหนี ซ่อน หรือพูด

### ติดตั้ง

1. SillyTavern → **AI Response Configuration** (ไอคอนสไลเดอร์ซ้ายบน) → ปุ่ม **Import preset** → เลือก `preset/IVY1999_RPG_UI.json`
2. เลือกเพรสเซ็ต **IVY1999_RPG_UI** จากดรอปดาวน์
3. แนบ lorebook `lorebook/HxH_Lorebook_v48.json` (หรือเล่มของคุณเอง) — lorebook ยังเป็นความจริงสูงสุด เพรสเซ็ตคุมแค่ "หน้าตา"
4. อยากให้ฟ้าเปลี่ยนตามเรื่องด้วย: ติดตั้ง **st-weather-overlay** แล้วอิมพอร์ต `weather/Hide-Weather-Tag.regex.json` เพื่อซ่อนแท็ก `[wx:]` จากจอ (ดูหัวข้อ 🌦️ ด้านบน)

> เพรสเซ็ตสั่งให้โมเดลส่ง HTML ออกมาตรงๆ ถ้าเห็นเป็นโค้ดดิบในแชท ให้เช็กว่า
> *User Settings → **Show HTML tags / Render HTML*** เปิดอยู่ และอย่าเปิดโหมดที่บังคับ escape HTML

### คำสั่งในเกม

`/สถานะ` `/ร่างกาย` `/เรดาร์` `/ที่นี่` `/เควส` `/เลเวล` `/ข่าว` `/โหมด <ชื่อ>` `/ทอย` `/พัก <ชม.>`
`/ย้อน` `/ยาก <1-5>` `/สรุป` · `/ui` เปิด-ปิดแฟ้ม · `/ui ascii` กลับไปใช้ HUD แบบเดิม · `/ui off` ซ่อน UI

### อยากแก้ UI เอง

แก้ข้อความโมดูลใน `tools/build_ivy1999_ui.py` แล้วรัน:

```bash
python3 tools/build_ivy1999_ui.py
```

ไฟล์ `preset/IVY1999_RPG_UI.json` จะถูกสร้างใหม่จาก `preset/IVY1999_RPG_Preset.json`
(อยากเปลี่ยนสีอย่างเดียว แก้ค่าพาเลตต์ในโมดูล `ivy_ui_core` ที่เดียว แล้วไล่เปลี่ยนในเทมเพลตตัวอย่าง)

---

## Credits

- Weather overlay: **st-weather-overlay** by *xo.nara* — https://github.com/xo-nara/st-weather-overlay
- *Hunter × Hunter* © Yoshihiro Togashi. Vina is a fan original character; Kurapika, Killua and the
  Zoldyck/Kurta clans are used for non-commercial fan roleplay.
