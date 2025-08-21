import json

# ---------------------  Student class ----------------------------------
class Student:
    def __init__(self, name, age, roll_no, marks):
        self.name = name
        self.age = age
        self.roll_no = roll_no
        self.marks = marks

    def display_details(self):
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Roll No. = {self.roll_no}")
        print(f"Marks = {self.marks}")

    def __str__(self):
        return f"Student({self.name}, Roll No: {self.roll_no})"

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "roll_no": self.roll_no,
            "marks": self.marks
        }

    @staticmethod
    def from_dict(data):
        return Student(data["name"], data["age"], data["roll_no"], data["marks"])


# --------------------- Student Manager Class ----------------------------
class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.Students = []
        self.load_students()

    def save_students(self):
        with open(self.filename, "w") as f:
            json.dump([s.to_dict() for s in self.Students], f, indent=4)

    def load_students(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.Students = [Student.from_dict(s) for s in data]
        except FileNotFoundError:
            self.Students = []

    def add(self, student):
        self.Students.append(student)
        self.save_students()   # ✅ save immediately
        print(f"{student} added successfully!")

    def display_all(self):
        if not self.Students:
            print("No Students available.")
        else:
            print("\nAll Students:\n")
            for s in self.Students:
                s.display_details()
                print("-" * 20)

    def search_student(self, roll_no):
        for student in self.Students:
            if student.roll_no == roll_no:
                print(f"✅ Student found (Roll No: {roll_no})")
                student.display_details()
                return student
        print(f"❌ Student with Roll no {roll_no} NOT FOUND")
        return None

    def update_student(self, roll_no, name=None, age=None, marks=None):
        student = self.search_student(roll_no)
        if student:
            if name:
                student.name = name
            if age:
                student.age = age
            if marks:
                student.marks = marks
            self.save_students()   # ✅ save after update
            print(f"✏️ {student} UPDATED successfully!")
        else:
            print(f"❌ UPDATE failed: No student with roll no {roll_no}.")

    def delete_student(self, roll_no):
        student = self.search_student(roll_no)
        if student:
            self.Students.remove(student)
            self.save_students()   # ✅ save after delete
            print(f"🗑️ Student (Roll No {roll_no}) DELETED successfully!")
        else:
            print(f"❌ DELETE FAILED: No student with Roll No {roll_no}.")


# --------------------- Menu System ----------------------------
def menu():
    manager = StudentManager()

    while True:
        print("\n======= Student Manager =======")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            roll_no = int(input("Enter roll no.: "))
            marks = int(input("Enter marks: "))
            student = Student(name, age, roll_no, marks)
            manager.add(student)

        elif choice == "2":
            manager.display_all()

        elif choice == "3":
            roll_no = int(input("Enter roll no. to search: "))
            manager.search_student(roll_no)

        elif choice == "4":
            roll_no = int(input("Enter roll no. to update: "))
            name = input("Enter new name (or press ENTER to skip): ")
            age_input = input("Enter new age (or press ENTER to skip): ")
            marks_input = input("Enter new marks (or press ENTER to skip): ")

            age = int(age_input) if age_input else None
            marks = int(marks_input) if marks_input else None

            manager.update_student(
                roll_no,
                name if name else None,
                age,
                marks,
            )

        elif choice == "5":
            roll_no = int(input("Enter roll no. to DELETE: "))
            manager.delete_student(roll_no)

        elif choice == "6":
            print("👋 Exiting Student Manager. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Try again.")

from students import StudentManager, Student

manager = StudentManager()
s1 = Student("Ujjwal Kumar", 20, 101, 89)
if __name__ == "__main__":
    menu()