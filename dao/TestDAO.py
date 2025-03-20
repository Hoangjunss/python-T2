from dao import StudentDAO, AttendancesDAO, ClassDAO, DepartmentDAO, ScheduleDAO, ScheduleDetailDAO, SemesterDAO, TeacherDAO

from models.Students import Student

student = Student(
    id=4,
    fullname="John Doe",
    gender="Male",
    status="Active",
    dateOfBirth="1990-01-01",
    academicYear="2020-2021",
    address="123 Main St, City, State, ZIP",
    ethnicity="Caucasian",
    religion="Christian",
    nationality="American",
    departmentId=1,
    class_id=1
)

StudentDAO.save(student)

print("student saved successfully")

