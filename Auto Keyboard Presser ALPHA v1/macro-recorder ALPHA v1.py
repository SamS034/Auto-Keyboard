#from win32gui import GetWindowText, GetForegroundWindow
import keyboard, time, sys, pyautogui

# INFO: BUGS LIST (3/1/20)
# 1. End record key is being part of the recorded key stroke
# 2. Some programs uses "esc" key 
# 3. Keyboard playback sometimes non-functional in certain apps

def record(user_time):
    print("Recording start:")
    recorded = keyboard.record(until='esc')
    print("Keys Recorded!")
    playback(recorded, user_time)

def playback(recorded, user_time):
    time.sleep(5)
    print("Keys Playing...")
    time_end = time.time() + 60 *user_time
    while time.time() < time_end:
        time.sleep(1)
        keyboard.play(recorded)
    print("Keys played for "+ str(user_time) + " minute(s)")
    print("recorder resetting...")
    time.sleep(1)

def time_set():
    while True:
        try:
            user_time = int(input('Minute(s) to repeat: '))
            record(user_time)
        except ValueError:
            print("That's not an integer!")


def main():
    print('Macro Recorder')
    print('1. Recording starts when the first key is pressed at "Recording Start:"')
    print('2. To end recording and start recorded macro, press "esc"')
    print('3. Keep target program opened during the playback')
    while True:
        start = input('start recorder? (y/n) ')
        if start == 'y':
            time_set()
        if start == 'n':
            print('Program exiting...')
            time.sleep(1)
            sys.exit(0)
        else:
            print("please choose 'y' or 'n' ")

if __name__ == "__main__":
    main()