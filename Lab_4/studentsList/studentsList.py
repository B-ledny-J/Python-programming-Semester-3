import json

class Student:
    def __init__(self, last_name, first_name, patronymic, birthday, year_of_joining):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.birthday = birthday
        self.year_of_joining = year_of_joining

    def __str__(self):
        return (
            f"{self.last_name} {self.first_name} {self.patronymic}, "
            f"born {self.birthday}, joined {self.year_of_joining}"
        )


class StateFundedStudent(Student):
    def __init__(self, last_name, first_name, patronymic, birthday, year_of_joining, scholarship):
        super().__init__(last_name, first_name, patronymic, birthday, year_of_joining)
        self.scholarship = scholarship

    def __str__(self):
        return f"{super().__str__()}, scholarship: {self.scholarship}"


class Group:
    def __init__(self, group_number, students):
        self.group_number = group_number
        self.students = students

    def __str__(self):
        return f"Group {self.group_number} ({len(self.students)} students)"

    def print_group(self):
        print(f"\nGroup {self.group_number}:")
        for student in self.students:
            print(f"  - {student}")

class Discipline:
    def __init__(self, name, credits, semester):
        self.name = name
        self.credits = credits
        self.semester = semester

    def __str__(self):
        return f"{self.name} ({self.credits} credits, semester {self.semester})"


class Lecturer:
    def __init__(self, last_name, first_name, patronymic, birthday, seniority, disciplines):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.birthday = birthday
        self.seniority = seniority
        self.disciplines = disciplines

    def __str__(self):
        return (
            f"{self.last_name} {self.first_name} {self.patronymic}, "
            f"born {self.birthday}, seniority {self.seniority}"
        )

    def total_subjects(self):
        total_credits = sum(d.credits for d in self.disciplines)
        return self.disciplines, total_credits

def load_groups(filename):
    groups = []
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for group_item in data:
        students_list = []
        for student_item in group_item["students"]:
            if student_item.get("type") == "budget":
                student_obj = StateFundedStudent(
                    student_item["lastName"],
                    student_item["firstName"],
                    student_item["patronymic"],
                    student_item["birthday"],
                    student_item["yearOfJoining"],
                    student_item["scholarship"]
                )
            else:
                student_obj = Student(
                    student_item["lastName"],
                    student_item["firstName"],
                    student_item["patronymic"],
                    student_item["birthday"],
                    student_item["yearOfJoining"]
                )
            students_list.append(student_obj)
        group_obj = Group(group_item["groupNumber"], students_list)
        groups.append(group_obj)
    return groups


def load_disciplines(filename):
    result = []
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for item in data:
        d = Discipline(item["discName"], item["creditsAmount"], item["numberOfSemesters"])
        result.append(d)
    return result


def load_lecturers(filename, disciplines_list):
    result = []
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for item in data:
        lecturer_disciplines = [
            d for d in disciplines_list if d.name in item["disciplines"]
        ]
        l = Lecturer(
            item["lastName"],
            item["firstName"],
            item["patronymic"],
            item["birthday"],
            item["seniority"],
            lecturer_disciplines
        )
        result.append(l)
    return result

def menu(groups, disciplines, lecturers):
    while True:
        print("\n--- MENU ---")
        print("1. Print groups")
        print("2. Print disciplines")
        print("3. Print lecturers")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            for group in groups:
                group.print_group()
        elif choice == "2":
            print("\nDisciplines:")
            for d in disciplines:
                print(f"  - {d}")
        elif choice == "3":
            print("\nLecturers:")
            for lecturer in lecturers:
                print(f"  - {lecturer}")
                subjects, total_credits = lecturer.total_subjects()
                print(f"    Subjects ({total_credits} credits):")
                for s in subjects:
                    print(f"      * {s}")
        elif choice == "0":
            break
        else:
            print("Invalid choice")

groups = load_groups("groups.json")

disciplines = load_disciplines("disciplines.json")
lecturers = load_lecturers("lecturers.json", disciplines)

menu(groups, disciplines, lecturers)