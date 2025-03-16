class Subject:
    def __init__(self, 
                id=None, 
                name=None, 
                numberOfLessons=None):
        self.id = id
        self.name = name
        self.numberOfLessons = numberOfLessons

    def __str__(self):
        return f"Subject(id={self.id}, name='{self.name}', numberOfLessons={self.numberOfLessons})"
