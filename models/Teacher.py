class Teacher:
    def __init__(self, 
                id=None, 
                fullname=None, 
                gender=None,
                status=None, 
                address=None, 
                email=None, 
                phone=None, 
                department_id=None):
        self.id = id
        self.fullname = fullname
        self.gender = gender
        self.status = status
        self.address = address
        self.email = email
        self.phone = phone
        self.department_id = department_id

    def __str__(self):
        return (f"Teacher(id={self.id}, fullname='{self.fullname}', gender='{self.gender}', "
                f"status='{self.status}', address='{self.address}', email='{self.email}', "
                f"phone='{self.phone}', department_id='{self.department_id}')")