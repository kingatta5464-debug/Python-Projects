class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class teacher(person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary


class student(person):
    def __init__(self, name, age, rollno, marks):
        super().__init__(name, age)
        self.rollno = rollno
        self.marks = marks


class school:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_student(self, student):
        self.students.append(student)

    def display_teachers(self):
        print("Teachers : \n")
        for t in self.teachers:
            print(
                f"Name: {t.name} Age: {t.age} Subject: {t.subject} Salary: {t.salary}"
            )

    def display_students(self):
        print("Students : \n")
        for t in self.students:
            print(
                f"Name: {t.name} Age: {t.age} Roll Number: {t.rollno} Marks: {t.marks}"
            )


sch1 = school("Govt. Girls Higher Secondary School Bagh.")
t1 = teacher("Rubina", 25, "Urdu", 33000)
s1 = student("Atta", 22, 11, 1045)
sch1.add_teacher(t1)
sch1.add_student(s1)

sch1.display_students()
sch1.display_teachers()
