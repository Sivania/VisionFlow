from ..base_flow import BaseFlow
import pyautogui

class HoldMouse(BaseFlow):
    def __init__(self, rightClick=False, subactions=None):
        super().__init__(f"holding {'left' if not rightClick else ' right'} button", subactions)
        
        self.isRightClick = rightClick
        
    def perform(self):
        self.printAction()
        self.holdMouse()
        
    def holdMouse(self):
        if self.isRightClick:
            pyautogui.mouseDown(button='right')
        else:
            pyautogui.mouseDown()