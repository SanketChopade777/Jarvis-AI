import tkinter as tk
from PIL import Image, ImageTk
import speech_recognition as sr
import os
import win32com.client
import webbrowser
import datetime
import threading

def execute_query(query, speaker):
    keywords = ["open", "time", "music", "chrome", "firefox", "edge", "security scan", "adobe acrobat"]

    is_valid_query = any(keyword in query.lower() for keyword in keywords)
    if is_valid_query:
        speaker.Speak("Hello, I am Jarvis A.I")
        sites = [
            ["youtube", "https://www.youtube.com"],
            ["google", "https://www.google.com"],
            ["mail", "https://mail.google.com/mail/u/0/#inbox"],
            ["linkedin","https://www.linkedin.com/feed/"],
            ["wikipedia", "https://www.wikipedia.com"],
            ["instagram", "https://www.instagram.com"],
            ["facebook", "https://www.facebook.com"],
            ["whatsapp", "https://www.whatsapp.com"],
            ["twitter", "https://www.twitter.com"],
            ["gcek", "https://www.gcekarad.ac.in"],
            ["chatgpt", "https://chat.openai.com/"]
        ]

        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                say = f"Opening {site[0]} Sir..."
                speaker.Speak(say)
                webbrowser.open(site[1])

        if "open music" in query:
            musicPath = "E:\\Music\\song.mp3"  # Replace this with the actual path
            os.system(f"start {musicPath}")

        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say = f"Sir, the time is {strfTime}"
            speaker.Speak(say)

        apps = [
            ["chrome", "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"],
            ["firefox", "C:\\Program Files\\Mozilla Firefox\\firefox.exe"],
            ["microsoft edge", "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"],
            ["security scan", "C:\\Users\Public\Desktop\PC Manager.lnk"],
            ["adobe acrobat", "C:\\Program Files\\Adobe\\Acrobat DC\\Acrobat\\Acrobat.exe"]
        ]

        for app in apps:
            if f"open {app[0]}".lower() in query.lower():
                say = f"Opening {app[0]} Sir..."
                speaker.Speak(say)
                os.startfile(app[1])  # Using os.startfile to open the application
    else:
        # Indicate that the query doesn't match any valid command
        speaker.Speak("I'm sorry, I didn't understand that command.")

def take_command(speaker, stop_event, recognized_label):
    r = sr.Recognizer()
    r.energy_threshold = 4000  # Adjust this value as needed
    while not stop_event.is_set():
        try:
            with sr.Microphone() as source:
                audio = r.listen(source, phrase_time_limit=3)  # Listen for 5 seconds
                query = r.recognize_google(audio, language="en-in")
                recognized_label.config(text=f"Recognized: {query}", fg="yellow")
                execute_query(query, speaker)
        except sr.WaitTimeoutError:
            pass
        except sr.UnknownValueError:
            pass
        except Exception as e:
            recognized_label.config(text="Some Error Occurred. Please Try Again!", fg="red")

def stop_program(stop_event, gui):
    stop_event.set()
    gui.destroy()

def initialize_gui():
    gui = tk.Tk()
    gui.title("Jarvis A.I.")
    gui.geometry("600x600")
    gui.configure(bg="black")

    background_img = Image.open("1699183481554_imgbg.net.png")
    background_img = ImageTk.PhotoImage(background_img)
    background_label = tk.Label(gui, image=background_img, bg="black")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    microphone_img = Image.open("1699184693484_imgbg.net.png")
    microphone_img = microphone_img.resize((100, 120))
    microphone_img = ImageTk.PhotoImage(microphone_img)

    microphone_label = tk.Label(gui, image=microphone_img, bg="black")
    microphone_label.pack()

    listening_label = tk.Label(gui, text="Listening...", fg="white", bg="black", font=("Rockwell Extra Bold", 20))
    listening_label.pack()


    recognized_label = tk.Label(gui, text="Recognizing", fg="white", bg="black", font=("Aptos", 14))
    recognized_label.pack()

    stop_button = tk.Button(gui, text="Stop", command=lambda: stop_program(stop_event, gui), fg="white", bg="black",
                            font=("Snap ITC", 14))
    stop_button.pack(side=tk.BOTTOM, pady=20)

    recognized_label.configure(font=("Arial", 14))
    stop_button.configure(width=10, height=2, relief=tk.FLAT)

    stop_event = threading.Event()

    speaker = win32com.client.Dispatch("SAPI.SpVoice")

    recognition_thread = threading.Thread(target=take_command, args=(speaker, stop_event, recognized_label))
    recognition_thread.daemon = True  # Set the thread as daemon
    recognition_thread.start()

    gui.mainloop()

if __name__ == "__main__":
    initialize_gui()
    s = "Thanks for Using Jarvis A.I. Have a Great Day!"
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(s)
