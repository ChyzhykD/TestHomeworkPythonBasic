# Task 1:
class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def info(self):
        return {'first_name': self.first_name, 'last_name': self.last_name}


student1 = Student('Dmytro', 'Chyzhyk')
print(student1.info())
