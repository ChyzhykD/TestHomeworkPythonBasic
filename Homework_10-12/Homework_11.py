import json


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
            for course_name in self.storage.data:
                print('- {}'.format(course_name))

    def exit_program(self):
        self.storage.save_data()
        print('Дані було успішно збережено.')


file_path = 'data.json'  # шлях до файлу збереження даних

storage = FileStorage(file_path)
app = App(storage)
app.run()
