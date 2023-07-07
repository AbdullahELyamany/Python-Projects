
"""
 Application To Remember every 25 minutes
"""

import time
import sys
from termcolor import colored
from plyer import notification

def morydoro():
    pomodoro_duration = 1  # in minutes
    break_duration = 0.5  # in minutes

    sessions = 4

    completed_pomodoros = 0  # Keep track of completed pomodoros
    while completed_pomodoros < 4:
        print("Starting a new Morydoro session for {} minutes".format(pomodoro_duration))
        print("You still have {} sessions.".format(sessions))
        for i in range(pomodoro_duration * 60, 0, -1):
            minutes, seconds = divmod(i, 60)
            progress = (pomodoro_duration * 60 - i) / (pomodoro_duration * 60)
            progress_bar = int(progress * 20)
            progress_string = "|" + "=" * progress_bar + " " * (20 - progress_bar) + "|"
            sys.stdout.write("\r" + colored(f"Time left: {minutes:02d}:{seconds:02d} {progress_string}", "yellow"))
            sys.stdout.flush()
            time.sleep(1)
            
        print("\nTime's up! Take a break.")
        completed_pomodoros += 1
        sessions -= 1
        
        notification.notify(
                title="Morydoro",
                message="Time is up!",
                app_name="Morydoro",
                timeout=5
            )

        print("Starting break for {} minutes".format(break_duration))
        for i in range(break_duration * 60, 0, -1):
            minutes, seconds = divmod(i, 60)
            progress = (break_duration * 60 - i) / (break_duration * 60)
            progress_bar = int(progress * 20)
            progress_string = "|" + "=" * progress_bar + " " * (20 - progress_bar) + "|"
            sys.stdout.write("\r" + colored(f"Time left: {minutes:02d}:{seconds:02d} {progress_string}", "green"))
            sys.stdout.flush()
            time.sleep(1)

        print("\n Break Ended.")
        notification.notify(
                title="Morydoro",
                message="Break Ended!",
                app_name="Morydoro",
                timeout=5
            )
            

    print("\n You Finished it Ya broooo!!! .")
    notification.notify(
                title="Morydoro",
                message="Youuu finisheddd!",
                app_name="Morydoro",
                timeout=5
            )


morydoro()