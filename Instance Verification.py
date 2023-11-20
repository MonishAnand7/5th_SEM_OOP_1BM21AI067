class Student:
    pass

class Marks:
    pass

student_instance = Student()
marks_instance = Marks()

is_student_instance = isinstance(student_instance, Student)
is_marks_instance = isinstance(marks_instance, Marks)

is_student_subclass = issubclass(Student, object)
is_marks_subclass = issubclass(Marks, object)

print(f"Is 'student_instance' an instance of 'Student' class? {is_student_instance}")
print(f"Is 'marks_instance' an instance of 'Marks' class? {is_marks_instance}")

print(f"Is 'Student' class a subclass of 'object' class? {is_student_subclass}")
print(f"Is 'Marks' class a subclass of 'object' class? {is_marks_subclass}")
