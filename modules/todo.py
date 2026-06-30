from pathlib import Path


TODO_FILE = Path(__file__).parent.parent / "assets" / "todo.txt"


def get_todo_list():
    """
    Returns a list of todo items.

    Empty lines are ignored.
    """

    if not TODO_FILE.exists():
        return []

    with open(TODO_FILE, "r", encoding="utf-8") as file:
        return [
            line.strip()
            for line in file
            if line.strip()
        ]