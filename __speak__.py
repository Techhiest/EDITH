import pyttsx3
import speech_recognition as sr
import E_D_I_T_H
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    print('Jarvis: '+audio)
    engine.say(audio)
    engine.runAndWait()