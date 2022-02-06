import sys
import evdev
from evdev import ecodes as e
import RPi.GPIO as GPIO
import time

class simplePiMediaPlayer:
    def __init__(self, UP, DOWN, LEFT, RIGHT, PLAY):
        self.UP    = UP
        self.DOWN  = DOWN
        self.LEFT  = LEFT
        self.RIGTH = RIGHT
        self.PLAY  = PLAY
        self.ALLPINS = [UP, DOWN, LEFT, RIGHT, PLAY]

        #Configure GPIO Pins
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        for pin in self.ALLPINS:
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.add_event_detect(pin, GPIO.BOTH, callback=self.button_callback)

        self.ui = evdev.uinput.UInput():

    def button_callback(self, channel):
        print("Button " + str(channel))
        if channel == self.UP:
            print("UP")
            ui.write(e.EV_KEY, e.KEY_UP, GPIO.input(self.UP))
        elif channel == self.DOWN:
            print("DOWN")
            ui.write(e.EV_KEY, e.KEY_DOWN, GPIO.input(self.DOWN))
        elif channel == self.LEFT:
            print("LEFT")
            ui.write(e.EV_KEY, e.KEY_LEFT, GPIO.input(self.LEFT))
        elif channel == self.RIGHT:
            print("RIGHT")
            ui.write(e.EV_KEY, e.KEY_RIGHT, GPIO.input(self.RIGHT))


player = simplePiMediaPlayer(5, 6, 13, 19, 26)
while True:
    time.sleep(1)
