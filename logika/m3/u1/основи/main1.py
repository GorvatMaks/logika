class Student():
    def __init__(self, surname, name, grade):
        self.surname = surname
        self.name = name
        self.grade = grade

students=[]

with open("cpusoc.txt", 'r', encoding= 'utf-8') as file:
    for line in file:
        data = line.split(' ')
        #print(data)
        obj = Student(data[0], data[1], int(data[2]))
        students.append(obj)

for student in students:
    if student.grade == 5:
        print(student.surname)

    normal_grades = sum(student.grade for student in students)
    qq_grade = normal_grades/len(students) if students else 0
    print(f"Суредня оцінка: {qq_grade:.2f}")