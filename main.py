import pyttsx3
import speech_recognition as sr
from datetime import datetime
import requests
import webbrowser
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.engine = pyttsx3.init()
        self.setWindowTitle("Jarvis")
        self.setGeometry(700, 300, 200, 200)

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)


        self.button = QPushButton("Start Jarvis", self)
        self.label = QLabel("Start Jarvis by pressing button")

        self.button.setStyleSheet("""
            color: Black;
            background-color: #E0FFFF;
            font-size: 100%;
            font-family: Arial;                        

            """)

        self.label.setStyleSheet("""
            font-size: 300%;
            font-family: Arial;
            background-color: #E0FFFF;
            color:Black
            """)

        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.button.clicked.connect(self.takecommand)

    def get_weather(self, city):
        api_key = API #Enter your own API
        base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(base_url)
        if response.status_code == 200:
            data = response.json()
            weather = data['weather'][0]['description']
            temperature = data['main']['temp']
            return f"The weather in {city} is {weather} with a temperature of {temperature}°C."
        else:
            return "Sorry, I couldn't fetch the weather details."

    def takecommand(self):
        name = "Jarvis"
        pth = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(pth))
        chrome = webbrowser.get('chrome')
        recognizer = sr.Recognizer()
        while True:
            with sr.Microphone() as source:
                self.label.setText("Listening...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
                try:
                    self.label.setText("Recongnizing...")
                    query = recognizer.recognize_google(audio, language="en-UK")
                    self.label.setText(f"You said: {query}")

                    if "green" in query.lower():
                        self.engine.say("Bye")
                        self.engine.runAndWait()
                        break
                        sys.exit()
                    elif 'tell me weather' in query.lower():
                        city = "Toronto"
                        weather_info = self.get_weather(city)
                        self.engine.say(weather_info)
                        self.engine.runAndWait()
                    elif "what is your name" in query.lower():
                        self.engine.say(f"My name is {name}")
                        self.engine.runAndWait()
                    elif "tell me time" in query.lower():
                        now = datetime.now()
                        current_time = now.strftime("%H:%M:%S")
                        self.engine.say(f"The current time in Toronto is {current_time}.")
                        self.engine.runAndWait()
                    elif "open chrome" in query.lower():
                        self.engine.say("Opening Chrome, one moment please.")
                        self.engine.runAndWait()
                        chrome.open("https://www.google.com")
                    else:
                        self.engine.say("Sorry, I didn't understand that.")
                        self.engine.runAndWait()
                except sr.UnknownValueError:
                    self.engine.say("Sorry, I couldn't understand what you said.")
                    self.engine.runAndWait()
                except sr.RequestError as e:
                    self.engine.say("Could not request results, please check your internet connection.")
                    self.engine.runAndWait()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())