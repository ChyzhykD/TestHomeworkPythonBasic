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
        total_pages = len(self.data) // self.page_size + 1
        if self.current_page < total_pages:
            self.current_page += 1
        else:
            print("Ви перебуваєте на останній сторінці.")


class FileStorage:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()

    @staticmethod
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
            print('Список всіх курсів:')
            courses = list(self.storage.data.keys())
            pagination = Pagination(courses)

            while True:
                try:
                    page = next(pagination)
                    for course_name in page:
                        print('- {}'.format(course_name))
                    print()

                    command = input("Виберіть сторінку (наступна - 'n', попередня - 'p', вийти - 'q'): ")
                    if command == 'n':
                        pagination.next_page()
                    elif command == 'p':
                        pagination.previous_page()
                    elif command == 'q':
                        return
                    else:
                        print("Невідома команда.")
                except StopIteration:
                    print("Кінець списку курсів.")
                    return

    def exit_program(self):
        self.storage.save_data()
        print('Дані було успішно збережено.')


if __name__ == '__main__':
    file_path = str(input('Enter storage path: '))
    app = App(FileStorage.load_data(file_path))
    app.run()
