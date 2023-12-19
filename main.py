class Grade:
    def init(self, student_name, id, grades):
        self.name = student_name
        self.id = id
        self.grade = list(grades)

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, items):
        for item in items:
            if item < 0 or item > 100:
                raise ValueError("Grading should be between 0 and 100")
            self._grade = items


student1 = Grade("John", 1011, [50, 1, 20, 100])
print(student1.name, student1.id, student1.grade)