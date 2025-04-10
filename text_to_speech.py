import pyttsx3

class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # Скорость речи
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if "ru" in voice.languages or "Russian" in voice.name:
                self.engine.setProperty('voice', voice.id)
                break

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

if __name__ == "__main__":
    tts = TextToSpeech()
    try:
        tts.speak("Тест синтеза речи. Привет, я Джарвис.")
    except Exception as e:
        print(f"Ошибка в TextToSpeech: {e}")
