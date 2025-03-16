
class Student:
    def __init__(self, 
                 id=None, 
                 fullname=None, 
                 gender=None, 
                 status=None, 
                 dateOfBirth=None, 
                 academicYear=None, 
                 address=None, 
                 ethnicity=None, 
                 religion=None, 
                 nationality=None,
                 departmentId=None,
                 class_id=None):
        self.id = id
        self.fullname = fullname
        self.gender = gender
        self.status = status
        self.dateOfBirth = dateOfBirth
        self.academicYear = academicYear
        self.address = address
        self.ethnicity = ethnicity
        self.religion = religion
        self.nationality = nationality
        self.departmentId = departmentId
        self.class_id = class_id

    def __str__(self):
        return (f"Student(id={self.id}, fullname='{self.fullname}', gender='{self.gender}', "
                f"status='{self.status}', dateOfBirth='{self.dateOfBirth}', academicYear='{self.academicYear}', "
                f"address='{self.address}', ethnicity='{self.ethnicity}', religion='{self.religion}', "
                f"nationality='{self.nationality}', departmentId='{self.departmentId}', classId='{self.class_id})")


