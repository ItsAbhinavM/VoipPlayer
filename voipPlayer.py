import pygetwindow as pw
import pyautogui as pg
import time
import speech_recognition as sr

keymap = {"forward": "w", "backward": "s", "left": "a", "right": "d", "jump": "space"}
X_OFFSET = 100


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


import speech_recognition as sr
import json

s = sr.Recognizer()
with sr.Microphone() as source:
    print("Calibrating...")
    s.adjust_for_ambient_noise(source)
    print("Calibration Complete!")
    activate_window("Minecraft")
while True:
    with sr.Microphone() as source:
        audio = s.listen(source, phrase_time_limit=1)
    try:
        word = json.loads(s.recognize_vosk(audio))["text"]
        if "l" in word:
            mouse_left()
        if "right" in word:
            mouse_right()
        if "forward" in word:
            forward()
        if "stop" in word:
            stop()
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Google Speech Recognition could not understand audio")
