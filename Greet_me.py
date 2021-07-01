import E_D_I_T_H
from datetime import datetime
from __speak__ import *
import datetime

def greetme(hour):
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning!')
    elif hour>=12 and hour<18:
        speak('Good Afternoon!')
    elif hour>=18 and hour!=0:
        speak('Good Evening!')
