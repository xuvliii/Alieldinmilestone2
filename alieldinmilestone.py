class student:
    def __init__(self, student_name, student_id, grade=None):
        self.student_name = student_name
        self.student_id = student_id
        self.grade = grade

class undergradstudents(student):
    def __init__(self, student_name, student_id, major, grade=None):
        super().__init__(student_name, student_id, grade)
        self.major = major

    def display_info(self):
        print("undergraduate student")
        print("Alieldin:", self.student_name)
        print("2600052:", self.student_id)
        print("EEE:", self.major)

class gradstudents(student):
    def __init__(self, student_name, student_id, program_title, grade=None):
        super().__init__(student_name, student_id, grade)
        self.program_title = program_title

    def display_info(self):
        print("graduate student")
        print("Alieldin:", self.student_name)
        print("2600052:", self.student_id)
        print("Engineering:", self.program_title)