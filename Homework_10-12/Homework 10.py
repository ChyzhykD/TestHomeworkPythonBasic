import json


class App:
    def __init__(self, app_file_storage):
        self.file_storage = app_file_storage

    def run(self):
        while True:
            print("Меню:")
            print("1. Додати курс")
            print("2. Показати всі курси")
            print("3. Вийти з програми")
            choice = input("Введіть номер опції: ")

            if choice == "1":
                course = input("Введіть назву курсу: ")
                self.file_storage.data.append(course)
                print("Курс додано.")
            elif choice == "2":
                print("Список курсів:")
                for course in self.file_storage.data:
                    print(course)
            elif choice == "3":
                self.file_storage.write_data()
                print("Дані збережено. Програма завершує роботу.")
                break
            else:
                print("Неправильний вибір. Спробуйте ще раз.")


file_path = "data.txt"  # Шлях до файлу для збереження даних

file_storage = FileStorage.create_instance(file_path)
app = App(file_storage)
app.run()
