import time
from plyer import notification
if __name__ == '__main__':
    while True:
        notification.notify(
            title = "All Day Reminder",
            message = "Today I have to submit my assignment",
            timeout = 15
        )
        time.sleep(60*60)
    