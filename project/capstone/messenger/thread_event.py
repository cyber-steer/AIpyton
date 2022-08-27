import threading


class Thread_Event:
    def __init__(self):
        self.storage_event = threading.Event()
        self.telegram_event = threading.Event()

    def clearAll(self):
        self.storage_event.clear()
        self.telegram_event.clear()
    def setAll(self):
        self.storage_event.set()
        self.telegram_event.set()

    def is_set(self):
        return self.storage_event.is_set() and self.telegram_event.is_set()


    # storage -> capture
    def get_storage(self):
        return self.storage_event
    # telegram -> capture
    def get_telegram(self):
        return self.telegram_event