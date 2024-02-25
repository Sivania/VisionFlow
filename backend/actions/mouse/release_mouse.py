from ..base_flow import BaseFlow
import pyautogui

class ReleaseMouse(BaseFlow):
    def __init__(self, rightClick=False, subactions=None):
        super().__init__(f"releasing {'left' if not rightClick else ' right'} button", subactions)
        
        self.isRightClick = rightClick
        
    def perform(self):
        self.printAction()
        self.releaseMouse()
        
    def releaseMouse(self):
        if self.isRightClick:
            pyautogui.mouseUp(button='right')
        else:
            pyautogui.mouseUp()