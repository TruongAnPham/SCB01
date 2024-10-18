class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grades(self, grades):
#Thêm nhiều điểm vào danh sách điểm của học viên.
        self.grades.extend(grades)

    def calculate_average(self):
#Tính điểm trung bình của học viên.
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0


class GradeManager:
    def __init__(self):
        self.students = []

    def add_student(self, name):
#Thêm học viên mới vào danh sách.
        student = Student(name)
        self.students.append(student)

    def find_student(self, name):
#Tìm học viên theo tên.
        for student in self.students:
            if student.name == name:
                return student
        return None

    def record_grades(self, name, grades):
#Ghi nhiều điểm cho học viên.
        student = self.find_student(name)
        if student:
            student.add_grades(grades)
        else:
            print(f"{name} khong tim thay .")

    def calculate_average_all(self):
#Tính điểm trung bình của toàn bộ học viên.
        if self.students:
            total_sum = 0
            total_count = 0

            for student in self.students:
                if student.grades:
                    total_sum += sum(student.grades)
                    total_count += len(student.grades)

            if total_count > 0:
                return total_sum / total_count
            else:
                print("khong co diem.")
        else:
            print("khong co hoc sinh.")
        return None

    def save_data(self, filename):
#Lưu điểm trung bình của học viên vào file.
        with open(filename, "w") as file:
            for student in self.students:
                average = student.calculate_average()
                file.write(f"Hoc sinh: {student.name}, DTB: {average:.2f}\n")
        print(f"Data saved to {filename}")


def menu():
    grade_manager = GradeManager()

    while True:
        print("\nMenu:")
        print("1. Them hoc sinh")
        print("2. Them diem cho hoc sinh")
        print("3. Tinh diem tong")
        print("4. Luu data")
        print("5. Exit")

        choice = input("chon (1-5): ")

        if choice == '1':
            name = input("Luu ten hoc sinh: ")
            grade_manager.add_student(name)

        elif choice == '2':
            name = input("Ten hoc sinh: ")
            try:
                grades_input = input("Tach diem ra = dau ,: ")
                grades = [float(grade.strip()) for grade in grades_input.split(",")]
                grade_manager.record_grades(name, grades)
            except ValueError:
                print("Invalid grade input.")

        elif choice == '3':
            average = grade_manager.calculate_average_all()
            if average is not None:
                print(f"Diem trung binh: {average:.2f}")

        elif choice == '4':
            filename = input("Luu data bang ten?: ")
            grade_manager.save_data(filename)

        elif choice == '5':
            print("Exiting program.")
            break

        else:
            print("khong kha dung.")


if __name__ == "__main__":
    menu()
