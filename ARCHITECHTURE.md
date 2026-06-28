# Daily Project Architecture Rules

## 1. `config.py`

### Responsibility

Store all configurable values for the project.

### Rules

-   Contains **only constants**.
-   All constants use **UPPER_CASE**.
-   Does not import any project modules.
-   Acts as the single source of truth for configuration.

### Organization

Configuration is grouped into two kinds of sections:

#### Website/Application Sections

Contain credentials or identifiers that may be reused by multiple
modules.

Example: - USER - CODEFORCES - LEETCODE - GITHUB

#### Module Sections

Contain settings specific to one module.

Example: - REMINDER - ANIMATION - UI - APPLICATION

------------------------------------------------------------------------

## 2. `boot.py`

### Responsibility

Coordinate the entire application.

### Rules

-   Contains the application flow only.
-   Starts background threads.
-   Starts, stops and transition animations.
-   Calls modules to fetch data.
-   Calls UI to render data.
-   Does **not** implement business logic.
-   Does **not** implement animation logic.
-   Does **not** render UI directly.

### Dependency Rule

`boot.py` may import: - `config.py` - `modules/*` - `ui/*`

------------------------------------------------------------------------

## 3. `modules/`

### Responsibility

Fetch and process data.

### Rules

-   Never print to the terminal.
-   Never use Rich.
-   Never import UI.
-   Return structured data only.
-   Expose one primary public function.
-   Helper functions should be private (prefixed with `_`).

Example:

``` python
stats = get_daily_stats()
```

------------------------------------------------------------------------

## 4. `ui/`

### Responsibility

Display information.

### Rules

-   Never fetch API data.
-   Never contain business logic.
-   Receive data from `boot.py`.
-   Render only what is provided.
-   Dashboard files should expose one public rendering function.

Example:

``` python
draw_dashboard(stats)
```

### Naming

Dashboard names should describe the data they display.

Examples: - `reminder_dashboard.py` - `github_dashboard.py` -
`weather_dashboard.py`

------------------------------------------------------------------------

## 5. `ui/animation.py`

### Responsibility

Manage terminal animations.

### Rules

-   Implements animation classes.
-   Boot controls when animations start and stop.
-   Animation classes never know about APIs.
-   Animation classes never know about dashboards.

### Interface

Every animation implements:

``` python
start()
update()
finish()
stop()
show_transition()
```

### Selection

Animations are created through:

``` python
animation = get_animation(ANIMATION)
```

The animation type comes from `config.py`.

------------------------------------------------------------------------

## 6. `assets/`

### Responsibility

Store non-code resources.

### Rules

-   Contains no Python logic.
-   Used for reusable resources.

Examples: - ASCII art - Logos - Fonts - Animation assets - Sounds

------------------------------------------------------------------------

# Global Rules

1.  One file = one responsibility.
2.  UI never imports Modules.
3.  Modules never import UI.
4.  `config.py` is the single source of configuration.
5.  `boot.py` is the only application controller.
6.  Communication is one-way:

```{=html}
<!-- -->
```
    config.py
         │
         ▼
    boot.py
     ├── modules/*
     └── ui/*

7.  New features should follow the existing pattern:

```{=html}
<!-- -->
```
    modules/github.py
    ui/github_dashboard.py

8.  Public interfaces should remain stable so implementations can change
    without modifying `boot.py`.
