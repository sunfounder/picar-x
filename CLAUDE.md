# PiCar-X Documentation Repository

## Project Identity

| Field | Value |
|---|---|
| **Product** | SunFounder PiCar-X — AI-driven self-driving robot car for Raspberry Pi |
| **Repository** | `git@github.com:sunfounder/picar-x.git` |
| **Documentation** | Sphinx + ReadTheDocs (`sphinx_rtd_theme`) |
| **Published at** | `https://docs.sunfounder.com/projects/picar-x/<lang>/latest/` |
| **Company** | SunFounder (service@sunfounder.com) |
| **License** | GPL v2 |

This repository contains **only documentation** for the PiCar-X robot car kit. The Python library code (`picar-x`, `robot_hat`, `vilib`) lives in separate repositories. This repo builds a multi-language Sphinx documentation site via ReadTheDocs.

---

## Branch Strategy: Multi-Language Documentation

The `v2.0` branch holds the kit code/examples. **All documentation lives on language-specific branches:**

| Branch | Language | Role |
|---|---|---|
| `docs-v2-en` | English | **SOURCE OF TRUTH** — all new content originates here |
| `docs-v2-de` | German | Translation target |
| `docs-v2-cn` | Chinese (zh-cn) | Translation target |
| `docs-v2-fr` | French | Translation target |
| `docs-v2-es` | Spanish | Translation target |
| `docs-v2-it` | Italian | Translation target |
| `docs-v2-ja` | Japanese | Translation target |
| `v2.0` | English | Kit code/examples (not documentation) |

### Cardinal Rule

> **`docs-v2-en` is the single source of truth.** All new content, structural changes, and configuration updates start on `docs-v2-en` and propagate to the translation branches. Never add new sections or restructure toctrees directly on a translation branch — do it on `docs-v2-en` first, then mirror to others.

### Translation Branch Sync Flow

```
docs-v2-en (write new content)
    │
    ├─→ docs-v2-de  (translate, keep German text)
    ├─→ docs-v2-cn  (translate, keep Chinese text)
    ├─→ docs-v2-fr  (translate, keep French text)
    ├─→ docs-v2-es  (translate, keep Spanish text)
    ├─→ docs-v2-it  (translate, keep Italian text)
    └─→ docs-v2-ja  (translate, keep Japanese text)
```

### What Gets Synced

When propagating from `docs-v2-en` to a translation branch:

1. **Copy as-is**: All image files (`img/`, `ai_interaction/img/`, `python/img/`, `ezblock/img/`, `hardware/img/`, `python_video_course/img/`)
2. **Translate**: All `.rst` content files — descriptive text must be in the target language
3. **Merge carefully**: `index.rst` and `conf.py` — preserve translated UI text while adding new entries
4. **Code blocks**: Keep Python/bash code and file paths as-is (they are language-agnostic)
5. **RST directives**: Keep `.. image::`, `.. code-block::`, `.. note::`, `.. warning::`, `.. important::` structural markup intact
6. **Reference labels**: Keep `.. _ref_label:` and `:ref:`target`` references intact (they are cross-document identifiers, not user-visible text)

### Language-Specific Configuration

Each translation branch's `conf.py` differs in:
- Link text in `rst_epilog` substitutions (e.g., German "OpenAI Plattform" vs English "OpenAI Platform")
- The `language` variable (set to the appropriate locale code when translations exist)

The `index.rst` in each branch has:
- Translated header/intro text
- Translated section descriptions
- Same toctree structure as `docs-v2-en`
- May preserve legacy content unique to that language

---

## Repository Layout

```
picar-x/
├── .readthedocs.yaml          # RTD build config (Sphinx, Python 3.11, Ubuntu 22.04)
├── .gitignore                 # Ignores: .vscode, build/, .claude/, secret files, backups
├── .gitmodules                # Submodule: docs/source/_shared → sf-shared.git (branch docs-de)
├── LICENSE                    # GPL v2
├── README.md                  # Kit overview (buy link, updates, troubleshooting)
├── show                       # License/warranty display script
├── CLAUDE.md                  # This file — AI assistant guidance
└── docs/
    ├── requirements.txt       # Sphinx dependencies
    ├── Makefile / make.bat    # Sphinx build (SOURCEDIR=source, BUILDDIR=build)
    └── source/
        ├── conf.py            # Sphinx config: extensions, theme, JS/CSS, rst_epilog links
        ├── index.rst          # Root toctree — chapters + appendix + hardware + FAQ
        ├── assemble.rst       # Assembly instructions
        ├── adjust_servo.rst   # Servo calibration guide
        ├── appendix.rst       # Appendix (SPI config, remote desktop, file transfer, etc.)
        ├── faq.rst            # Frequently asked questions
        ├── openclaw.rst       # OpenClaw AI agent control tutorial
        ├── _shared/           # Git submodule: shared SunFounder doc assets (sf-shared)
        ├── _templates/        # Sphinx HTML templates (layout.html)
        ├── _static/           # Custom JS/CSS (custom.js, lang.js, video assets)
        ├── img/               # Top-level images (picar-x_v2.png, robot_hat_pic.png, etc.)
        │   ├── openclaw/      # OpenClaw installation screenshots
        │   └── apt_*.png      # OpenAI/LLM API setup screenshots
        ├── python/            # Python programming chapter
        │   ├── play_with_python.rst    # Chapter toctree + intro
        │   ├── install_all_modules.rst # Module installation guide
        │   ├── python_move.rst         # Lesson: basic movement
        │   ├── python_keyboard.rst     # Lesson: keyboard control
        │   ├── python_avoid.rst        # Lesson: obstacle avoidance
        │   ├── python_cliff.rst        # Lesson: cliff detection
        │   ├── python_line_track.rst   # Lesson: line tracking
        │   ├── python_calibrate.rst    # Lesson: speed calibration
        │   ├── py_servo_adjust.rst     # Lesson: servo adjustment
        │   ├── python_computer_vision.rst  # Lesson: computer vision intro
        │   ├── python_stare_at_you.rst     # Lesson: face tracking
        │   ├── python_record.rst       # Lesson: video recording
        │   ├── python_bull_fight.rst   # Lesson: bull fight game
        │   ├── python_video_car.rst    # Lesson: video-controlled car
        │   ├── control_by_app.rst      # Lesson: SunFounder Controller app
        │   └── img/                    # Python chapter screenshots
        ├── ezblock/           # Ezblock (graphical programming) chapter
        │   ├── play_with_ezblock.rst   # Chapter toctree + intro
        │   ├── quick_guide_on_ezblock.rst # Getting started with Ezblock
        │   ├── get_start_app.rst       # Ezblock Studio app setup
        │   ├── ezblock_move.rst        # Lesson: movement
        │   ├── ezblock_*.rst           # Lessons: sound, color, avoid, remote, etc.
        │   └── img/                    # Ezblock chapter screenshots
        ├── python_video_course/  # Python Video Course chapter
        │   ├── python_video_course.rst # Chapter toctree + intro
        │   ├── video_a1_start.rst      # Video: getting started
        │   ├── video_a2_assembly.rst   # Video: assembly
        │   ├── video_a3_calibration.rst # Video: calibration
        │   ├── video_1_move.rst        # Video: basic movement
        │   ├── video_2_keyboard_control.rst  # Video: keyboard control
        │   ├── video_3_tts.rst         # Video: text-to-speech
        │   ├── video_4_ir_avoid.rst    # Video: IR obstacle avoidance
        │   ├── video_5_line_tracking.rst # Video: line tracking
        │   ├── video_6_cliff.rst       # Video: cliff detection
        │   ├── video_7_computer_vision.rst # Video: computer vision
        │   ├── video_8_stares_at_you.rst   # Video: face tracking
        │   ├── video_9_record_video.rst    # Video: recording
        │   ├── video_10_bullfight.rst  # Video: bull fight
        │   ├── video_11_video_car.rst  # Video: video car
        │   ├── video_12_treasure_hunt.rst  # Video: treasure hunt
        │   └── video_12_using_mobile_app.rst # Video: mobile app control
        ├── hardware/          # Hardware reference chapter
        │   ├── cpn_hardware.rst        # Chapter toctree
        │   ├── cpn_robot_hat.rst       # Robot HAT intro
        │   ├── cpn_battery.rst         # Battery guide
        │   ├── cpn_camera.rst          # Camera setup
        │   ├── cpn_ultrasonic.rst      # Ultrasonic sensor
        │   └── img/                    # Hardware photos
        └── ai_interaction/    # AI Interaction chapter (added 2025-10-13)
            ├── ai_interaction.rst      # Chapter toctree + intro
            ├── python_sound_background_music.rst  # Background music + TTS
            ├── python_voice_prompt.rst     # Voice prompt interaction
            ├── python_storytelling_robot.rst # Storytelling robot with TTS
            ├── python_voice_control.rst     # Voice control (speech recognition)
            ├── python_text_vision_talk.rst  # Text + vision multimodal chat
            ├── python_online_llms.rst       # Multi-provider LLM setup
            ├── python_local_chatbot.rst      # Local chatbot (Ollama)
            ├── python_treasure_hunt.rst      # Treasure hunt game with AI
            ├── python_ai_robot.rst           # Full AI voice assistant robot
            └── img/                    # AI chapter screenshots
```

---

## Documentation Conventions

### RST Reference Labels

Cross-document references use Sphinx `:ref:` roles. Each `.rst` file defines a unique label at the top (after the Facebook note). These labels **must remain consistent across all language branches** — they are the linking mechanism.

| Label | File | Content |
|---|---|---|
| `play_python` | `play_with_python.rst` | Python chapter entry point |
| `quick_guide_python` | `play_with_python.rst` | Quick guide section within Python chapter |
| `play_ezblock` | `play_with_ezblock.rst` | Ezblock chapter entry point |
| `play_ai` | (implicit via toctree) | AI chapter entry point |
| `install_all_modules` | `install_all_modules.rst` | Module installation prerequisite |
| `install_ezblock` | `get_start_app.rst` | Ezblock app setup |
| `assembly_instructions` | `assemble.rst` | Assembly guide |
| `py_move` | `python_move.rst` | Basic movement lesson |
| `py_avoid` | `python_avoid.rst` | Obstacle avoidance lesson |
| `py_cliff` | `python_cliff.rst` | Cliff detection lesson |
| `py_line_tracking` | `python_line_track.rst` | Line tracking lesson |
| `py_calibrate` | `python_calibrate.rst` | Speed calibration |
| `py_keyboard_control` | `python_keyboard.rst` | Keyboard control lesson |
| `py_computer_vision` | `python_computer_vision.rst` | Computer vision lesson |
| `py_stare` | `python_stare_at_you.rst` | Face tracking lesson |
| `py_video` | `python_record.rst` | Video recording lesson |
| `py_bull_fight` | `python_bull_fight.rst` | Bull fight game lesson |
| `video_car` | `python_video_car.rst` | Video-controlled car lesson |
| `control_by_app` | `control_by_app.rst` | Controller app lesson |
| `py_tts` | `python_sound_background_music.rst` | TTS / background music |
| `py_online_llm` | `python_online_llms.rst` | Online LLM setup |
| `py_treasure` | `python_treasure_hunt.rst` | Treasure hunt game |
| `ai_voice_assistant_car` | `python_ai_robot.rst` | Full AI voice assistant |
| `picarx_skill` | `openclaw.rst` | OpenClaw PiCar-X skill |
| `install_ezblock` | `get_start_app.rst` | Ezblock Studio installation |
| `ezb_*` | `ezblock_*.rst` | Ezblock lessons (grayscale, minecart, remote_control, etc.) |
| `cpn_*` | `_shared/component/cpn_*.rst` | Hardware component references (from submodule) |

### RST File Boilerplate

Every lesson file starts with a Facebook community note (translated to the target language), followed by the reference label:

```rst
.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 ...
    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_example:

NN. Lesson Title
====================================
```

### Link Substitutions (`rst_epilog` in `conf.py`)

All external links live as RST substitutions in `conf.py` under `rst_epilog`. This centralizes URL management. Pattern:
```python
.. |link_something| raw:: html

    <a href="https://example.com" target="_blank">Link Text</a>
```

When adding a new external link, add the `|link_xxx|` definition to `conf.py` on `docs-v2-en` **first**, then propagate to translation branches (translating only the link text, not the URL).

### Image Paths

- Top-level images: `img/<name>.png` (relative path)
- Chapter-specific: `img/<name>.png` (relative to the chapter's directory)
- OpenClaw images: `img/openclaw/<name>.png`
- Python/Ezblock/Hardware/AI: `img/<name>.png` within their respective directories
- Shared images: via `_shared` submodule

### File Naming

- Python lessons: `python_<topic>.rst` (snake_case)
- Ezblock lessons: `ezblock_<topic>.rst` (snake_case)
- Hardware components: `cpn_<component>.rst` (snake_case)
- AI interaction: `python_<topic>.rst` (shares `python_` prefix — these are Python-code-based AI lessons)
- Video course: `video_<N>_<topic>.rst` (numbered, snake_case)

---

## Submodule: `docs/source/_shared`

Points to `https://github.com/sunfounder/sf-shared.git`. The branch used varies by documentation branch:
- `docs-v2-en` uses the `main` branch of sf-shared
- `docs-v2-de` uses the `docs-de` branch of sf-shared

Contains shared SunFounder documentation assets reused across all product repos:
- `pi_start/` — Raspberry Pi setup guides (OS install, Wi-Fi, power supply)
- `component/` — Hardware component reference pages
- `appendix/` — Shared appendix content (remote desktop, file transfer, etc.)

When checking out this repo, run:

```bash
git submodule update --init --recursive
```

The `.readthedocs.yaml` includes `submodules: include: all` with `recursive: true`.

---

## Build & Preview

### Local Build (Sphinx)

```bash
cd docs
pip install -r requirements.txt
make html          # Output: docs/build/html/index.html
```

On Windows:
```batch
cd docs
make.bat html
```

### ReadTheDocs

Builds automatically on push to any branch. Configuration in `.readthedocs.yaml`:
- OS: Ubuntu 22.04, Python 3.11
- Sphinx config: `docs/source/conf.py`
- Builds all formats (HTML, PDF, ePub)
- Submodules: included recursively

### Published URLs

Each language branch maps to:
```
https://docs.sunfounder.com/projects/picar-x/<lang>/latest/
```
Where `<lang>` corresponds to the branch suffix: `en`, `de`, `zh-cn`, `fr`, `es`, `it`, `ja`.

---

## Common Maintenance Tasks

### Adding a New Lesson / Documentation Page

1. Create the `.rst` file on `docs-v2-en` in the appropriate chapter directory
2. Define a unique `.. _ref_label:` at the top (after the Facebook note)
3. Add the file to the parent chapter's `.. toctree::` directive
4. If new external links are needed, add `|link_xxx|` definitions to `conf.py`
5. Build locally to verify: `cd docs && make html`
6. Commit on `docs-v2-en`
7. Propagate to translation branches (translate text, keep structure/labels/code)

### Syncing Content to a Translation Branch

1. Identify what's new/missing vs `docs-v2-en`:
   ```bash
   git diff docs-v2-en --name-only  # if on translation branch with EN as remote tracking
   ```
2. Copy image assets directly (no translation needed)
3. For each new/missing `.rst` file:
   - Copy the structure and code blocks as-is
   - Translate all descriptive/navigational text to the target language
   - Keep `.. _ref_label:`, `:ref:`, `.. image::`, `.. code-block::` directives unchanged
   - **Critical:** When translating section titles, extend the RST underline (`===`, `---`, `^^^`, `~~~`) to match the new title length. Translated titles are often longer than English, and Sphinx will error with `Title underline too short` if the underline is shorter than the title.
4. For `index.rst`: merge new toctree entries, translate new section descriptions
5. For `conf.py`: add new `|link_xxx|` definitions from EN branch (translate link text only)
6. Build locally to verify no broken references
7. **Review [Common Pitfalls](#common-pitfalls-when-syncing-translation-branches) before and after every sync operation.**

### Updating the toctree Structure

The root toctree is in `index.rst`. Chapter-level toctrees are in:
- `python/play_with_python.rst`
- `ezblock/play_with_ezblock.rst`
- `ai_interaction/ai_interaction.rst`
- `python_video_course/python_video_course.rst`
- `hardware/cpn_hardware.rst`

When reordering or adding entries, ensure the same structure propagates to all language branches.

### Adding Support for a New LLM Provider

1. Add provider section to `python_online_llms.rst` (API key setup + test code)
2. Add any new screenshots to `ai_interaction/img/`
3. Add `|link_newprovider|` to `conf.py` `rst_epilog`
4. If a full interactive example is needed, create a new `python_<feature>.rst` and add it to `ai_interaction/ai_interaction.rst` toctree
5. Propagate to translation branches

### Handling Legacy Content in Translation Branches

Some translation branches may have pages not present in `docs-v2-en`. When syncing:
- **Keep** legacy pages in the toctree if they still provide value to that language's audience
- **Do not** add legacy pages to `docs-v2-en` unless they're being promoted to canonical status
- Legacy pages may need link updates if `conf.py` substitutions change

---

## CJK + RST Inline Markup

When translating documentation into Chinese, Japanese, or Korean (CJK), RST inline markup frequently breaks because the closing delimiter touches a CJK character that RST doesn't recognize as a valid terminator.

**The Rule:** RST inline markup closing delimiters must be followed by **whitespace** or **ASCII punctuation** only. Characters from Unicode blocks outside ASCII — including CJK ideographs and full-width punctuation — are NOT recognized as valid terminators.

**Affected markup types and their Sphinx warnings:**

| Markup | Syntax | Warning when broken |
|---|---|---|
| Strong (bold) | `**text**` | `Inline strong start-string without end-string` |
| Literal (code) | ` ``text`` ` | `Inline literal start-string without end-string` |
| Substitution ref | `\|link_name\|` | `Inline substitution_reference start-string without end-string` |

**Characters that break inline markup** (non-exhaustive):

| Category | Characters | Examples |
|---|---|---|
| CJK ideographs | All Han characters | `中文字符` immediately after `**` or ` `` ` ` |
| Full-width parentheses | `（）` | `**text**（` causes `strong` warning |
| Full-width punctuation | `。，、：；！？` | Usually tolerated, but `（）` and Chinese chars always fail |
| Em-dash | `——` | `**text**——` causes `strong` warning |

**The Fix:** Insert `\ ` (backslash-escaped space) between the closing delimiter and the CJK character:

```rst
# Wrong:
**加粗文本**中文           → WARNING: strong start-string without end-string
``LANGUAGE``变量           → WARNING: literal start-string without end-string
|link_aliyun|（控制台）    → WARNING: substitution_reference start-string without end-string
**OpenAI**（ChatGPT）      → WARNING: strong start-string without end-string

# Correct:
**加粗文本**\ 中文          → escaped space before CJK character
``LANGUAGE``\ 变量          → escaped space before CJK character
|link_aliyun|\ （控制台）   → escaped space before full-width parenthesis
**OpenAI**\ （ChatGPT）     → escaped space before full-width parenthesis
```

**Patterns to check before committing to any CJK branch:**

1. `grep -n '\*\*[^*]+\*\*[（\p{Han}]' docs/source/**/*.rst` — bold + CJK
2. `grep -n '``[^`]+``[（\p{Han}]' docs/source/**/*.rst` — literal + CJK
3. `grep -n '|link_[a-z_]+|[（\p{Han}]' docs/source/**/*.rst` — substitution ref + CJK

**Known-safe patterns** (no fix needed):
- `**text**` followed by whitespace or ASCII `. , : ; ! ? ) ] } /` → always OK
- `**text**。` or `**text**，` — full-width period/comma directly after `**` are **usually tolerated** by docutils, but verify with `make html`

---

## Common Pitfalls When Syncing Translation Branches

These issues were discovered during actual sync operations (EN → JA, EN → DE, EN → FR, etc.). Refer to this section before starting any translation branch sync.

| # | Problem | Symptom | Root Cause | Fix |
|---|---|---|---|---|
| **P1** | UTF-8 encoding corruption | Japanese/Chinese text turns to gibberish (`æ¶ˆæ`, `é`, `ã` etc.) | PowerShell 5.1 `Get-Content -Raw` reads UTF-8 as system encoding (Shift-JIS on JP Windows). `Set-Content` / `[System.IO.File]::WriteAllText` then writes garbled bytes back. | **Never** use PowerShell for CJK file content operations. Use `Edit` / `Write` tools exclusively. Use `git checkout -- <file>` to restore corrupted files. |
| **P2** | Untracked files lost during branch switch | Newly created `.rst` files disappear after `git checkout --force <other-branch>` | Untracked files persist across checkouts *in theory*, but `--force` combined with working tree conflicts or PowerShell file operations can cause loss. | Immediately commit or stash new files before switching branches. Verify with `git status` after returning. |
| **P3** | Line ending corruption | File stops rendering; `Edit` tool fails with "String not found" | `Set-Content` on PowerShell 5.1 writes CR-only (`\r`) line endings. RST/docutils requires LF or CRLF. | Use `Write` tool for new files. For existing files, only use `Edit`. Check with `git diff` after any PowerShell file operation. |
| **P4** | CJK + RST inline markup | `Inline strong/literal/substitution_reference start-string without end-string` | `**bold**` / `` ``literal`` `` / `\|link\|` / `:ref:` followed by CJK character or full-width punctuation (`（）`、`「」`、`。，、`) — RST doesn't recognize these as valid terminators. | Insert `\ ` (backslash-escaped space) between closing delimiter and CJK character. See [CJK + RST Inline Markup](#cjk--rst-inline-markup). |
| **P5** | Section title underline too short | `Title underline too short` | Translated title is longer than English original (e.g., "Poses" → "Postures"), but the RST underline (`===`, `---`, `^^^`) was not extended. **For CJK titles, even slightly exceeding the character count may still trigger the warning** — Sphinx/docutils appears to use display-width or byte-length calculations for CJK characters rather than Unicode code-point count (`len()`). | For Latin-alphabet languages: extend the underline to at least match the character count. **For CJK (JA/ZH): make the underline clearly longer than the title** — add 4–8 extra `=` signs beyond the character count. Discovered in the JA branch where `7. ブルファイト` (9 chars, underline 14 `=`) and `11. 新しいステップの記録` (14 chars, underline 22 `=`) both triggered warnings despite the underline being numerically longer. |
| **P6** | Duplicate `\|link\|` definition | Sphinx warning about duplicate substitution | A `\|link_xxx\|` defined both inline in a `.rst` file and globally in `conf.py` `rst_epilog`. The inline definition is a copy-paste artifact from the English version. | Remove the inline `.. \|link_xxx\| raw:: html` block from the `.rst` file — rely on `conf.py`'s global definition. |
| **P7** | New `.rst` file not in toctree | `document isn't included in any toctree` | File was created on disk but not added to the parent chapter's `.. toctree::` directive. | After creating a new lesson file, verify it appears in the chapter's toctree (e.g., `play_with_python.rst` for Python lessons, `ai_interaction.rst` for AI lessons). |
| **P8** | Existing files have outdated code/commands | Script names, git branches, file paths differ from EN branch | The initial sync only added *new* files but **did not propagate content updates to pre-existing files**. The EN branch had accumulated fixes (numbered script names, updated install commands, corrected paths) that were never merged into translation branches. | Before declaring sync complete, run `git diff docs-v2-en <branch> -- docs/source/` and review all files. Pay special attention to: `.. code-block::` content, `sudo python3` commands, `git clone` commands, and file paths. |
| **P9** | New file missing from toctree in all branches | toctree warning in all translation branches | File was created during initial sync but toctree entry was never added to the parent chapter's `.. toctree::` in any branch. | After creating any new lesson file, check `git grep "<filename>" <branch> -- docs/source/` to confirm it appears in a toctree. |
| **P10** | Lesson number prefixes lost during translation | Lesson titles render without the number prefix (e.g., "Hindernisvermeidung" instead of "4. Hindernisvermeidung") | When translating numbered lesson titles from EN (e.g., "4. Obstacle Avoidance"), the `NN. ` prefix gets dropped, leaving only the translated text. | After translating lesson titles, verify the `NN. ` prefix is preserved. Compare with `docs-v2-en` to confirm all numbered titles stay numbered. This applies to both `python/` and `ezblock/` lesson files. |
| **P11** | Untranslated page titles | Page body text is in the target language but the title remains in English (e.g., "Play with Python" instead of "Mit Python programmieren") | The translator translated the body content but overlooked the title line. The title is the most visible text on the page and must be translated. | When syncing a translation branch, explicitly check every `.rst` file's first section title (the underlined heading after the reference label) against the target language. Titles like "Play with Python", "Install All the Modules", "Assemble the PiCar-X" are user-facing and must be translated. Tip: use `index.rst` as a reference — if the index mentions a chapter in the target language, use that phrasing for the page title. |

---

## Notes for AI Assistants

When working on this repository:

1. **Always identify the current branch first.** If it's not `docs-v2-en`, ask whether the change should start on `docs-v2-en` instead.
2. **The Facebook community note** at the top of every `.rst` file must be translated to the target language — use the existing translation from `index.rst` on that branch as a template.
3. **`conf.py` link substitutions** are the single source of external URLs. Never hardcode external links in `.rst` files — use `|link_xxx|` substitutions.
4. **Reference labels** (`.. _label:`) are code identifiers, not human-readable text. Never translate them.
5. **RST section underlines must match title length.** When translating section titles, the underline characters (`=`, `-`, `^`, `~`) must be at least as long as the title text above them. Translated titles are often longer — always count and extend the underline accordingly. **For CJK titles (JA/ZH), Sphinx/docutils may use display-width rather than `len()` — make the underline clearly longer than the character count** (add 4–8 extra chars). See [P5](#common-pitfalls-when-syncing-translation-branches).
6. **RST inline markup must be separated from CJK characters.** RST inline markup (`**bold**`, ` ``literal`` `, `|link_substitution|`) requires the closing delimiter to be followed by whitespace or **ASCII** punctuation. Chinese/Japanese/Korean characters and full-width punctuation (`（）「」『』。，、：；！？`) do NOT qualify. When any of these follow inline markup, insert an escaped space `\ ` between the closing delimiter and the CJK character. See [CJK + RST Inline Markup](#cjk--rst-inline-markup) for the full reference.
7. **Code blocks** (Python, bash) are never translated. Comments within code blocks may be translated if they are user-facing, but variable names, function names, and command strings stay as-is.
8. **The `_shared` submodule** should not be modified directly — changes to shared assets go through the `sf-shared` repo.
9. **`.gitignore` already excludes** `.vscode`, `build*`, `.claude/`, `secret*` files, and `backups/` — do not commit these.
10. **Build output** goes to `docs/build/` and is gitignored — never commit build artifacts.
11. **When in doubt about language coverage**, check all `docs-v2-*` branches to understand what's been translated and what's lagging.
12. **The `show` script** at the repo root is a license/warranty display utility — it's not part of the documentation build.
13. **Lesson number prefixes must survive translation.** The EN source uses numbered lesson titles (e.g., "4. Obstacle Avoidance"). When translating to other languages, the `NN. ` prefix must be preserved on the translated title (e.g., "4. Hindernisvermeidung"). Check every lesson file in `python/` and `ezblock/` to ensure numbering matches `docs-v2-en`. See [P10](#common-pitfalls-when-syncing-translation-branches).
14. **Every user-facing title must be translated.** Don't assume the title was already translated just because the body text is in the target language. Titles like "Play with Python", "Assemble the PiCar-X", "Install All the Modules" are prominently displayed to users — verify each one is in the target language. See [P11](#common-pitfalls-when-syncing-translation-branches).
15. **PiCar-X is a self-driving car, not a quadruped robot.** When writing documentation, use car-appropriate terminology: "drive", "steer", "lane", "parking" — not "walk", "crawl", or "pose".
16. **After any translation or sync work, run `make html` as the definitive check.** The Sphinx build catches all issues that manual review misses: title underline mismatches (P5), duplicate substitutions (P6), missing toctree entries (P7, P9), broken references, and malformed RST. After any file modifications:

   .. code-block:: bash

      cd docs
      pip install -r requirements.txt   # ensure correct theme version
      make html 2>&1 | grep -E "WARNING|ERROR" | grep -v "_shared"

   ``grep -v "_shared"`` filters out noise from the shared submodule (content not used by this project). If the command produces any output besides unsupported theme options, fix every issue and rebuild until clean. **A task that modifies `.rst` files is not complete until `make html` passes with zero relevant warnings.**
