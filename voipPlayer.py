import pygetwindow as pw
import pyautogui as pg
import time
import azure.cognitiveservices.speech as speechsdk
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


def right():
    for i in range(2):
        pg.moveRel(X_OFFSET, yOffset=0, duration=0.25)
    pg.keyDown(keymap["forward"])


def left():
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


def start_speech_engine():
    done = False

    def stop_cb():
        print("Stopping Recognition")
        speech_recognizer.stop_continuous_recognition()
        nonlocal done
        done = True

    speech_config = speechsdk.SpeechConfig(
        subscription=os.environ.get("API_KEY"), region="centralindia"
    )
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    speech_recognizer.recognizing.connect(analyse)
    speech_recognizer.session_started.connect(lambda _: print("Voice engine active!"))
    speech_recognizer.canceled.connect(lambda _: print("API Failure"))
    speech_recognizer.session_stopped.connect(stop_cb)
    speech_recognizer.start_continuous_recognition()
    while not done:
        time.sleep(0.5)


def analyse(evt):
    word = evt.result.text


import pygetwindow as pw
import pyautogui as pg
import time
import azure.cognitiveservices.speech as speechsdk
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


def right():
    for i in range(2):
        pg.moveRel(X_OFFSET, yOffset=0, duration=0.25)
    pg.keyDown(keymap["forward"])


def left():
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

def attack():
    pg.click()

def break_block():
    pg.h


def place_block():
    pg.keyDown(keymap["jump"])
    pg.keyUp(keymap["jump"])
    pg.click(button="right")


def launch_game(title):
    game = pw.getWindowsWithTitle(title)[0]
    game.minimize()
    game.restore()
    screen_width, screen_height = pg.size()
    pg.moveTo(screen_width // 2, screen_height // 2)


def quit_command(title):
    quit = pw.getWindowsWithTitle(title)
    if quit:
        quit[0].close()


def start_speech_engine():
    done = False

    def stop_cb():
        print("Stopping Recognition")
        speech_recognizer.stop_continuous_recognition()
        nonlocal done
        done = True

    speech_config = speechsdk.SpeechConfig(
        subscription=os.environ.get("API_KEY"), region="centralindia"
    )
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    speech_recognizer.recognizing.connect(analyse)
    speech_recognizer.session_started.connect(lambda _: print("Voice engine active!"))
    speech_recognizer.canceled.connect(lambda _: print("API Failure"))
    speech_recognizer.session_stopped.connect(stop_cb)
    speech_recognizer.start_continuous_recognition()
    launch_game(game)
    while not done:
        time.sleep(0.5)


def analyse(evt):
    word = evt.result.text
    print(word)
    if "left" in word:
        left()
    if "right" in word:
        right()
    if "forward" in word or "straight" in word:
        forward()
    if "stop" in word:
        stop()
    if "jump" in word:
        jump()
    if "fly" in word:
        for _ in range(2):
            jump()
    if "creative" in word or "immortal" in word:
        creative()
    if "survival" in word or "normal" in word:
        survival()
    if "backward`" in word:
        look_back()
    if "day" in word:
        day()
    if "night" in word:
        night()
    if "quit" in word:
        print("Closing game")
        time.sleep(1)
        quit_command(game)
        print("See you next time !")
    if "attack" in word or "break" in word:
        break_block()
    if "place block" in word or "place" in word:
        place_block()


if __name__ == "__main__":
    start_speech_engine()
