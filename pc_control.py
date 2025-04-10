import os
import subprocess
import shutil

class PCControl:
    def __init__(self):
        self.programs = {
            "блокнот": "notepad",
            "калькулятор": "calc",
            "браузер": r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Edge.lnk",
            "steam": r"C:\Program Files (x86)\Steam\steam.exe",  # Укажите путь к Steam
            "диспетчер" : "taskmgr",
            "проводник": "explorer",
            "параметры": "ms-settings:",
            "командная строка": "cmd",
            "торрент": r"C:\Users\Никита\Desktop\µTorrent.lnk"
        }

    def launch_program(self, program_name):
        # Проверяем, есть ли программа в словаре
        command = self.programs.get(program_name.lower())
        if command:
            # Проверяем, существует ли указанный путь или это команда
            if os.path.exists(command) or shutil.which(command):
                try:
                    subprocess.Popen(command, shell=True)
                    return True
                except Exception as e:
                    print(f"Ошибка запуска программы '{program_name}': {e}")
                    return False
            else:
                print(f"Путь к программе '{program_name}' не существует.")
                return False

        # Если программа не найдена в словаре, выводим сообщение
        print(f"Программа '{program_name}' не найдена. Укажите полный путь в словаре.")
        return False

    def shutdown(self):
        try:
            os.system("shutdown /s /t 1")
        except Exception as e:
            print(f"Ошибка выключения компьютера: {e}")

if __name__ == "__main__":
    pc_control = PCControl()
    print("Тест запуска программ:")
    try:
        pc_control.launch_program("блокнот")  # Попробуйте запустить блокнот
    except Exception as e:
        print(f"Ошибка в PCControl: {e}")
