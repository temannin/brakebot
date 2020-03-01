from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class ContentHandler(FileSystemEventHandler):
    """Logs all the events captured."""

    def on_moved(self, event):
        print(event)

    def on_created(self, event):
        print(event)

    def on_deleted(self, event):
        print(event)

    def on_modified(self, event):
        print(event)
