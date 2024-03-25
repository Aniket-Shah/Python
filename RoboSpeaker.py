# import pyttsx3
#
# if __name__ == '__main__':
#     print("Welcome to RoboSpeaker 1.1 Created by Aniket")
#     engine = pyttsx3.init()
#     while True:
#         x = input("Enter what you want me to speak: ")
#         if x == "q":
#             break
#         engine.say(x)
#         engine.runAndWait()

import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")

while True:
    text = input("Enter what you want me to speak: ")
    if text == "q":
        break
    speak.Speak(text)
