import json
import pyautogui
import time
import random

from actions.base_flow import BaseFlow

class MoveMouse(BaseFlow):
    def __init__(self, x, y, subactions=None):
        super().__init__(f"moving mouse from {x} to {y}", subactions)

        self.x = x
        self.y = y

    def perform(self):
        self.printAction()
        self.human_like_mouse_move()

    def serializeJson(self):
        action_data = {
            'type': self.__class__.__name__,
            'x': self.x,
            'y': self.y
        }
        return json.dumps(action_data)
    
    def human_like_mouse_move(self, steps=10, shake=0.5, duration=1):
        # Get the current mouse position
        start_x, start_y = pyautogui.position()
        
        # Calculate the distance to travel
        distance_x = self.x - start_x
        distance_y = self.y - start_y
        
        # Break the movement into smaller steps
        steps = duration * steps  # More steps for a smoother movement
        for i in range(steps):
            step_x = start_x + (distance_x * i) / steps
            step_y = start_y + (distance_y * i) / steps
            
            # Add some randomness to the path
            step_x += random.uniform(-shake, shake)
            step_y += random.uniform(-shake, shake)
            
            # Move the mouse to the next position
            pyautogui.moveTo(step_x, step_y, duration=0.1)
            
            # Pause briefly at this step to control the speed of the mouse
            time.sleep(duration / steps)