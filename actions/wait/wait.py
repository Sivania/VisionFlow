from ..base_action import BaseAction
import time

class Wait(BaseAction):
    def __init__(self, milliseconds, subactions=None):
        super().__init__(f"Waiting {milliseconds/1000} seconds", subactions)
        
        self.milliseconds = milliseconds
        
    def perform(self):
        self.printAction()
        self.wait()
        
    def wait(self):
        time.sleep(self.milliseconds/1000)