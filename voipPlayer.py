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


def activate_window(title):
    game = pw.getWindowsWithTitle(title)[0]
    game.minimize()
    game.restore()
    screen_width, screen_height = pg.size()
    pg.moveTo(screen_width // 2, screen_height // 2)


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
                if "forward" in word:
                    forward()
                if "stop" in word:
                    stop()
                if "jump" in word:
                    jump()

            except sr.UnknownValueError:
                print("Failed to recognize speech")
            except sr.RequestError:
                print("Failed to access API, please check your internet connection")
