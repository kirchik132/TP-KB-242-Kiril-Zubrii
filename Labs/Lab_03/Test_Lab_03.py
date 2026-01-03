import unittest
from student import Student
from list_student import StudentList


class TestStudentSystem(unittest.TestCase):

    def setUp(self):

        self.student_list_manager = StudentList()

    def test_add_student(self):

        self.student_list_manager.add(
            "Bob",
            "0631234567",
            "damsbob@gmail.com",
            "kb-242"
        )
        added_student = self.student_list_manager.students[0]

        assert len(self.student_list_manager.students) == 1
        assert (added_student.phone) == "0631234567"

    def test_delete_student(self):

        initial_student = Student(
            "Bob",
            "0631234567",
            "damsbob@gmail.com",
            "kb-242"
        )
        self.student_list_manager.students = [initial_student]
        assert len(self.student_list_manager.students) == 1

        result = self.student_list_manager.delete("Bob")
        assert result == True
        assert len(self.student_list_manager.students) == 0


if __name__ == '__main__':
    unittest.main()