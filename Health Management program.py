
import time
from datetime import datetime
from pygame import mixer

def musicloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        user_responce = input()
        if user_responce == stopper:
            mixer.music.stop()
            break

def log_info(msg):
    with open("log.txt","a") as f:
        f.write(f"{msg}{datetime.now()}\n")

def water():
    print(time.sleep(3))
    musicloop("water.mp3","stop")
    log_info("water Drank at: ")

def eyes():
    print(time.sleep(6))
    musicloop("eyes.mp3","done")
    log_info("eyses exercise done at: ")

def exercise():
    print(time.sleep(10))
    musicloop("exercise.mp3","done")
    log_info("Physical exercise done at: ")


while True:
    water()
    eyes()
    exercise()
