from dao.StudentDAO import StudentDAO
from dao import TeacherDAO
from dao import ClassDAO
from dao import DepartmentDAO
from dao import SemesterDAO
from models.Students import Student
from models.Teacher import Teacher
from models.Class import Class
from models.Department import Department
from models.Semester import Semester
from datetime import date

class TestDAO:
    def __init__(self):
        print("Test class initialized.")
        self.teacher_login()

    def teacher_login(self):
        try:
            teacher = TeacherDAO.get_by_username_and_password("GV001", "1")
            if teacher:
                print("Teacher logged in successfully: ", teacher)
            else:
                print("Teacher not found.")
        except Exception as e:
            print(f"✗ Error in TeacherDAO tests: {str(e)}")
            
    def test_all_daos(self):
        """Run all DAO tests"""
        print("\n=== Testing StudentDAO ===")
        self.test_student_dao()
        
        print("\n=== Testing TeacherDAO ===")
        self.test_teacher_dao()
        
        print("\n=== Testing ClassDAO ===")
        self.test_class_dao()
        
        print("\n=== Testing DepartmentDAO ===")
        self.test_department_dao()
        
        print("\n=== Testing SemesterDAO ===")
        self.test_semester_dao()

    def test_student_dao(self):
        """Test StudentDAO operations"""
        try:
            # Create test student
            test_student = Student(
                id=999,
                fullname="Test Student",
                gender="Nam",
                status="Active",
                dateOfBirth=date(2000, 1, 1),
                academicYear="2024-2025",
                address="Test Address",
                ethnicity="Kinh",
                religion="None",
                nationality="Việt Nam",
                departmentId=1,
                class_id=1
            )

            # Test save
            StudentDAO.save(test_student)
            print("✓ Save student successful")

            # Test get_by_id
            retrieved_student = StudentDAO.get_by_id(999)
            if retrieved_student and retrieved_student.fullname == "Test Student":
                print("✓ Get student by ID successful")

            # Test get_all
            all_students = StudentDAO.get_all()
            if all_students:
                print("✓ Get all students successful")

            # Test get_by_department_id
            dept_students = StudentDAO.get_by_department_id(1)
            if dept_students:
                print("✓ Get students by department successful")

            # Test get_by_class_id
            class_students = StudentDAO.get_by_class_id(1)
            if class_students:
                print("✓ Get students by class successful")

            # Test update
            test_student.fullname = "Updated Test Student"
            StudentDAO.update(test_student)
            updated_student = StudentDAO.get_by_id(999)
            if updated_student and updated_student.fullname == "Updated Test Student":
                print("✓ Update student successful")

            # Test delete
            StudentDAO.delete(999)
            deleted_student = StudentDAO.get_by_id(999)
            if not deleted_student:
                print("✓ Delete student successful")

        except Exception as e:
            print(f"✗ Error in StudentDAO tests: {str(e)}")

    def test_teacher_dao(self):
        """Test TeacherDAO operations"""
        try:
            # Create test teacher
            test_teacher = Teacher(
                id=999,
                fullname="Test Teacher",
                gender="Nam",
                status="Active",
                address="Test Address",
                email="test@example.com",
                phone="0123456789",
                department_id=1,
                username="test_teacher",
                password="test123"
            )

            # Test save
            TeacherDAO.save(test_teacher)
            print("✓ Save teacher successful")

            # Test get_by_id
            retrieved_teacher = TeacherDAO.get_by_id(999)
            if retrieved_teacher and retrieved_teacher.fullname == "Test Teacher":
                print("✓ Get teacher by ID successful")

            # Test get_all
            all_teachers = TeacherDAO.get_all()
            if all_teachers:
                print("✓ Get all teachers successful")

            # Test get_by_username
            username_teacher = TeacherDAO.get_by_username("test_teacher")
            if username_teacher:
                print("✓ Get teacher by username successful")

            # Test get_by_username_and_password
            login_teacher = TeacherDAO.get_by_username_and_password("test_teacher", "test123")
            if login_teacher:
                print("✓ Get teacher by username and password successful")

            # Test update
            test_teacher.fullname = "Updated Test Teacher"
            TeacherDAO.update(test_teacher)
            updated_teacher = TeacherDAO.get_by_id(999)
            if updated_teacher and updated_teacher.fullname == "Updated Test Teacher":
                print("✓ Update teacher successful")

            # Test delete
            TeacherDAO.delete(999)
            deleted_teacher = TeacherDAO.get_by_id(999)
            if not deleted_teacher:
                print("✓ Delete teacher successful")

        except Exception as e:
            print(f"✗ Error in TeacherDAO tests: {str(e)}")

    def test_class_dao(self):
        """Test ClassDAO operations"""
        try:
            # Create test class
            test_class = Class(
                id=999,
                name="Test Class",
                grade_level=10,
                teacher_id=1,
                academic_year="2024-2025",
                room="T101",
                total_student=30,
                description="Test class description"
            )

            # Test save
            ClassDAO.save(test_class)
            print("✓ Save class successful")

            # Test get_by_id
            retrieved_class = ClassDAO.get_by_id(999)
            if retrieved_class and retrieved_class.name == "Test Class":
                print("✓ Get class by ID successful")

            # Test get_all
            all_classes = ClassDAO.get_all()
            if all_classes:
                print("✓ Get all classes successful")

            # Test update
            test_class.name = "Updated Test Class"
            ClassDAO.update(test_class)
            updated_class = ClassDAO.get_by_id(999)
            if updated_class and updated_class.name == "Updated Test Class":
                print("✓ Update class successful")

            # Test delete
            ClassDAO.delete(999)
            deleted_class = ClassDAO.get_by_id(999)
            if not deleted_class:
                print("✓ Delete class successful")

        except Exception as e:
            print(f"✗ Error in ClassDAO tests: {str(e)}")

    def test_department_dao(self):
        """Test DepartmentDAO operations"""
        try:
            # Create test department
            test_department = Department(
                id=999,
                name="Test Department",
                dean_id=1
            )

            # Test save
            DepartmentDAO.save(test_department)
            print("✓ Save department successful")

            # Test get_all
            all_departments = DepartmentDAO.get_all()
            if all_departments:
                print("✓ Get all departments successful")

            # Test count_students_by_department
            student_count = DepartmentDAO.count_students_by_department(1)
            if student_count is not None:
                print("✓ Count students by department successful")

        except Exception as e:
            print(f"✗ Error in DepartmentDAO tests: {str(e)}")

    def test_semester_dao(self):
        """Test SemesterDAO operations"""
        try:
            # Create test semester
            test_semester = Semester(
                id=999,
                name="Test Semester",
                startdate=date(2024, 1, 1),
                enddate=date(2024, 6, 30)
            )

            # Test save
            SemesterDAO.save(test_semester)
            print("✓ Save semester successful")

            # Test get_by_id
            retrieved_semester = SemesterDAO.get_by_id(999)
            if retrieved_semester and retrieved_semester.name == "Test Semester":
                print("✓ Get semester by ID successful")

            # Test get_all
            all_semesters = SemesterDAO.get_all()
            if all_semesters:
                print("✓ Get all semesters successful")

            # Test get_by_department_id
            dept_semesters = SemesterDAO.get_by_department_id(1)
            if dept_semesters:
                print("✓ Get semesters by department successful")

            # Test update
            test_semester.name = "Updated Test Semester"
            SemesterDAO.update(test_semester)
            updated_semester = SemesterDAO.get_by_id(999)
            if updated_semester and updated_semester.name == "Updated Test Semester":
                print("✓ Update semester successful")

            # Test delete
            SemesterDAO.delete(999)
            deleted_semester = SemesterDAO.get_by_id(999)
            if not deleted_semester:
                print("✓ Delete semester successful")

        except Exception as e:
            print(f"✗ Error in SemesterDAO tests: {str(e)}")

if __name__ == "__main__":
    test = TestDAO()

