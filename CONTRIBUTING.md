# Contributing to Dashboard

Thank you for your interest in contributing to Dashboard.

Before contributing, please read `ARCHITECTURE.md`. The project is built around a modular architecture, and preserving that architecture is more important than adding new features.

---

# Development Principles

The following principles guide every contribution:

- One responsibility per file.
- Simplicity over cleverness.
- Prefer extending the project rather than modifying existing functionality.
- Public interfaces should remain stable.
- Minimize unnecessary dependencies.

---

# Project Structure

```text
boot.py
    │
    ├── modules/
    ├── ui/
    └── config.py
```

Each component has a clearly defined responsibility.

## boot.py

Responsibilities:

- Controls the application lifecycle.
- Starts background tasks.
- Controls animations.
- Coordinates modules and UI.

Rules:

- Do not implement business logic.
- Do not implement UI rendering.
- Do not perform API requests directly.

---

## modules/

Modules are responsible for collecting and processing data.

Rules:

- Never import anything from `ui/`.
- Never print to the terminal.
- Never use Rich.
- Return structured data only.
- Keep helper functions private whenever possible.

---

## ui/

UI components are responsible only for rendering.

Rules:

- Never fetch API data.
- Never implement business logic.
- Never import anything from `modules/`.
- Receive all required data through function arguments.

---

## config.py

All configurable values belong in `config.py`.

Examples include:

- Usernames
- Goals
- Theme
- Animation selection
- Application settings

Avoid hardcoding configuration elsewhere.

---

# Adding a New Feature

Whenever possible, implement new functionality as a new module.

Example:

```text
modules/github.py
ui/github_dashboard.py
```

Then integrate the module through `boot.py`.

Avoid modifying unrelated files.

---

# Dependencies

Avoid introducing new third-party libraries unless they provide substantial value.

Prefer:

- Python Standard Library
- Existing project dependencies

If a new dependency is required, explain why it is necessary in the pull request.

---

# Pull Requests

Before submitting a pull request, ensure:

- The project runs successfully through `boot.py`.
- The architecture described in `ARCHITECTURE.md` is preserved.
- Existing functionality continues to work.
- New code follows the project's naming conventions.
- Configuration remains centralized in `config.py`.

---

# Code Style

- Use descriptive names.
- Prefer readability over cleverness.
- Keep functions focused on a single responsibility.
- Remove unused code before submitting.

---

Thank you for helping improve Dashboard.