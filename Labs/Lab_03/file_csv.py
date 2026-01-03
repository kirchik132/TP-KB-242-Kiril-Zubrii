import csv
from list_student import StudentList


class Filecsv:

    @staticmethod
    def read_data_from_file(student_list: StudentList, inputfile: str):

        with open(inputfile, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                student_list.add(
                    name=row["Studname"],
                    phone=row["Phone"],
                    email=row["Gmail"],
                    group=row["Group"]
                )

    @staticmethod
    def save_data(student_list: StudentList, inputfile: str):

        with open(inputfile, "w", newline="") as file:
            fieldnames = ["Studname", "Phone", "Gmail", "Group"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for student in student_list.students:
                writer.writerow({
                    "Studname": student.name,
                    "Phone": student.phone,
                    "Gmail": student.email,
                    "Group": student.group
                })