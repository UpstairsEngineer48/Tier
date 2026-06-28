from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

console = Console()


def _progress_bar(done, goal, length=20):
    """
    Returns a simple progress bar.
    """

    done = min(done, goal)

    filled = int((done / goal) * length)

    return "█" * filled + "░" * (length - filled)


def draw_dashboard(stats):
    """
    Draw the Reminder dashboard.
    """

    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]Reminder Dashboard[/bold cyan]",
            border_style="cyan",
        )
    )

    table = Table(
        show_header=True,
        header_style="bold cyan",
    )

    table.add_column("Platform")
    table.add_column("Goal", justify="center")
    table.add_column("Done", justify="center")
    table.add_column("Remaining", justify="center")

    cf = stats["codeforces"]
    lc = stats["leetcode"]

    table.add_row(
        "Codeforces",
        str(cf["goal"]),
        str(cf["done"]),
        str(cf["remaining"]),
    )

    table.add_row(
        "LeetCode",
        str(lc["goal"]),
        str(lc["done"]),
        str(lc["remaining"]),
    )

    console.print(table)

    console.print()

    console.print("[bold cyan]Codeforces[/bold cyan]")

    console.print(
        f"[cyan]{_progress_bar(cf['done'], cf['goal'])}[/cyan] "
        f"{min(cf['done'], cf['goal'])}/{cf['goal']}"
    )

    console.print()

    console.print("[bold yellow]LeetCode[/bold yellow]")

    console.print(
        f"[yellow]{_progress_bar(lc['done'], lc['goal'])}[/yellow] "
        f"{min(lc['done'], lc['goal'])}/{lc['goal']}"
    )

    console.print()

    console.print(
        Text(
            f"Remaining Today : {stats['total_remaining']}",
            style="bold",
        )
    )