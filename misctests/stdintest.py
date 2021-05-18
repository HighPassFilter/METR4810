import sys
import keyboard

keyboard.add_hotkey('\r', print, args=('triggered', 'hotkey'))

if __name__ == "__main__":
    while True:
        a = 1