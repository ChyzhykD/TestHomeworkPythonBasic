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
        self.words.sort()

    def get(self, prefix):
        # filtered_words = [word for word in self.words if word.startswith(prefix)]
        # return filtered_words[:5]
        filtered_words = []
        for word in self.words:
            if word.startswith(prefix):
                filtered_words.append(word)
            if len(filtered_words) == 5:
                break
        return filtered_words


# Task 3:
class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, new_student):
        self.students.append(new_student)

    def to_json(self):
        student_data = []
        for person in self.students:
            student_data.append(person.info())

        course_data = {
            'course_name': self.course_name,
            'students': student_data
        }

        return json.dumps(course_data)


if __name__ == '__main__':
    student = Student('John', 'Doe')
    assert student.info() == {'first_name': 'John', 'last_name': 'Doe'}

    fruits_storage = Storage()
    assert fruits_storage.get('') == []
    assert fruits_storage.get('apple') == []

    fruits_storage.add('plum')
    fruits_storage.add('apple')
    fruits_storage.add('peach')
    fruits_storage.add('apricot')
    fruits_storage.add('pineapple')

    assert fruits_storage.get('') == ['apple', 'apricot', 'peach', 'pineapple', 'plum']
    assert fruits_storage.get('a') == ['apple', 'apricot']
    assert fruits_storage.get('p') == ['peach', 'pineapple', 'plum']
    assert fruits_storage.get('abc') == []

    fruits_storage.add('pear')

    assert fruits_storage.get('') == ['apple', 'apricot', 'peach', 'pear', 'pineapple']

    python_basic = Course('Python basic')
    python_basic.add_student(Student('Jane', 'Doe'))
    assert json.loads(python_basic.to_json()) == {
        'course_name': 'Python basic',
        'students': [{'first_name': 'Jane', 'last_name': 'Doe'}]
    }

    python_basic.add_student(Student('John', 'Doe'))
    assert json.loads(python_basic.to_json()) == {
        'course_name': 'Python basic',
        'students': [
            {'first_name': 'Jane', 'last_name': 'Doe'},
            {'first_name': 'John', 'last_name': 'Doe'}
        ]
    }
