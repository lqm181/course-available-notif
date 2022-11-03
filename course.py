class Course:
    def __init__(self, term, year, college, dept, course_num, section="") -> None:
        self.term = term
        self.year = year
        self.college = college
        self.dept = dept
        self.course_num = course_num
        self.section = section
        self.open_seats = 0

    def set_term(self, term):
        self.term = term

    def set_term(self, year):
        self.year = year

    def set_college(self, college):
        self.college = college

    def set_dept(self, dept):
        self.dept = dept

    def set_course_num(self, course_num):
        self.course_num = course_num

    def set_section(self, section):
        self.section = section

    def set_open_seats(self, num):
        self.open_seats = num

    def get_sem(self):
        return self.term + " " + self.year

    def has_open_seats(self):
        return self.open_seats > 0

    def __str__(self) -> str:
        return self.term + " " + self.year + " " + self.college + " " + self.dept + " " + self.course_num
