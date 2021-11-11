from playsound import playsound
import datetime

print('Time ', datetime.datetime.now().time())
alarm_hour = 0
alarm_minute = 0


def alarm_setup():
    globals()['alarm_hour'] = int(input('Enter the alarm time hour:'))
    globals()['alarm_minute'] = int(input('Enter alarm time minutes:'))
    am_pm = input('am or pm:')
    print('Alarm set for: ', alarm_hour, ':', alarm_minute, am_pm)
    if am_pm == 'pm':
        globals()['alarm_hour'] += 12


alarm_setup()


def alarm_play():
    while True:
        if datetime.datetime.now().hour == alarm_hour and datetime.datetime.now().minute == alarm_minute:
            print('Alarm....')
            playsound('D:\\alarm_clock\\venv\\Lib\\site-packages\\radha-krishna.mp3')
            break


alarm_play()
