class Settings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            cls._instance.window_title = "VisionTaskFlow"
            cls._instance.window_width = 800
            cls._instance.window_height = 600
            
            cls._instance.shape_inital_width = 600
            cls._instance.shape_inital_heigth = 600
            
        return cls._instance