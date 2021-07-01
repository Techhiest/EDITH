
import E_D_I_T_H
import smtplib



def sendmail(to,content):
    server.smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('46gauravkumar@gmail.com','GAURAV=05')
    server.sendmail('46gauravkumar@gmail.com',to,content)

    server.close()