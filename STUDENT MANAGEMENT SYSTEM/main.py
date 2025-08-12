class student:
    def __init__(self, name, rollno, subjects, marks):
        self.name = name
        self.rollno = rollno
        self.subjects = subjects
        self.marks = marks

    def calculate_average(self, marks):
        m = 0
        for i in marks:
            m += i
        return m / len(marks)

    def show_details(self):
        print(f"Name : {self.name}")
        print(f"Roll Number : {self.rollno}")

        for i, name in enumerate(self.subjects):
            print(f"{name} : {self.marks[i]}")

        print(f"Average : {self.calculate_average(self.marks):.2f}")


name = "Atta Ul Mustafa"
roll_number = 11
subjects = ["Math", "English", "Chemistry"]
marks = [92, 83, 67]

s1 = student(name, roll_number, subjects, marks)

s1.show_details()
