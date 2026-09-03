# ⚡ Hackatime & VS Code Coding Activity Simulator

A realistic, background-capable Python application that simulates authentic human coding activity within a specified project workspace (`C:\Users\pvoja\Desktop\OJAS\CODING\My_First_Hackatime_Website`).

Instead of writing artificial code, the simulator creates and continuously develops **authentic, production-grade real-world projects** chosen and rotated dynamically:

1. **Modern Calculator (`calculator/`)**:
   - Neumorphic & scientific web calculator with precision arithmetic, floating-point error mitigation, trigonometric functions, powers, and persistent calculation tape history.
2. **Netflix Platform Clone (`netflix-clone/`)**:
   - Streaming service landing page with billboard trailer, horizontal scroll carousels (Trending Now, Top 10, Sci-Fi), card zoom previews, and 4K trailer modal.
3. **Amazon Storefront (`amazon-storefront/`)**:
   - E-commerce marketplace with multi-tier navigation, department search, lightning deal cards, Prime tags, and slide-out shopping cart drawer.
4. **Enterprise SaaS Platform (`saas-platform/`)**:
   - B2B Cloud metrics and revenue telemetry dashboard featuring canvas sparkline charts, KPI cards (MRR, Churn), and secret API key manager modal.
5. **Agile Kanban Board (`kanban-flow/`)**:
   - Interactive sprint task management board with HTML5 drag-and-drop progression (Backlog, To Do, In Progress, Review, Done).
6. **Workspace Hub (`index.html`)**:
   - Developer portfolio index linking all interactive applications.

---

## 🌟 Key Features

1. **Realistic Human Developer Modeling**:
   - **Zero Hackatime References in Code**: Generated code contains only authentic application code, domain-specific utilities, and real engineering comments.
   - **Organic Typing Cadence**: Types out HTML, CSS, JavaScript, and JSON files line-by-line with micro-delays and keystroke jitter.
   - **Plausible Typo Simulation**: Occasionally mistypes a character, pauses for a fraction of a second, backspaces, and corrects it.
   - **Multi-Project Rotation**: Naturally shifts focus between different projects after bursts of coding activity.
   - **Natural Pauses**: Simulates thinking breaks and documentation lookups.

2. **Direct Hackatime / WakaTime Heartbeat Integration**:
   - Automatically synchronizes with `~/.wakatime.cfg` API key and endpoint (`https://hackatime.hackclub.com/api/hackatime/v1`).
   - Dynamically reports the active project name (e.g. `Netflix-Stream-Clone`, `SaaS-Analytics-Platform`, `Modern-Calculator`, `Amazon-Storefront-Clone`) to show rich, diverse coding activity on Hackatime/WakaTime.
   - Guaranteed telemetry detection even when VS Code is minimized or closed.

3. **Dual Execution Modes**:
   - **Interactive Dashboard (TUI)**: Live terminal interface showing real-time session uptime, active file & line, total lines written, and heartbeat sync telemetry.
   - **Silent Background Daemon**: Run completely silently in the background with zero desktop disruption.

---

## 🚀 Quick Start

### Option A: Interactive Mode (with Live Terminal UI)
Double-click `run_interactive.bat` or run:
```bash
python main.py
```

### Option B: Silent Background Mode (Runs in Background)
Double-click `run_background.bat` or run:
```bash
pythonw main.py --headless
```

### Option C: Stop Background Simulation
Double-click `stop_background.bat` or run:
```powershell
.\stop_background.bat
```

---

## ⚙️ Configuration & Customization

You can customize the simulation behavior either via `config.json` or CLI flags:

### Speed Presets (`--speed`):
- `chill`: Slower, relaxed typing with longer thinking pauses (15–45s).
- `normal` *(Default)*: Balanced, realistic developer pace.
- `fast`: High-tempo coding session.
- `turbo`: Ultra-rapid line generation.

### CLI Flag Options:
```bash
python main.py --help
  --target-dir, -t      Path to project directory (default: My_First_Hackatime_Website)
  --project-name, -p    Project name reported to Hackatime
  --speed, -s           Speed profile (chill, normal, fast, turbo)
  --api-key, -k         Custom API Key (defaults to ~/.wakatime.cfg)
  --api-url, -u         Custom API URL (defaults to Hackatime)
  --rate-limit, -r      Heartbeat interval in seconds (default: 30)
  --no-heartbeat        Disable direct API heartbeats (file edits only)
  --headless            Run without terminal UI (log output only)
```

---

## 📁 Project Structure

```
Hackatime Glitch/
├── main.py                # Main application orchestrator
├── code_engine.py         # File synthesis, typing, refactoring, and disk I/O engine
├── heartbeat_client.py    # Hackatime HTTP heartbeat client
├── dashboard.py           # ANSI terminal user interface
├── code_templates.py      # Rich library of realistic web code snippets
├── config.py              # Configuration manager & CLI parser
├── config.json            # Persistent user configuration
├── run_interactive.bat    # 1-Click interactive launcher
├── run_background.bat     # 1-Click silent background launcher
├── stop_background.bat    # 1-Click background process stopper
└── README.md              # Documentation
```
