import time
import os
from abc import ABC, abstractmethod

from rich.console import Console

from config import WELCOME_MESSAGE, THEME

console = Console()


# =====================================================
# BASE CLASS
# =====================================================

class Animation(ABC):
    """
    Base class for all animations.
    """

    def start(self):
        """
        Called once before the animation starts.
        """
        pass

    @abstractmethod
    def update(self):
        """
        Draw exactly one frame.
        """
        pass

    def finish(self):
        """
        Optional finishing animation.
        """
        pass

    def show_transition(self):
        """
        Draw the final static loading screen.
        """
        pass

    def stop(self):
        """
        Called once after the animation ends.
        """
        os.system("cls")


# =====================================================
# PLACEHOLDER ANIMATION
# =====================================================

class PlaceholderAnimation(Animation):

    def __init__(self):

        self.frames = [
            "[          ]",
            "[=         ]",
            "[==        ]",
            "[===       ]",
            "[====      ]",
            "[=====     ]",
            "[======    ]",
            "[=======   ]",
            "[========  ]",
            "[========= ]",
            "[==========]",
        ]

        self.index = 0

    def update(self):

        os.system("cls")

        console.print("\n")
        console.print(f"[bold {THEME}]{WELCOME_MESSAGE}[/bold {THEME}]")
        console.print()

        console.print(self.frames[self.index])

        self.index = (self.index + 1) % len(self.frames)

        
    def finish(self):

        os.system("cls")

        console.print("\n")
        console.print(f"[bold {THEME}]{WELCOME_MESSAGE}[/bold {THEME}]")
        console.print()

        console.print("[==========]")

        time.sleep(0.25)
        
    def show_transition(self):

        os.system("cls")

        console.print()
        console.print(f"[bold {THEME}]{WELCOME_MESSAGE}[/bold {THEME}]")
        console.print()

        console.print("[==========]")
        console.print()
# =====================================================
# MATRIX ANIMATION (Placeholder)
# =====================================================

class MatrixAnimation(Animation):

    def __init__(self):
        self.frame = 0

    def update(self):

        os.system("cls")

        console.print("\n")
        console.print(f"[bold {THEME}]{WELCOME_MESSAGE}[/bold {THEME}]")
        console.print()

        console.print("Matrix animation coming soon...")

        self.frame += 1

        


# =====================================================
# FACTORY
# =====================================================

def get_animation(name: str) -> Animation:
    """
    Returns the requested animation object.
    """

    animations = {
        "placeholder": PlaceholderAnimation,
        "matrix": MatrixAnimation,
    }

    if name not in animations:
        raise ValueError(f"Unknown animation '{name}'.")

    return animations[name]()