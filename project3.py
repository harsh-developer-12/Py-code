# from kivy.app import App
# from kivy.uix.textinput import TextInput

# class first(App):
#     def build(self):
#         return TextInput(
#             hint_text=" type msg",                               ## hint text set krne ke liye  as placeholdetr
#             multiline=True,
#             font_size=20 
#         )
    
# first().run()  





# from kivy.app import App 
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.button import Button 

# class chatApp(App):
#     def build(self):    
#           layout = BoxLayout (orientation = 'vertical' , size_hint=(.1, .1), pos_hint={'last_y':.5, 'last_x':.2})
#           btn1 = Button(text="send")
#           btn2 = Button(text="receive")
#           layout.add_widget(btn1)
#           layout.add_widget(btn2)
#           return layout
         
# chatApp().run()






# from logging.config import listen
# import speech_recognition as sr
# import pyttsx3
# import webbrowser

# # text to speech
# engine = pyttsx3.init()

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# # speech to text
# def listen():
#    r = sr.Recognizer()

# with sr.Microphone() as source:
#         speak("hello pande ji, mai sun raha hun, boliye kya kehna hai")
#         audio = r.listen(source)
# try:
#     text = r.recognize_google(audio, language="hi-IN")
#     print("Tumne bola:", text)
#     speak("Tumne kaha " + text)

# except:
#     speak("Sorry, main samajh nahi paya")

# def nova():
#     while True:
#       command = "listen"
#       if "Google kholo" in command:
#                 webbrowser.open("")
#                 speak("Google khol raha hun")

#       elif "YouTube kholo" in command:
#                 webbrowser.open("https://www.youtube.com")
#                 speak("YouTube khol raha hun")

#       elif "band karo" in command:
#                 speak("theek hai pande ji, alvida")
#                 break

# except:
# speak("Sorry, main samajh nahi paya")
    
# nova()




