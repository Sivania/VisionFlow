class BaseAction:
    def __init__(self, name, subactions=None):
        self.name = name
        self.subactions = subactions or []
    
    def perform(self):
        print(f"Performing action: {self.name}")
        for subaction in self.subactions:
            subaction.perform()