from ..base_flow import BaseFlow
import pyautogui

class ClickMouse(BaseFlow):
    def __init__(self, rightClick=False, subactions=None):
        super().__init__("Moving mouse", subactions)
        
        self.isRightClick = rightClick
        
    def perform(self):
        print(f"moving mouse from {self.x} to {self.y}")
        self.click()
        
    def click(self):
        if self.isRightClick:
            pyautogui.click(button='right')
        else:
            pyautogui.click()
    
    