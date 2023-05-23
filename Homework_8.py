import json


# Task 1:
class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def info(self):
        return {'first_name': self.first_name, 'last_name': self.last_name}


# Task 2:
class Storage:
    def __init__(self):
        self.words = []

    def add(self, word):
        self.words.append(word)

    def get(self, prefix):
        filtered_words = [word for word in self.words if word.startswith(prefix)]
        sorted_words = sorted(filtered_words)
        return sorted_words[:5]


# Task 3:
class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def to_json(self):
        student_data = []
        for student in self.students:
            student_data.append(student.to_dict())

        course_data = {
            'course_name': self.course_name,
            'students': student_data
        }

        return json.dumps(course_data)
