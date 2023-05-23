class FileStorage:
    def __init__(self, storage_path):
        self.storage_path = storage_path
        self.data = []

        if storage_path and self._file_exists():
            self._load_data()

    def _file_exists(self):
        try:
            with open(self.storage_path, 'r') as file:
                return True
        except FileNotFoundError:
            return False

    def _load_data(self):
        with open(self.storage_path, 'r') as file:
            self.data = file.readlines()

    def save_data(self):
        with open(self.storage_path, 'w') as file:
            file.writelines(self.data)


class App:
    def __init__(self, app_storage):
        self.app_storage = app_storage

    def run(self):
        while True:
            self.print_menu()
            choice = input("Виберіть опцію: ")

            if choice == '1':
                self.add_course()
            elif choice == '2':
                self.show_courses()
            elif choice == '3':
                self.app_storage.save_data()
                break
            else:
                print("Недійсний вибір. Будь ласка, спробуйте ще раз.")

    def print_menu(self):
        print("Меню:")
        print("1. Додати курс")
        print("2. Показати всі курси")
        print("3. Вийти з програми")

    def add_course(self):
        course_name = input("Введіть назву курсу: ")
        self.app_storage.data.append(course_name)

    def show_courses(self):
        if self.app_storage.data:
            print("Всі курси:")
            for course in self.app_storage.data:
                print(course)
        else:
            print("Немає жодного курсу.")


file_path = "data.txt"  # Шлях до файлу

file_storage = FileStorage(file_path)
app = App(file_storage)
app.run()
