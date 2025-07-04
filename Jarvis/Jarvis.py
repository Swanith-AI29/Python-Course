import os
import pyttsx3
import speech_recognition as sr
import requests
import pyautogui
import subprocess
from googletrans import Translator

# ========== SETUP ==========
DEEPSEEK_API_KEY = "your_deepseek_api_key_here"
LANGUAGE = "en"
# ===========================

engine = pyttsx3.init()
translator = Translator()
recognizer = sr.Recognizer()

def speak(text):
    if LANGUAGE != "en":
        text = translator.translate(text, dest=LANGUAGE).text
    engine.say(text)
    engine.runAndWait()

def listen_command():
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
    try:
        command = recognizer.recognize_google(audio, language=LANGUAGE)
        print(f"🗣️ You said: {command}")
        return command.lower()
    except:
        speak("Sorry, I didn't catch that.")
        return ""

def ask_deepseek(prompt):
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
    }
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}]
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except:
        return "Error: Could not reach DeepSeek."

def control_pc(command):
    if "shutdown" in command:
        speak("Shutting down.")
        os.system("shutdown /s /t 1")

    elif "restart" in command:
        speak("Restarting.")
        os.system("shutdown /r /t 1")

    elif "lock" in command:
        speak("Locking the computer.")
        os.system("rundll32.exe user32.dll,LockWorkStation")

    elif "open" in command:
        app = command.replace("open", "").strip()
        speak(f"Opening {app}")
        try:
            subprocess.Popen(app)
        except:
            pyautogui.press('win')
            pyautogui.typewrite(app)
            pyautogui.press('enter')

    elif "type" in command:
        text = command.replace("type", "").strip()
        pyautogui.typewrite(text)

def run_jarvis():
    speak("Jarvis activated.")
    while True:
        command = listen_command()

        if command == "":
            continue

        if "exit" in command or "stop" in command:
            speak("Goodbye!")
            break

        elif any(x in command for x in ["open", "shutdown", "restart", "lock", "type"]):
            control_pc(command)

        else:
            response = ask_deepseek(command)
            print("Jarvis:", response)
            speak(response)

if __name__ == "__main__":
    run_jarvis()
