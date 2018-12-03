class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 87, 98, 88, 95),
    Student("구지연", 87, 98, 88, 95),
    Student("나선주", 87, 98, 88, 95),
    Student("윤아린", 87, 98, 88, 95),
    Student("윤명월", 87, 98, 88, 95),
    Student("김미화", 87, 98, 88, 95),
    Student("김연화", 87, 98, 88, 95),
    Student("박아현", 87, 98, 88, 95),
    Student("서준서", 87, 98, 88, 95)
]

print(students[0].name)
print(students[0].korean)
print(students[0].math)
print(students[0].english)
print(students[0].science)

print("isinstance(sudent, Student): ", isinstance(students[0], Student))