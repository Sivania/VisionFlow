import json

class BaseFlow:
    def __init__(self, name, subactions=None):
        self.name = name
        self.subactions = subactions or []
    
    def perform(self):
        self.printAction()
        for subaction in self.subactions:
            subaction.perform()
    
    def getName(self):
        return self.name
    
    def printAction(self):
        print(f"Performing action: {self.name}")
        
    def serializeJson(self):
        return json.dumps(self)