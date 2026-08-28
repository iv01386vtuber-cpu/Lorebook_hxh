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

## Credits

- Weather overlay: **st-weather-overlay** by *xo.nara* — https://github.com/xo-nara/st-weather-overlay
- *Hunter × Hunter* © Yoshihiro Togashi. Vina is a fan original character; Kurapika, Killua and the
  Zoldyck/Kurta clans are used for non-commercial fan roleplay.

---

## 📕 HxH · Ivy Lee (Kurta Ember) — v7 LEAN

A separate, self-contained pack in [`hxh_ivy_v7/`](hxh_ivy_v7/) for the Kurapika × Ivy build,
rebuilt from the v5/v6 files: canon corrected to the Succession-Contest present, the OC's Hatsu
reworked into one lawful Specialist ability, and the always-on token cost cut from ~5.5k to ~2.2k.

| File | Purpose |
|---|---|
| `hxh_ivy_v7/lorebook/HxH_Ivy_v7_Lorebook.json` | 29-entry World Info (4 always-on, 4 disabled POST-REVELATION entries) |
| `hxh_ivy_v7/card/Kurapika_v7.json` | Kurapika card, v2 spec, 3 opening scenes, ensemble-aware |
| `hxh_ivy_v7/persona/Ivy_Persona_v7.txt` | Ivy persona text to paste into the Persona box |
| `hxh_ivy_v7/preset/ST_Claude_Preset_v7.json` | Claude preset — main prompt, jailbreak, author's note, sampler settings |
| `hxh_ivy_v7/preset/JAILBREAK_v7.md` | The same three blocks as copy-paste, plus recommended settings |
| `hxh_ivy_v7/README.md` | **The analysis**: every canon error found, and the full rework of the OC's power |
