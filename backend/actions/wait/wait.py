from ..base_flow import BaseFlow
import time

class Wait(BaseFlow):
    def __init__(self, milliseconds, subactions=None):
        super().__init__(f"Waiting {milliseconds/1000} seconds", subactions)
        
        self.milliseconds = milliseconds
        
    def perform(self):
        self.printAction()
        self.wait()
        
    def wait(self):
        time.sleep(self.milliseconds/1000)