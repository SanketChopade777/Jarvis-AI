# 🧑‍💻 Voice-Controlled Assistant using Python

Welcome to the **Jarvis A.I. Project** 🌐 — a basic implementation of a **voice-controlled assistant** using **Tkinter** for GUI and **SpeechRecognition** for interpreting user commands via microphone! This assistant can open applications, websites, play music, tell time, and more! ⏰🎵

---

## 🔍 Features

- 🚀 Voice-controlled command execution
- 🎨 Interactive GUI with background & microphone icon
- 🌍 Opens apps & websites using voice
- ⏳ Tells current time (24-hour format)
- 🎶 Plays music on voice command

---

## 🧰 Libraries & Modules Used

```python
import tkinter as tk
from PIL import Image, ImageTk
import speech_recognition as sr
import os
import win32com.client
import webbrowser
import datetime
import threading
```

### 💡 Module Explanations:
- **tkinter** 💻: Builds the GUI.
- **PIL** 📷: Manages background and microphone images.
- **speech_recognition** 🎤: Converts speech to text.
- **os** 🗄: Interacts with OS for opening files/apps.
- **win32com.client** 🎤: Handles text-to-speech via Windows SAPI.
- **webbrowser** 🌐: Opens websites in the browser.
- **datetime** 🕒: Gets current system time.
- **threading** 🧱: Allows continuous speech recognition in a separate thread.

---

## 🔊 Code Explanation

### 1) `execute_query(query, speaker)`
- Continuously listens to the user's microphone input.
- Converts spoken words into text and executes actions based on recognized command.

### 2) `stop_program(stop_event, gui)`
- Gracefully stops the application by terminating threads and closing the GUI.

### 3) `initialize_gui()`
- Creates the GUI using `Tkinter`
- Sets up background, microphone icon, and GUI layout
- Starts the recognition thread

### 4) `main` Block
```python
if __name__ == "__main__":
    initialize_gui()
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak("Thanks for Using Jarvis A.I. Have a Great Day!")
```
- Launches the app and says goodbye with text-to-speech after GUI closes.

---

## 🚀 Application Usage & Output

### ▶️ After Running the Program:
1. GUI with microphone icon launches.
2. Start speaking your command.

### 🔊 Sample Voice Commands:

#### 📗 Open Applications:
- "Open Chrome"
- "Open Firefox"
- "Open Adobe Acrobat"
- "Open Edge"

#### 🌐 Open Websites:
- "Open YouTube"
- "Open Google"
- "Open Gmail"
- "Open Instagram"
- "Open Wikipedia"
- "Open LinkedIn"
- "Open WhatsApp"
- "Open Facebook"
- "Open Twitter"
- "Open Geek"

#### 🎶 Music & Time:
- "Open Music"
- "What's the time?"

You can easily add more apps/websites by modifying the `execute_query` logic 🔧.

---

## 🚀 How to Extend?
- 🔹 Add more applications & commands
- 🔹 Integrate AI-based NLP for smart responses
- 🔹 Enhance GUI with voice indicators

---

## 📄 Requirements

Install dependencies using pip:
```bash
pip install pillow speechrecognition pywin32
```

---

## 🌟 Final Thoughts
This project is a great starting point for creating your own AI-powered assistant.
Customize it, expand it, and make it your own! 🌍✨

---

Made with ❤️ by Sanket Chopade

---


