
import E_D_I_T_H
from __speak__ import *
def takecommand():
    try:
        speak('You just type and ask me any query.')
        query=str(input('Command: '))
    except:
        speak('Sorry Boss, I didn\'t get that please try again.')
        query=str(input("Command: "))
    return query
    