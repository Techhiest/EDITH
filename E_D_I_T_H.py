

from Tic_Tac_Toe import play
import pyttsx3
import webbrowser as wb
import random
import os
import sys
import speech_recognition as sr
import smtplib
import datetime

from Take_Command import *
from __speak__ import *
from __intro__ import *
from Greet_me import *
from B_J import *

from war import *
from suduko import *
from calculator import *

if __name__=='__main__':
    introduce()
    while True:
        
        query=takecommand()
        query=query.lower()
        if 'open youtube' in query:
            speak('Okay Sir!')
            wb.open('www.youtube.com')
        elif 'open google' in query:
            speak('Almost getting there')
            wb.open('www.google.com')
        elif 'What\'s up' in query or 'how are you' in query:

            stmsgs=['Just doing my thing!','I am fine','I am nice and full of energy']
            speak(random.choice(stmsgs))
        elif 'bye' in query:
            speak('Bye Boss, Have a nice day')
            sys.exit()
        elif 'thank you' in query:
            speak('welcome Sir')
        elif 'the date' in query:
            speak('just a minute sir')
            strdate=datetime.datetime.today().strftime('%d %m %y')
            speak('Sir today\'s date is %s' %strdate)
        elif 'who created you' in query:
            speak('My creator is Mr.Gaurav Kumar')
        elif 'games' in query:
            speak('Your are in mood of playing game')
            speak(' Let\'s play')
            speak('Which game do you want to play?')
            speak("You have the following option to play.")
            speak('1. Black Jack \n 2. War \n 3. Suduko \n 4. Tic Tac Toe')
            c=str(input("Enter the name of the game: ")).lower()
            if c=='tic tac toe':
                play()
            if c=='black jack':
                play_bj()
            
            if c=='war':
                play_war()
            if c=='suduko':
                play_suduko()
        elif 'calculator' in query:
            speak('Seems like you are stuck with some calculations.')
            speak('getting you a calculator for help.')
            sc()
        else:
            print('None Answerable.')


