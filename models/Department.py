class Department:
    def __init__(self, id, name, dean_id=None):
        self.id = id
        self.name = name
        self.dean_id = dean_id

    def __str__(self):
        return f"Department(id={self.id}, name='{self.name}', dean_id={self.dean_id})"
    