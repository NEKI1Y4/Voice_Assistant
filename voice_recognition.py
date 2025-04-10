import speech_recognition as sr

class VoiceRecognition:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            print("Слушаю...")
            try:
                audio = self.recognizer.listen(source)
                return self.recognizer.recognize_google(audio, language="ru-RU")
            except sr.UnknownValueError:
                print("Не удалось распознать речь.")
            except sr.RequestError as e:
                print(f"Ошибка сервиса распознавания речи: {e}")
        return None

if __name__ == "__main__":
    recognizer = VoiceRecognition()
    try:
        print("Скажите что-нибудь...")
        command = recognizer.listen()
        print(f"Вы сказали: {command}")
    except Exception as e:
        print(f"Ошибка в VoiceRecognition: {e}")
