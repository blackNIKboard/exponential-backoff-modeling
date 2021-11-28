import hashlib
import time


class Request:
    def __init__(self, slot):
        self.id = hashlib.md5(str(time.time()).encode('UTF-8')).hexdigest()[:10]
        self.entry_slot = slot
        self.exit_slot = -1

    def exit(self, slot):
        self.exit_slot = slot

        return self

    def get_delay(self):
        return self.exit_slot - self.entry_slot
