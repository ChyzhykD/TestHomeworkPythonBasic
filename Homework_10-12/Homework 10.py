import json


class FileStorage:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = {}
        self.load_data()

    def load_data(self):
        try:
            with open(self.file_path, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.save_data()

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
                print("Invalid choice. Please try again.")

    def display_menu(self):
        print("Menu:")
        print("1. Add a course")
        print("2. Show all courses")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        return choice

    def add_course(self):
        course_name = input("Enter the course name: ")
        self.storage.data[course_name] = True
        self.storage.save_data()

    def show_courses(self):
        courses = list(self.storage.data.keys())
        if courses:
            print("Courses:")
            for course in courses:
                print(course)
        else:
            print("No courses found.")

    def exit_program(self):
        self.storage.save_data()
        print("Exiting the program.")


file_path = "data.json"
storage = FileStorage(file_path)
app = App(storage)
app.run()
