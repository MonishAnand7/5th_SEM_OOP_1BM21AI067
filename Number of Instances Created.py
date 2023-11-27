class Student:
    instance_count = 0

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

        Student.instance_count += 1

    def display_info(self):
        print(f"Student Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

    @classmethod
    def get_instance_count(cls):
        return cls.instance_count


def main():
    num_students = int(input("Enter the number of students: "))

    students = []

    for _ in range(num_students):
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        grade = float(input("Enter student grade: "))

        student = Student(name, age, grade)

        students.append(student)

    for student in students:
        student.display_info()

    print(f"Total number of instances created: {Student.get_instance_count()}")


if __name__ == "__main__":
    main()
