from sys import argv
from list_student import StudentList
from file_csv import Filecsv


def student_input():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    group = input("Group: ")
    return name, phone, email, group


def main():
    student_list_manager = StudentList()

    if len(argv) < 2:
        print("Example: py Labs/Lab_03/Lab_03.py Labs/Lab_03/Lab_03.csv")
        return

    inputfile = argv[1]
    Filecsv.read_data_from_file(student_list_manager, inputfile)
# -------------------------------
    while True:
        chouse = input(
            "Please specify the action [ C create, U update, D delete, P print, X exit ] "
        )
        match chouse.upper():
            case "C":
                name, phone, email, group = student_input()
                student_list_manager.add(name, phone, email, group)
                student_list_manager.print_all_list()
# ----------------------------------------------------------------------
            case "U":
                old_name = input("Please enter name to be updated data: ")
                if not any(s.name == old_name for s in student_list_manager.students):
                    print(f"Element with name '{old_name}' was not found.")
                    continue
                new_name, new_phone, new_email, new_group = student_input()
                student_list_manager.update(
                    old_name, new_name, new_phone, new_email, new_group)
# ----------------------------------------------------------------------
            case "D":
                name_to_delete = input("Please enter name to be deleted: ")
                student_list_manager.delete(name_to_delete)
# ----------------------------------------------------------------------
            case "P":
                student_list_manager.print_all_list()
# ----------------------------------------------------------------------
            case "X":
                print("Saved data and Exit")
                Filecsv.save_data(student_list_manager, inputfile)
                break
            case _:
                print("Erorre!")


if __name__ == "__main__":
    main()