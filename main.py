import time
import webbrowser
import pygetwindow as gw
from voice_recognition import VoiceRecognition
from text_to_speech import TextToSpeech
from system_info import SystemInfo
from pc_control import PCControl

def main():
    recognizer = VoiceRecognition()
    tts = TextToSpeech()
    pc_control = PCControl()

    tts.speak("Здравствуйте, я Джарвис. Чем могу помочь?")

    while True:
        print("Ожидание команды...")
        command = recognizer.listen()

        if not command:
            print("Команда не распознана. Попробуйте снова.")
            continue

        command = command.lower().strip()
        print(f"Вы сказали: {command}")

        # Обработка команд
        if "загрузка процессора" in command:
            tts.speak(SystemInfo.get_cpu_usage())
        elif "использование памяти" in command:
            tts.speak(SystemInfo.get_memory_usage())
        elif "использование диска" in command:
            tts.speak(SystemInfo.get_disk_usage())
        elif "запусти" in command:
            program_name = command.replace("запусти", "").strip()
            if pc_control.launch_program(program_name):
                tts.speak(f"Запускаю {program_name}")
            else:
                tts.speak(f"Не удалось найти или запустить программу {program_name}")
        elif "выключи компьютер" in command:
            tts.speak("Выключаю компьютер. До свидания!")
            pc_control.shutdown()
            break
        elif "выход" in command:
            tts.speak("Выход из программы. До свидания!")
            break
        elif "пауза" in command:
            tts.speak("Пауза. Скажите 'продолжить', чтобы продолжить.")
            while True:
                command = recognizer.listen()
                if command and "продолжить" in command.lower():
                    tts.speak("Продолжаю.")
                    break
        elif "я дома" in command:
            tts.speak("Открываю YouTube и сворачиваю все окна.")
            webbrowser.open("https://www.youtube.com/watch?v=tV0rzgqpWXU&list=PLL3Qcp9LCpVpreLTWsW7KN6R78_ZXppuM&index=3")  # Укажите ссылку на нужное видео
            time.sleep(3)  # Даем браузеру время на открытие
            for window in gw.getAllWindows():
                if window.isMinimized:  # Проверяем, уже ли окно свернуто
                    continue
                try:
                    window.minimize()  # Сворачиваем окно
                except Exception as e:
                    print(f"Не удалось свернуть окно: {window.title}. Ошибка: {e}")
        else:
            tts.speak("Извините, я не понял вашу команду. Попробуйте еще раз.")
        

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Ошибка в основном файле: {e}")
