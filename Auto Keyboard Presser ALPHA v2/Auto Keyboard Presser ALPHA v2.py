import keyboard, time, sys, os, ctypes

def record(user_time, end_key):
    print("Start Recording")
    record_keys = keyboard.record(until=end_key)
    record_keys = record_keys[1:-1]
    print("Keys Recorded!")
    playback(record_keys, user_time)

def playback(record_keys, user_time):
    time.sleep(5)
    print("Keys Playing...")
    time_end = time.time() + 60 *user_time
    while time.time() < time_end:
        time.sleep(1)
        keyboard.play(record_keys)
    print("Keys played for "+ str(user_time) + " minute(s)")
    print("recorder resetting...")
    time.sleep(1)

def configure():
    print("Auto Keyboard Clicker ALPHA v2")
    while True:
        try:
            user_time = int(input('Minute(s) to repeat: '))
            end_key = input('Enter a stop recording key: ')
            input("Press Enter to begin recording keys...")
            record(user_time, end_key)
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
        print("Run the program as Administrator")
        sys.exit(0)

if __name__ == "__main__":
    start()
