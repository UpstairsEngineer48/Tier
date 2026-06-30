from rich.console import Console

console = Console()


def render(todo_list):
    """
    Display the user's to-do list.
    """

    console.print("\n[bold cyan]To-Do[/bold cyan]")

    if not todo_list:
        console.print("[green]✓ Nothing to do![/green]")
        return

    for task in todo_list:
        console.print(f"□ {task}")