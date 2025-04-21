# Simple Jarvis Application without AI

This Python application simulates a basic assistant called "Jarvis" using PyQt6. Jarvis can respond to voice commands, tell its name, provide weather updates for Toronto, report the current time, and open Chrome browser.

## Features
- Voice recognition for commands.
- Responds with text-to-speech.
- Provides the current weather in Toronto.
- Reports the current time.
- Opens Chrome browser upon request.

## Requirements
To run this application, you need:
- Python 3.x
- PyQt6
- pyttsx3 (text-to-speech engine)
- SpeechRecognition (voice command recognition)
- datetime (to fetch the current time)
- requests (to fetch weather information)
- Webbrowser (to open websites)

Install necessary libraries using pip:
```bash
pip install pyttsx3 SpeechRecognition requests PyQt6
