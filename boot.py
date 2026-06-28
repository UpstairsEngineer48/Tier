import threading
import time
from config import ANIMATION,WINDOW_TITLE
import os


from modules.reminder import get_daily_stats

from ui.animation import get_animation
from ui.reminder_dashboard import draw_dashboard


# =====================================================
# GLOBALS
# =====================================================

stats = None


# =====================================================
# BACKGROUND WORKER
# =====================================================

def load_data():
    global stats
    stats = get_daily_stats()


# =====================================================
# MAIN
# =====================================================

def main():
    # Treminal name
    os.system(f"title {WINDOW_TITLE}")
    # Create animation
    animation = get_animation(ANIMATION)

    # Start API thread
    worker = threading.Thread(target=load_data)

    worker.start()

    # Start animation
    animation.start()

    # Keep animating until data is ready
    while worker.is_alive():
        animation.update()
        time.sleep(0.08)

    # Ensure thread has finished
    worker.join()

    # Stop animation
    animation.finish()
    animation.stop()
    animation.show_transition()

    
    # Draw dashboard
    draw_dashboard(stats)

    input("\nPress Enter to close...")


# =====================================================
# ENTRY POINT
# =====================================================

if __name__ == "__main__":
    main()