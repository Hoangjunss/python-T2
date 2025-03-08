from database.ConnectDB import Database

class Department:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"Department(id={self.id}, name='{self.name}')"
    
    
