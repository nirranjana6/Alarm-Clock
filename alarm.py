
import time
import os
import winsound
import keyboard

term_prog = 0      

while True:

    if term_prog == 1:    # Condition to terminate the application
        print('Thank You For Using Our Application!')
        time.sleep(2)
        os.system('cls')
        break


    print("OPTIONS :")
    print("Enter '0' just to view the time")
    print("Enter '1' for Alarm \nEnter '2' for Timer \nEnter '3' for Stopwatch ")
    print("Enter '4' to terminate the application.")
    Option_Clock = input('')
    print()


    if Option_Clock[-1] == '0' or Option_Clock[-1] == '1':  
        # Option Chosen : Clock (OR) Alarm
        print('If you want your CLOCK to be shown in ')
        print('(i) 12hr format => Enter 1')
        print('(ii) 24hr format => Enter 2')
        Option_Type = int(input(''))
        print()


    if Option_Clock[-1] == "1":

        k = 1
        while k == 1:

            k = 0
            print('Enter alarm in 24 hr format', end=' ')
            print('["HH:MM:SS"]  -  default is 00:00:00')
            alarm_time = input('')
            alarm_list = alarm_time.split(":")
            alarm_mesg = input("Enter Alarm Message : ")

            for i in range(len(alarm_list)):
                if alarm_list[i] == '':
                    alarm_list.pop(i)
                    alarm_list.insert(i, 0)
            if len(alarm_list) == 0:
                alarm_hr = 0
                alarm_min = 0
                alarm_sec = 0
            elif len(alarm_list) == 1:
                alarm_hr = int(alarm_list[0])
                alarm_min = 0
                alarm_sec = 0
            elif len(alarm_list) == 2:
                alarm_hr = int(alarm_list[0])
                alarm_min = int(alarm_list[1])
                alarm_sec = 0
            elif len(alarm_list) == 3:
                alarm_hr = int(alarm_list[0])
                alarm_min = int(alarm_list[1])
                alarm_sec = int(alarm_list[2])
            else:
                print()
                print('INVALID INPUT')
                time.sleep(1)
                k = 1
                os.system('cls')




            if alarm_hr > 23 or alarm_min > 59 or alarm_sec > 59:
                print()
                print("INVALID")
                time.sleep(1)
                k = 1
                os.system('cls')
            elif alarm_hr < 0 or alarm_min < 0 or alarm_sec < 0:
                print()
                print("INVALID")
                time.sleep(1)
                k = 1
                os.system('cls')

        os.system('cls')
        print('Your Alarm has been set for  ', str(alarm_hr).zfill(2), ':',
              str(alarm_min).zfill(2), ':', str(alarm_sec).zfill(2), sep='')
        time.sleep(2)

   
    os.system('cls')            # this command clears the screen
    t = time.localtime()        # system time stored into a variable 't'
    current_time = time.strftime("%H:%M:%S", t)
    hr = int(current_time[0]+current_time[1])
    min = int(current_time[3]+current_time[4])
    sec = int(current_time[6]+current_time[7])

    def make_sound(type):  
        # default function to make sound for alarm and timer.

        i = 0  
        if type == '2':
            print('Press "m" to go back to menu')
            print(' --------')
            print('|', '00', ':', '00', ':', '00', '|', sep='')
            print(' --------')
            print('TIME IS UPP !!!')
            while i < 10:
                if keyboard.is_pressed('m'):
                    # i_break_loop = 1
                    os.system('cls')
                    break
                winsound.Beep(500, 1000)
                i += 1
            os.system('cls')
        else:
            while i < 10:
                winsound.Beep(500, 500)
                i += 1
            os.system('cls')



    def Clock_Alarm(hr, min, sec, Opt_Cl, Opt_Type):
        # Function Definition for Clock (AND) Alarm

        i_break_loop = 0
        i_Alarm = 0
        i_SnoozePressed = 0
        while True:
            if i_break_loop == 1:
                break
            h = hr
            while h < 24:
                if i_break_loop == 1:
                    break
                if h == 23: 
                    hr = 0
                    # Ensuring that hour does not turn to 24, 25, etc.
                m = min
                while m < 60:
                    if i_break_loop == 1:
                        break
                    if m == 59:
                        min = 0  
                        # Ensuring that min does not turn to 60, 61, etc.
                    s = sec
                    while s < 60:

                        os.system('cls')
                        print('Press "m" to go back to menu')
                        print()

                        if keyboard.is_pressed('m'):
                            # Condition to go back to menu
                            i_break_loop = 1
                            os.system('cls')
                            break

                        if Opt_Type == 1:
                            # Time Format Chosen : 12 Hour Format

                            if h > 12:
                                print(' -----------')
                                print('|', str(h-12).zfill(2), ':', str(m).zfill(
                                    2), ':', str(s).zfill(2), ' PM', '|', sep='')
                                print(' -----------')
                            elif h < 12:
                                print(' -----------')
                                print('|', str(h).zfill(2), ':', str(m).zfill(
                                    2), ':', str(s).zfill(2), ' AM', '|', sep='')
                                print(' -----------')
                            else:
                                print(' -----------')
                                print('|', '12', ':', str(m).zfill(
                                    2), ':', str(s).zfill(2), ' PM', '|', sep='')
                                print(' -----------')

                        else:
                            # Time Format Chosen : 24 Hour Format

                            print(' --------')
                            print('|', str(h).zfill(2), ':', str(m).zfill(
                                2), ':', str(s).zfill(2), '|', sep='')
                            print(' --------')

                        if s == 59:
                            sec = 0
                            # Looping back condition

                        if Opt_Cl == '1':
                            if alarm_hr == h and alarm_sec == s and alarm_min == m:
                                i_Alarm = 1

                        if i_Alarm > 0 and i_Alarm <= 30:

                            if i_SnoozePressed == 0 or i_SnoozePressed == 30:
                                print((alarm_mesg + ' ')*5, '\n')
                                print('Long press "z" to snooze for 30 seconds.')
                                print('Long press "d" to dismiss the alarm.')
                                winsound.Beep(500, 1000)
                                i_Alarm += 1
                                if i_SnoozePressed == 30:
                                    i_SnoozePressed = 0
                                    i_Alarm = 1
                            else:
                                time.sleep(1)
                            if i_SnoozePressed > 0:
                                i_SnoozePressed += 1
                            if keyboard.is_pressed('z'):
                                i_SnoozePressed = 1
                            elif keyboard.is_pressed('d'):
                                i_SnoozePressed = -1

                        else:
                            time.sleep(1)

                        s += 1
                    m += 1
                h += 1



    def Timer(Opt_Cl):

        i_break_loop = 0

        timer_time = input('Set your timer as "HH:MM:SS" : ')
        timer_list = timer_time.split(":")
        timer_hr = int(timer_list[0])
        timer_min = int(timer_list[1])
        timer_sec = int(timer_list[2])

        while True:
            if i_break_loop == 1:
                break

            for h in range(timer_hr, -1, -1):
                # Same as clock, but moving backwards.

                if i_break_loop == 1:
                    break
                if h == 0:
                    timer_hr = 23


               
    for m in range(timer_min, -1, -1):
                    if i_break_loop == 1:
                        break
                    if m == 0:
                        timer_min = 59

                    for s in range(timer_sec, -1, -1):
                        os.system('cls')
                        print('Press "m" to go back to menu')
                        if keyboard.is_pressed('m'):
                            i_break_loop = 1
                            os.system('cls')
                            break
                        print(' --------')
                        print('|', str(h).zfill(2), ':', str(m).zfill(
                            2), ':', str(s).zfill(2), '|', sep='')
                        print(' --------')
                        if s == 0:
                            timer_sec = 59
                        if h == 0 and m == 0 and s == 0:
                            time.sleep(1)
                            os.system('cls')
                            make_sound(Opt_Cl)
                            if i_break_loop == 1:
                                os.system('cls')
                                break 
                            i_break_loop = 1 
                            # Condition to break the loop
                            break

                        time.sleep(1)



    def Stop_Watch(sw_hour, sw_min, sw_sec):

        i_break_loop = 0

        sw_list = []
        # This list will store all the LAPed values

        lap_flag = 0
        # Used for LAP condition

        while True:

            if i_break_loop == 1:
                break
            h = sw_hour
            # Variable storing the HOUR of stopwatch

            while h < 24:
                if i_break_loop == 1:
                    break
                m = sw_min
                # Variable storing the MINUTE of stopwatch

                while m < 60:
                    if i_break_loop == 1:
                        break
                    s = sw_sec
                    # Variable storing the SECONDS of stopwatch

                    while s < 60:
                        i_reset = 0
                        if i_break_loop == 1:
                            break

                        os.system('cls')
                        print("Long press 's' to stop and return to menu")
                        print("Long press 'p' to pause ")
                        print("Long press 'l' to lap ")

                        if lap_flag == 0:
                            print(' ========')
                            print('|', str(h).zfill(2), ':', str(m).zfill(
                                2), ':', str(s).zfill(2), '|', sep='')
                            print(' ========')
                            print()

                        if keyboard.is_pressed('s'):
                            # OPTION SELECTED : Stop And Return To Menu

                            os.system('cls')
                            i_break_loop = 1
                            print("FINAL TIME :")
                            print(' ========')
                            print('|', str(h).zfill(2), ':', str(m).zfill(2), ':', str(s).zfill(2), '|', sep='')
                            print(' ========')
                            winsound.Beep(500, 3000)
                            os.system('cls')
                            break

                        elif keyboard.is_pressed('p'):
                            # OPTION SELECTED : Pause

                            print("Press 'r' for reset and", end=' ')
                            print("any other key to continue")
                            SW_INPUT = input("")

                            if SW_INPUT[len(SW_INPUT)-1] == 'r':
                                # If reset chosen, stopwatch goes back to 00:00:00

                                i_reset = 1  
                                # condition for reset

                                s = 0
                                m = 0
                                h = 0
                                # Setting back to 00:00:00

                            if i_reset == 1:
                                sw_list = []

                        elif keyboard.is_pressed('l'):
                            # OPTION SELECTED : Lap

                            lap_flag = 1
                            sw_list.append(' --------' + '\n' + '        |' + str(h).zfill(
                                2) + ':' + str(m).zfill(
                                2) + ':' + str(s).zfill(
                                2) + '|' + '\n' + '         --------')

                        for i in range(len(sw_list)):
                            print('Lap', i+1, ': ', end='')
                            print(sw_list[i])
                        if lap_flag == 1:
                            print(' ========')
                            print('|', str(h).zfill(2), ':', str(m).zfill(2), ':', str(s).zfill(2), '|', sep='')
                            print(' ========')
                            print()

                        time.sleep(1)
                        s += 1
                    if i_reset != 1:  # checking reset condition
                        m += 1
                if i_reset != 1:  # checking reset condition
                    h += 1




    if Option_Clock[-1] == '0' or Option_Clock[-1] == '1':
        Clock_Alarm(hr, min, sec, Option_Clock[-1], Option_Type)  
    if Option_Clock[-1] == '2':
        Timer(Option_Clock[-1])  
    if Option_Clock[-1] == '3':
        print("Long press 's' to stop and return to menu")
        print("Long press 'p' to pause")
        print("Long press 'l' to lap ")
        time.sleep(1)
        Stop_Watch(0, 0, 0)  
    if Option_Clock[-1] == '4':
        term_prog = 1