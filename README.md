# Tier

A modular terminal dashboard that launches automatically when you log in.

It currently tracks your daily competitive programming progress and displays your personal to-do list, while remaining modular enough to support additional dashboards in the future.

---

## Features

### Current

- Automatic startup on Windows login
- One-command installation (`install.py`)
- Automatic virtual environment creation
- Automatic dependency installation
- Boot animation while data loads
- Codeforces daily progress tracker
- LeetCode daily progress tracker
- Personal To-Do list
- Independent progress bars
- Configurable daily goals
- Modular architecture

### Planned

- GitHub Dashboard
- Multiple boot animations
- Linux installer
- macOS installer
- Plugin system

---

# Project Structure

```text
Tier/
│
├── assets/
│   └── todo.txt
│
├── modules/
│   ├── reminder.py
│   └── todo.py
│
├── ui/
│   ├── animation.py
│   ├── reminder_dashboard.py
│   └── todo_dashboard.py
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
git clone https://github.com/UpstairsEngineer48/Tier.git
cd Tier
```

---

## 2. Configure Tier

Open `config.py` and update:

```python
CODEFORCES_HANDLE = "your_handle"
LEETCODE_USERNAME = "your_username"

CF_GOAL = 2
LC_GOAL = 2
```

You may also customize:

- Name
- Theme
- Welcome message
- Animation
- Timezone

Edit your personal to-do list in:

```text
assets/todo.txt
```

---

## 3. Install Tier

```bash
python install.py
```

The installer automatically:

- Creates a virtual environment
- Installs all required dependencies
- Registers Tier with Windows Task Scheduler

Tier will automatically launch the next time you log in.

---

# Manual Run

To run Tier manually:

```bash
python boot.py
```

---

# Architecture

Tier follows a modular architecture.

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
| `modules/` | Data collection and processing |
| `ui/` | Terminal rendering |
| `assets/` | Static resources |

See **ARCHITECTURE.md** for additional details.

---

# Design Principles

- One responsibility per file
- Modules never import UI
- UI never imports modules
- Configuration belongs only in `config.py`
- New features should be added as modules
- Keep components loosely coupled
- Minimize unnecessary dependencies

---

# Dependencies

- Python 3.11+
- Rich
- Requests

The installer automatically installs all required dependencies.

---

# Contributing

Contributions are welcome.

Please read:

- `ARCHITECTURE.md`
- `CONTRIBUTING.md`

before opening a pull request.

---

# License

This project is licensed under the MIT License.
