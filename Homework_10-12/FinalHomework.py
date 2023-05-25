import json


class FileStorage:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = {}

    @staticmethod
    def create_instance(file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}

        storage = FileStorage(file_path)
        storage.data = data
        return storage

    def save(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.data, file)


class App:
    def __init__(self, file_storage):
        self.file_storage = file_storage

    def run(self):
        while True:
            self.print_menu()
            choice = input("Виберіть опцію: ")
            if choice == "1":
                self.add_course()
            elif choice == "2":
                self.show_courses()
            elif choice == "3":
                self.add_students_to_course()
            elif choice == "4":
                self.load_data()
            elif choice == "5":
                self.remove_course()
            elif choice == "6":
                self.remove_student_from_course()
            elif choice == "7":
                self.exit_program()
                break
            else:
                print("Недійсний вибір. Спробуйте ще раз.")

    def print_menu(self):
        print("Меню:")
        print("1. Додати курс")
        print("2. Показати всі курси")
        print("3. Додавати студентів на курс")
        print("4. Завантажити дані з файлу")
        print("5. Видалити курс")
        print("6. Видалити студента з курсу")
        print("7. Вийти з програми")

    def add_course(self):
        course_name = input("Введіть назву курсу: ")
        self.file_storage.data.setdefault('courses', []).append(course_name)
        print("Курс успішно доданий.")

    def show_courses(self):
        courses = self.file_storage.data.get('courses', [])
        if courses:
            print("Список курсів:")
            pagination = Pagination(courses)
            for page in pagination:
                for course in page:
                    print(course)
                print("------")
            print(f"Сторінка {pagination.current_page}/{pagination.get_max_page()}")
        else:
            print("Немає жодного курсу.")

    def add_students_to_course(self):
        course_name = input("Введіть назву курсу: ")
        students = self.file_storage.data.setdefault('students', {})
        students_list = students.setdefault(course_name, [])
        student_name = input("Введіть ім'я та прізвище студента: ")
        students_list.append(student_name)
        print("Студент успішно доданий до курсу.")

    def load_data(self):
        self.file_storage = FileStorage.create_instance(self.file_storage.file_path)
        print("Дані успішно завантажені.")

    def remove_course(self):
        course_name = input("Введіть назву курсу, який потрібно видалити: ")
        courses = self.file_storage.data.get('courses', [])
        if course_name in courses:
            courses.remove(course_name)
            self.file_storage.data['courses'] = courses
            print("Курс успішно видалений.")
        else:
            print("Курс не знайдений.")

    def remove_student_from_course(self):
        course_name = input("Введіть назву курсу: ")
        students = self.file_storage.data.get('students', {})
        if course_name in students:
            students_list = students[course_name]
            if students_list:
                print("Список студентів на курсі:")
                for i, student in enumerate(students_list):
                    print(f"{i+1}. {student}")
                student_index = input("Введіть номер студента для видалення: ")
                try:
                    student_index = int(student_index)
                    if 1 <= student_index <= len(students_list):
                        student = students_list.pop(student_index - 1)
                        print(f"Студент {student} успішно видалений з курсу.")
                    else:
                        print("Недійсний номер студента.")
                except ValueError:
                    print("Недійсний номер студента.")
            else:
                print("Немає студентів на цьому курсі.")
        else:
            print("Курс не знайдений.")

    def exit_program(self):
        self.file_storage.save()
        print("Зміни збережено. До побачення!")


class Pagination:
    def __init__(self, data, page_size=3):
        self.data = data
        self.page_size = page_size
        self.current_page = 1

    def __iter__(self):
        self.current_page = 1
        return self

    def __next__(self):
        start_index = (self.current_page - 1) * self.page_size
        end_index = self.current_page * self.page_size
        items = self.data[start_index:end_index]

        if not items:
            raise StopIteration

        self.current_page += 1
        return items

    def go_to_page(self, page_number):
        max_page = self.get_max_page()

        if page_number < 1 or page_number > max_page:
            print("Недійсний номер сторінки.")
        else:
            self.current_page = page_number

    def get_max_page(self):
        return (len(self.data) + self.page_size - 1) // self.page_size


if __name__ == '__main__':
    file_path = input('Enter storage path: ')
    app = App(FileStorage.create_instance(file_path))
    app.run()
