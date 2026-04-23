import time
import keyboard
import pyautogui

MK_GAINED = 0

def moveMouseTo(x, y, delay=0.1):
    pyautogui.moveTo(x, y)
    time.sleep(delay)

def click_and_wait(delay=0.1):
    pyautogui.click()
    time.sleep(delay)

def gotoMap():
    time.sleep(0.1)

    moveMouseTo(1280, 1260) # Click "Play" button
    click_and_wait(0.3)

    moveMouseTo(1800, 1300) # Click "Expert" maps
    click_and_wait()
    click_and_wait() # Confirm Expert selection

    moveMouseTo(720, 350) # Select a specific map
    click_and_wait(0.3)

    moveMouseTo(850, 550) # Select difficulty (easy)
    click_and_wait(0.3)

    moveMouseTo(1700, 600) # Select subdifficulty (deflation)
    click_and_wait(3) # Wait for map to load

    moveMouseTo(1300, 1000) # Click "OK" on round start
    click_and_wait(1)


def completeMap():
    """
    Executes a sequence of actions to complete a map, including placing monkeys,
    upgrading, and checking for Monkey Knowledge (MK) gained.
    """
    global MK_GAINED
    placeMonkey(200,750,"z","3-2-0")
    for i in range(3): # Cycle through targeting options to target "strong" for this monkey
        keyboard.press_and_release("tab")
        time.sleep(0.1)
    placeMonkey(1110,520,"q","2-0-3")
    placeMonkey(1110,900,"q","2-0-3")
    placeMonkey(720,1000,"c","0-3-2")
    placeMonkey(1500,400,"c","0-3-2")
    placeMonkey(2015,750,"z","2-0-4")

    keyboard.press_and_release("space") # Start rounds
    time.sleep(0.5)
    keyboard.press_and_release("space") # Speed up game
    time.sleep(11) # Wait for map completion
    # Check pixels to see if MK screen is detected
    if check_pixels():
        MK_GAINED += 1
        print(f"MK Gained: {MK_GAINED}")
        click_and_wait(0.5) # Click to dismiss MK screen 1
        click_and_wait(10)  # Click to dismiss MK screen 2, Wait after dismissing MK screen to confirm map is complete

    moveMouseTo(1270, 1200) # Click "Next" after game
    click_and_wait(0.5)

    moveMouseTo(950, 1100) # Click "Exit to home"
    click_and_wait(2.5)

def placeMonkey(x, y, monkeyKeybind="q", upgradePath="0-0-0"):
    """
    Places a monkey at given coordinates and applies specified upgrades.
    """
    keyboard.press_and_release(monkeyKeybind)
    time.sleep(0.1)
    moveMouseTo(x, y)
    keyboard.press_and_release("tab") # Snap to nearest valid placement point
    time.sleep(0.1)
    click_and_wait() # Place the monkey
    click_and_wait() # Open upgrade menu
    upgradeMonkey(upgradePath)
    time.sleep(0.1)

def upgradeMonkey(upgradePath="0-0-0"):
    """
    Applies upgrades to a selected monkey based on a path string (e.g., "2-0-4").
    """
    upgrade_counts = upgradePath.split('-')
    upgrade_keys = [",", ".", "/"] # Keys for top, middle, bottom path upgrades
    time.sleep(0.1) # Small delay before starting upgrades
    for i in range(len(upgrade_counts)):
        key_to_press = upgrade_keys[i]
        num_times_to_press = int(upgrade_counts[i])
        for _ in range(num_times_to_press):
            keyboard.press_and_release(key_to_press)
            time.sleep(0.15) # Delay between each upgrade press

def check_pixels():
    """
    Takes a screenshot and checks the RGB color of three specific pixels.
    Returns True if all pixels match their expected colors, False otherwise.
    """
    x1 = 100
    y1 = 200
    expected_color1 = (5, 3, 9)
    x2 = 300
    y2 = 400
    expected_color2 = (19, 13, 36)
    x3 = 1849
    y3 = 1241
    expected_color3 = (20, 15, 40)
    screenshot = pyautogui.screenshot()
    pixel_color1 = screenshot.getpixel((x1, y1))
    pixel_color2 = screenshot.getpixel((x2, y2))
    pixel_color3 = screenshot.getpixel((x3, y3))

    # uncomment these lines to debug pixel colors
    """
    label_w = 17

    print(f"{'expected color 1:':<{label_w}} {expected_color1} | "
          f"{'expected color 2:':<{label_w}} {expected_color2} | "
          f"{'expected color 3:':<{label_w}} {expected_color3}")

    print(f"{'pixel 1:':<{label_w}} {pixel_color1} | "
          f"{'pixel 2:':<{label_w}} {pixel_color2} | "
          f"{'pixel 3:':<{label_w}} {pixel_color3}")

    print("-" * 80)
    """
    if pixel_color1 == expected_color1 and pixel_color2 == expected_color2 and pixel_color3 == expected_color3:
        return True
    else:
        return False
