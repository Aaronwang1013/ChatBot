class Student:
    
    def __init__(self , firstname , lastname):
        self.firstname = firstname
        self.lastname = lastname
        # self.major = major
    
    def grettings(self):
        return f'Hello I am {self.firstname} {self.lastname}'
    

class CollegeStudent(Student):
    def __init__(self, firstname, lastname,major):
        super().__init__(firstname, lastname)
        self.major = major

class NonCollegeStudent(Student):
    def __init__(self , firstname, lastname , future_job):
        super().__init__(firstname, lastname)
        self.future_job = future_job
    def grow_up(self):
        return f'When I grow up , I want to be '\
            f'a {self.future_job}'
# student_1 = Student()
# student_2 = Student()

# student_1.firstname = 'Eric'
# student_1.lastname = 'Ruby'
# student_1.major = 'CS'

# student_2.firstname = 'Eric'
# student_2.lastname = 'Ruby'
# student_2.major = 'CS'


student1 = CollegeStudent('Eric' , 'Ruby' , 'CS')
student2 = NonCollegeStudent('Aaron' , 'Wang' , 'Software Development at google')
print(student1.major)
print(student1.grettings())


print(student2.grettings())
print(student2.future_job)
print(student2.grow_up())