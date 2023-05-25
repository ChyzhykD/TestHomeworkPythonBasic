import json


class FileStorage:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = {"courses": [], "students": []}

    def read_data(self):
        try:
            with open(self.file_path, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = {"courses": [], "students": []}

    def write_data(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.data, file)

    @staticmethod
    def create_instance(file_path):
        storage = FileStorage(file_path)
        storage.read_data()
        return storage


class Pagination:
    def __init__(self, data, items_per_page=3):
        self.data = data
        self.items_per_page = items_per_page
        self.current_page = 1

    def get_current_page_data(self):
        start_index = (self.current_page - 1) * self.items_per_page
        end_index = start_index + self.items_per_page
        return self.data[start_index:end_index]

    def next_page(self):
        if self.current_page < self.get_total_pages():
            self.current_page += 1

    def previous_page(self):
        if self.current_page > 1:
            self.current_page -= 1

    def get_total_pages(self):
        return (len(self.data) + self.items_per_page - 1) // self.items_per_page


class App:
    def __init__(self, file_storage):
        self.file_storage = file_storage

    def run(self):
        self.file_storage.read_data()
        while True:
            print("Меню:")
            print("1. Додати курс")
            print("2. Показати всі курси")
            print("3. Вийти з програми")
            choice = input("Введіть номер опції: ")

            if choice == "1":
                course = input("Введіть назву курсу: ")
                self.file_storage.data["courses"].append(course)
                print("Курс додано.")
            elif choice == "2":
                courses = self.file_storage.data["courses"]
                pagination = Pagination(courses)
                while True:
                    current_page_data = pagination.get_current_page_data()
                    if not current_page_data:
                        print("Всі курси показано.")
                        break
                    for course in current_page_data:
                        print(course)
                    print(f"Сторінка {pagination.current_page}/{pagination.get_total_pages()}")
                    option = input("Наступна (n), Попередня (p), Вихід (q): ")
                    if option.lower() == "n":
                        pagination.next_page()
                    elif option.lower() == "p":
                        pagination.previous_page()
                    elif option.lower() == "q":
                        break
                    else:
                        print("Неправильний вибір. Спробуйте ще раз.")
            elif choice == "3":
                self.file_storage.write_data()
                print("Дані збережено. Програма завершує роботу.")
                break
            else:
                print("Неправильний вибір. Спробуйте ще раз.")


file_path = "data.json"

storage = FileStorage.create_instance(file_path)
app = App(storage)
app.run()