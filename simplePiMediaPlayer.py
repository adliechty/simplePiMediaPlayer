import RPi.GPIO as GPIO
import subprocess

#############################################################
# Functions
#############################################################

#############################################################
# Classes
#############################################################
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

    def button_callback(self, channel):
        print("Button " + str(channel))


player = simplePiMediaPlayer(5, 6, 13, 19, 26)


#subprocess.run(["omxplayer", "/home/pi/bigbuckbunny_30sclip.mp4"])
