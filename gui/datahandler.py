class DataHandler:
    def __init__(self):
        pass
    
    def fetchData(self):
        return {"data": ["Rectangle", "Oval", "Circle"]}

    def saveData(self, data):
        print("Saving data:", data)