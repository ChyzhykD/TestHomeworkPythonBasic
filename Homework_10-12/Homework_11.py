import json


class Pagination:
    def __init__(self, data):
        self.data = data
        self.page_size = 3
        self.current_page = 1

    def __iter__(self):
        return self

    def __next__(self):
        start_index = (self.current_page - 1) * self.page_size
        end_index = start_index + self.page_size

        if start_index >= len(self.data):
            raise StopIteration

        page_data = self.data[start_index:end_index]
        self.current_page += 1

        return page_data

    def previous_page(self):
        if self.current_page > 1:
            self.current_page -= 1
        else:
            print("Ви перебуваєте на першій сторінці.")

    def next_page(self):
        start_index = (self.current_page - 1) * self.page_size
        if start_index < len(self.data):
            self.current_page += 1
        else:
            print("Ви перебуваєте на останній сторінці.")


class FileStorage:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}
        return data

    def save_data(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.data, file)


class App:
    def __init__(self, storage):
        self.storage = storage
        self.pagination = None

    def run(self):
        while True:
            choice = self.display_menu()
            if choice == 1:
                self.add_course()
            elif choice == 2:
                self.show_courses()
            elif choice == 3:
                self.exit_program()
                break
            else:
                print('Неправильний вибір. Будь ласка, спробуйте ще раз.')

    def display_menu(self):
        print('Меню:')
        print('1. Додати курс')
        print('2. Показати всі курси')
        print('3. Вийти з програми')
        choice = int(input("Виберіть опцію: "))
        return choice

    def add_course(self):
        course_name = input('Введіть назву курсу: ')
        self.storage.data[course_name] = {}
        print('Курс "{}" був успішно доданий.'.format(course_name))

    def show_courses(self):
        if not self.storage.data:
            print('Жодного курсу не знайдено.')
        else:
            courses = list(self.storage.data.keys())
            self.pagination = Pagination(courses)

            while True:
                page = next(self.pagination)
                print("Сторінка курсів:")
                for course_name in page:
                    print('- {}'.format(course_name))

                command = input("Виберіть сторінку (наступна - N, попередня - P, вийти - Q): ")

                if command == 'N':
                    self.pagination.next_page()
                elif command == 'P':
                    self.pagination.previous_page()
                elif command == 'Q':
                    break
                else:
                    print("Невідома команда.")

    def exit_program(self):
        self.storage.save_data()
        print('Дані було успішно збережено.')


file_path = 'data.json'

storage = FileStorage(file_path)
app = App(storage)
app.run()
