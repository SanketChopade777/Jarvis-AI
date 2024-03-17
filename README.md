The Project is a basic implementation of a voice-controlled assistant using the Tkinter library for the graphical user interface (GUI) and the Speech Recognition library for recognizing voice commands. While it serves as a foundation for creating a voice-controlled assistant with various applications.
❖ Explanation Of Code and module Used in Project -

1) Importing Libraries:
import tkinter as tk
from PIL import Image, ImageTk 
import speech_recognition as sr 
import os
import win32com.client
import webbrowser
import datetime
import threading
•    tkinter: Used for creating the graphical user interface (GUI).
•    PIL (Python Imaging Library): Used for working with images, particularly for displaying background and microphone images in the GUI.
•    speech_recognition: A library for performing speech recognition, used for capturing voice commands.
•    os: Provides a way to interact with the operating system, used for opening files and applications.
•    win32com.client: Allows communication with the Windows Speech API (SAPI), used for text-to-speech capabilities.
•    webbrowser: Provides a high-level interface to allow displaying Web-based documents to users, used for opening websites.
•    datetime: Used for working with dates and times.
•    threading: Used for creating and managing threads for concurrent execution.

2)  Function ‘execute_query’ :
def execute_query(query, speaker):
# ...
This function continuously listens for voice commands using a microphone. It utilizes the Speech Recognition library to capture audio and recognize the spoken words. The recognized text is then displayed on the GUI, and the execute query function is called to perform actions based on the recognized command.

3)  Fuction ‘’stop program’ :
def stop_program(stop_event, gui):
it ...
This function sets a threading event (stop_event) to signal the thread to stop, and it destroys the GUI

4)  Function ‘initializegui’ :
def initialize_gui():
This function initializes the GUI using the Tkinter library. It sets up labels, buttons, and  images for the background  and  microphone.  It also  starts a separate thread (recognition thread) to continuously listen for voice commands.

5)  Main Block:
if ..name.. == "..main..":
initialize_gui()
s = "Thanks for Using Jarvis A.I. Have a Great Day!" speaker = win32com.client.Dispatch("SAPI.SpVoice") speaker.Speak(s)
The main block of the script calls initialize gui to start the GUI and voice recognition. After the GUI is closed, it uses text-to-speech to say a farewell message.

6)  Overall Implementation:
•    The assistant responds to voice commands, performing actions like opening websites, playing music, and executing applications.
•    The GUI includes a background image, a microphone icon, and labels for displaying recognition status.
•    Voice recognition is performed continuously in a separate thread to avoid blocking the main GUI.

❖ After Running the Program -
1.  Opens the Screen Shown Below and takes Commands form the User
2.   When User say’s “Open” - Youtube Or Chrome they automatic Capture the command and open youtube or chrome accordingly without any interrupt.
The Following app’s and website are opened we can also include more app and website in the code as we need

Apps =>  "chrome", "firefox", "edge", "security scan", "adobe acrobat”
Website => "youtube", "google", "gmail", "linkedin", "wikipedia", "instagram", "facebook", "whatsapp", "twitter", "geek"

3.  Also it play music when user say’s “open music”
4.  And it tell’s Time when we say’s that “the time” (i.e 24 hour)
