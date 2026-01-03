from student import Student


class StudentList:
    def __init__(self):
        self.students = []

    def position(self, name: str) -> int:
        for i, student in enumerate(self.students):
            if name < student.name:
                return i
        return len(self.students)
# -------------------------------------------------------------------

    def add(self, name: str, phone: str, email: str, group: str):
        new_student = Student(name, phone, email, group)
        insert_position = self.position(name)
        self.students.insert(insert_position, new_student)
        print("New element has been added")
# -------------------------------------------------------------------

    def delete(self, name: str) -> bool:
        for i, student in enumerate(self.students):
            if student.name == name:
                del self.students[i]
                print(f"Student '{name}' has been deleted")
                return True
        print(f"Element with name '{name}' was not found")
        return False
# -------------------------------------------------------------------

    def update(self, old_name: str, new_name: str, new_phone: str, new_email: str, new_group: str) -> bool:
        for i, student in enumerate(self.students):
            if student.name == old_name:
                del self.students[i]

                updated_student = Student(
                    new_name, new_phone, new_email, new_group)
                insert_position = self.position(new_name)
                self.students.insert(insert_position, updated_student)
                print("Element updated")

        print("Element was not found")
        return
# -------------------------------------------------------------------

    def print_all_list(self):
        for student in self.students:
            print(student)