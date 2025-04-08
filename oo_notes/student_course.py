# OO Python script for managing students, and courses they are enrolled in
class Student(object):
    def __init__(self, name, major):
        self.name = name
        self.major = major
        self.courses = []
    def __repr__(self):
        return f'Student name: {self.name}, Major:{self.major}'
    @property
    def courseLoad(self):
        return [course.courseTitle for course in self.courses]

class Course(object):
    def __init__(self, title, capacity=2, restriction='CIS'):
        self.title = title
        self.capacity = capacity
        self.restriction = restriction
        self.students = []
    
    def addStudent(self, student):
        if self.capacity > len(self.students) and self.restriction == student.major and student not in self.students:
            self.students.append(student)
            student.courses.append(self)
            
    def removeStudent(self, student):
        if student in self.students:
            self.students.remove(student)
    def classList(self):
        return self.students
    def __repr__(self): # show course title, capacity, and enrollment
        return f'{self.title} Cap: {self.capacity} Enroll: {len(self.students)}'
    @property
    def courseTitle(self):
        return self.title

if __name__ == '__main__':
    courses = []
    students = []
    bijay = Student('Bijay', 'CIS')
    print(bijay)
    ray = Student('Ray', 'BUS')
    lin = Student('Lin', 'CIS')
    parker = Student('Parker', 'BUS')
    zhang = Student('Zhang', 'CIS')
    cis407 = Course('Database', 4, 'CIS')
    cis199 = Course('Intro to MIS', 10, 'BUS')
    cis407.addStudent(bijay)
    print(cis407, cis407.classList())
    cis407.addStudent(parker)
    print(cis407, cis407.classList())
    cis407.addStudent(zhang)
    print(cis407, cis407.classList())
    cis407.addStudent(lin)
    print(cis407, cis407.classList())
    cis407.addStudent(zhang)
    print(cis407, cis407.classList())
    cis548 = Course('ERP', 2, 'CIS')
    cis548.addStudent(bijay)
    print ('bijay course load:', bijay.courseLoad)
    