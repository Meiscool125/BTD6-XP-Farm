import time

import keyboard
import pyautogui

if __name__ == "__main__":
    while True:
        if keyboard.is_pressed("t"):
            x, y = pyautogui.position()
            print(f"Mouse position: {x}, {y}")
            time.sleep(0.5)
