from ..base_action import BaseAction
import pyautogui

class ReleaseMouse(BaseAction):
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