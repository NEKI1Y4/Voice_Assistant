import os
import shutil

def check_program_in_path(program_name):
    program_path = shutil.which(program_name)
    if program_path:
        print(f"Программа '{program_name}' найдена: {program_path}")
    else:
        print(f"Программа '{program_name}' не найдена в PATH.")

def list_path_directories():
    path_dirs = os.environ.get("PATH", "").split(os.pathsep)
    print("Директории в PATH:")
    for directory in path_dirs:
        print(directory)

if __name__ == "__main__":
    # Проверить конкретную программу
    check_program_in_path("notepad")  # Замените "notepad" на нужное имя программы

    # Вывести все директории PATH
    list_path_directories()
