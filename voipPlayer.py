import pygetwindow as pw
import pyautogui as pg
import time
import speech_recognition as sr
import dotenv
import os

dotenv.load_dotenv()

keymap = {"forward": "w", "backward": "s", "left": "a", "right": "d", "jump": "space"}
X_OFFSET = 100
game = "Minecraft"


## Game Commands:
def forward():
    pg.keyDown(keymap["forward"])


def backward():
    pg.keyDown(keymap["backward"])


def left():
    pg.keyDown(keymap["left"])


def right():
    pg.keyDown(keymap["right"])


def jump():
    pg.keyDown(keymap["jump"])
    time.sleep(0.05)
    pg.keyUp(keymap["jump"])


def stop():
    for key in keymap.values():
        pg.keyUp(key)


def mouse_left():
    pg.moveRel(-X_OFFSET, yOffset=0, duration=0.25)


def mouse_right():
    pg.moveRel(X_OFFSET, yOffset=0, duration=0.25)


def move_right():
    for i in range(2):
        pg.moveRel(X_OFFSET, yOffset=0, duration=0.25)
    pg.keyDown(keymap["forward"])


def move_left():
    for i in range(2):
        pg.moveRel(-X_OFFSET, yOffset=0, duration=0.25)
    pg.keyDown(keymap["forward"])


def creative():
    pg.write("/gamemode creative", interval=0.1)
    pg.press("enter")


def survival():
    pg.write("/gamemode survival", interval=0.1)
    pg.press("enter")


def look_back():
    for i in range(4):
        pg.moveRel(X_OFFSET, yOffset=0, duration=0.25)


def day():
    pg.write("/time set day", interval=0.1)
    pg.press("enter")


def night():
    pg.write("/time set night", interval=0.01)
    pg.press("enter")


def break_block():
    pg.click()


def place_block():
    pg.keyDown(keymap["jump"])
    pg.keyUp(keymap["jump"])
    pg.click(button="right")


def activate_window(title):
    game = pw.getWindowsWithTitle(title)[0]
    game.minimize()
    game.restore()
    screen_width, screen_height = pg.size()
    pg.moveTo(screen_width // 2, screen_height // 2)


def quit_command(title):
    quit = pw.getWindowsWithTitle(title)
    if quit:
        quit[0].close()


if __name__ == "__main__":
    # Speech Recognition
    s = sr.Recognizer()
    s.energy_threshold = 5000
    s.pause_threshold = 0.5
    with sr.Microphone() as source:
        print("Calibrating...")
        s.adjust_for_ambient_noise(source)
        print("Calibration Complete!")
        activate_window(game)

    # commands for movement
    while True:
        with sr.Microphone() as source:
            print("Talk Now")
            audio = s.listen(source)
            print("Processing...")
            try:
                start = time.time()
                word = s.recognize_azure(
                    audio,
                    key=os.environ.get("API_KEY"),
                    language="en-IN",
                    location="centralindia",
                )[0].lower()
                end = time.time()

                analysis_duration = round(end - start, 4)
                print(f"{word} took {analysis_duration} seconds")

                if "left" in word:
                    mouse_left()
                if "right" in word:
                    mouse_right()
                if "forward" in word or "straight" in word:
                    forward()
                if "stop" in word:
                    stop()
                if "jump" in word:
                    jump()
                if "fly" in word:
                    for i in range(2):
                        jump()
                if "creative" in word or "immortal" in word:
                    creative()
                if "survival" in word or "normal" in word:
                    survival()
                if "back" in word:
                    look_back()
                if "day" in word:
                    day()
                if "night" in word:
                    night()
                if "go right" in word or "move right" in word:
                    move_right()
                if "go left" in word or "move left" in word:
                    move_left()
                if "quit" in word:
                    print("Closing game")
                    time.sleep(1)
                    quit_command(game)
                    print("See you next time !")
                    break
                if "attack" in word or "break" in word:
                    break_block()
                if "place block" in word or "place" in word:
                    place_block()
                if word.isdigit() and 1 <= int(word) <= 9:
                    print("went here")
                    pg.keyDown(keymap[(str(word))])
            except sr.WaitTimeoutError:
                print("No speech detected !")
            except sr.UnknownValueError:
                print("Failed to recognize speech")
            except sr.RequestError:
                print("Failed to access API, please check your internet connection")
