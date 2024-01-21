from ..base_action import BaseAction
import pyautogui

class MoveMouse(BaseAction):
    def __init__(self, x, y, subactions=None):
        super().__init__("Move mouse", subactions)

        self.x = x
        self.y = y

    def perform(self):
        print(f"moving mouse from {self.x} to {self.y}")
        self.human_like_mouse_move()