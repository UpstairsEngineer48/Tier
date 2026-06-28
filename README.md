# Dashboard

A modular terminal dashboard that launches automatically when you log in.

The project follows a modular architecture, making it easy to add new dashboards without changing the application's core.

---

## Features

### Current

- Automatic startup on Windows login
- Automatic installation using a single installer
- Boot animation while background tasks load
- Codeforces daily progress tracker
- LeetCode daily progress tracker
- Independent progress bars for each platform
- Configurable daily goals

### Planned

- GitHub Dashboard
- Multiple boot animations
- Linux installer
- macOS installer


---

# Project Structure

```text
Dashboard/
│
├── assets/
│
├── modules/
│   └── reminder.py
│
├── ui/
│   ├── animation.py
│   └── reminder_dashboard.py
│
├── boot.py
├── config.py
├── install.py
│
├── README.md
├── ARCHITECTURE.md
├── CONTRIBUTING.md
├── LICENSE
├── requirements.txt
└── .gitignore
```

---

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/<your-username>/Dashboard.git
cd Dashboard
```

---

## 2. Configure Dashboard

Open `config.py` and update the following variables:

```python
CODEFORCES_HANDLE = "your_handle"
LEETCODE_USERNAME = "your_username"

CF_GOAL = 2
LC_GOAL = 2
```

You can also customize:

- Name
- Theme
- Welcome message
- Animation
- Timezone

---

## 3. Install Dashboard

```bash
python install.py
```

The installer automatically:

- Creates a Python virtual environment
- Installs all required dependencies
- Registers Dashboard with Windows Task Scheduler

Dashboard will automatically launch the next time you log in.

---

# Manual Run

If you want to test Dashboard without installing it:

```bash
python boot.py
```

---

# Architecture

Dashboard follows a modular architecture.

```
boot.py
        │
        ├── config.py
        ├── modules/
        ├── ui/
        └── assets/
```

Each component has a single responsibility.

| Component | Responsibility |
|-----------|----------------|
| `boot.py` | Application controller |
| `config.py` | Global configuration |
| `modules/` | Fetch and process data |
| `ui/` | Render dashboards |
| `assets/` | Static resources |

More information is available in **ARCHITECTURE.md**.

---

# Design Principles

- One responsibility per file
- Modules never import UI
- UI never imports modules
- Configuration belongs only in `config.py`
- Features should be added as new modules
- Minimize unnecessary dependencies
- Keep components loosely coupled

---

# Dependencies

- Python 3.11+
- Rich
- Requests

The installer automatically installs all dependencies.


---

# Contributing

Contributions are welcome.

Before contributing, please read:

- `ARCHITECTURE.md`
- `CONTRIBUTING.md`

---

# License

This project is licensed under the MIT License.