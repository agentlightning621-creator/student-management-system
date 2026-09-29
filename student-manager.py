students = []

def add_student(name):
    students.append(name)

def show_students():
    for student in students:
        print(student)

add_student("Alex")
add_student("Sam")
add_student("Jordan")

show_students()
