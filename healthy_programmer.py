# 9.00 am - 5.00pm
# Water (3.5 litres water have to drink) - water.mp3 - play every 40 mins -to stop the music type -
# drank - then save this as a log.
# Eyes - eyes.mp3 - play every 20 mins - to stop the music type - done - then save this as a log.
# Physical activity - physical.mp3 - play every 60 mins - to stop the music type - done - then save this as a log.
# Pygame module to play audio

from pygame import mixer
from datetime import datetime
from time import time


def drink_water(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break


def eye_exercise(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break


def physical_exercise(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break


def my_fitness_log(message):
    with open("my_fitness_log.txt", "a") as f:
        f.write(f"{message}, {datetime.now()}\n")


if __name__ == '__main__':
    water = time()
    eyes = time()
    exercise = time()
    watertime = 2400
    eyetime = 1200
    exetime = 3600

    while True:
        if time() - water > watertime:
            print("Time to drink some water! Enter 'drank' to stop the alarm.")
            drink_water("drink.mp3", "drank")
            water = time()
            my_fitness_log("Drank water at")

        if time() - eyes > eyetime:
            print("Time for some eye exercise! Start rolling your eyes. Enter 'done' to stop the alarm.")
            eye_exercise("eyes.mp3", "done")
            eyes = time()
            my_fitness_log("Done eye exercise at")

        if time() - exercise > exetime:
            print("Time to do some physical exercise! Get up from you seat and start jumping"
                  " Enter 'done' to stop the alarm.")
            physical_exercise("exercise.mp3", "done")
            exercise = time()
            my_fitness_log("Done physical exercise at")


