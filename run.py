import os
import subprocess
import time
from time import sleep

from watchdog.events import LoggingEventHandler
from watchdog.observers import Observer

shouldR = False
lastEvent = time.time()


class Event(LoggingEventHandler):
    def dispatch(self, event):
        global lastEvent
        global shouldR
        filename, file_extension = os.path.splitext(event.src_path)

        if file_extension == ".dart":
            if lastEvent < time.time() - 0.2:
                lastEvent = time.time()
                process.stdin.write(b'r\n')
                process.stdin.flush()
                print("Modified!")


event_handler = Event()
observer = Observer()
observer.schedule(event_handler, '.', recursive=True)
observer.start()

process = subprocess.Popen(['flutter', 'run', '-d', 'windows'], shell=True, stdin=subprocess.PIPE)

while True:
    sleep(10)
