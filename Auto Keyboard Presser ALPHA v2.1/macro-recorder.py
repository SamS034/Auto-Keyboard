import keyboard, time, sys, os, ctypes
from threading import Thread

#Global Variables:
pause_bool = 'y'

def record(user_time, end_key, playback_speed):
    print("Start Recording")
    record_keys = keyboard.record(until=end_key)
    record_keys = record_keys[1:-1]
    print("Keys Recorded!")
    thread = Thread(target = playback, args=[record_keys, user_time, playback_speed]) #playback thread
    thread.start()

def playback(record_keys, user_time, playback_speed): #thread1
    global pause_bool
    time.sleep(5)
    thread2 = Thread(target = interrupt, args=[], daemon=True) # interrupt thread
    time_end = time.time() + 60 *user_time
    time.sleep(1)
    thread2.start()
    print("Keys Playing...")
    while time.time() < time_end:
        if pause_bool == 'y':
            keyboard.play(record_keys, speed_factor=playback_speed)
        if pause_bool == 'n':
            pause_bool = input('Playback paused, continue? (y/n):')
            if pause_bool == 'y':
                continue
            if pause_bool == 'n':
                sys.exit(0)

def interrupt(): #thread2
    global pause_bool
    while(1):
        if (pause_bool == 'y'):
            input()
            pause_bool = 'n'
            print('Pause key detected! Pausing...')
        if (pause_bool == 'n'):
            continue

def configure():
    print("Auto Keyboard Clicker ALPHA v2.01")
    try:
        user_time = int(input('Minute(s) to repeat: '))
        end_key = input('Enter a stop recording key: ')
        playback_speed = float(input('Enter Playback Speed:'))
        input("Press Enter to begin recording keys...")
        record(user_time, end_key, playback_speed)
    except ValueError:
        print("That's not an integer!")

def start():
    try:
        user = os.getuid() == 0
    except AttributeError:
        user = ctypes.windll.shell32.IsUserAnAdmin() != 0

    if user is True:
        configure()
    else:
        input("Please run the program as Administrator...") #Bugfix: program closes before informing the user to run as admin
        sys.exit(0)

if __name__ == "__main__":
    start()
