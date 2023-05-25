import unittest
import json
from file_storage import FileStorage, Pagination


class FileStorageTestCase(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_data.json"
        self.storage = FileStorage.create_instance(self.file_path)

    def tearDown(self):
        self.storage = None
        with open(self.file_path, 'w') as file:
            file.write("")

    def test_data_structure(self):
        expected_data = {"courses": [], "students": []}
        self.assertEqual(self.storage.data, expected_data)

    def test_load_courses(self):
        courses = ["Math", "Science", "History"]
        self.storage.data["courses"] = courses
        self.storage.write_data()

        loaded_storage = FileStorage.create_instance(self.file_path)
        self.assertEqual(loaded_storage.data["courses"], courses)


class PaginationTestCase(unittest.TestCase):
    def test_pagination(self):
        data = [1, 2, 3, 4]
        pagination = Pagination(data, items_per_page=3)

        self.assertEqual(pagination.get_current_page_data(), [1, 2, 3])

        pagination.next_page()
        self.assertEqual(pagination.get_current_page_data(), [4])

        pagination.next_page()
        self.assertEqual(pagination.get_current_page_data(), [])

        pagination.previous_page()
        self.assertEqual(pagination.get_current_page_data(), [1, 2, 3])

        pagination.previous_page()
        self.assertEqual(pagination.get_current_page_data(), [1, 2, 3])

        empty_data = []
        empty_pagination = Pagination(empty_data, items_per_page=3)
        self.assertEqual(empty_pagination.get_current_page_data(), [])

        large_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        large_pagination = Pagination(large_data, items_per_page=4)
        self.assertEqual(large_pagination.get_current_page_data(), [1, 2, 3, 4])
        large_pagination.next_page()
        self.assertEqual(large_pagination.get_current_page_data(), [5, 6, 7, 8])
        large_pagination.previous_page()
        self.assertEqual(large_pagination.get_current_page_data(), [1, 2, 3, 4])


class CourseTestCase(unittest.TestCase):
    def setUp(self):
        self.course = Course("Math")

    def test_add_student(self):
        student = Student("John", "Doe")
        self.course.add_student(student)
        self.assertIn(student, self.course.students)

    def test_get_students(self):
        # Перевірка отримання списку студентів курсу
        student1 = Student("John", "Doe")
        student2 = Student("Jane", "Smith")
        self.course.add_student(student1)
        self.course.add_student(student2)

        students = self.course.get_students()
        self.assertEqual(students, [student1, student2])

if __name__ == '__main__':
    unittest.main()
