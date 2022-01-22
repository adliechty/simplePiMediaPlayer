import RPi.GPIO as GPIO
import subprocess
import time
from pynput import keyboard
from pynput.keyboard import Key
import os

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
        self.curDir = "/media/pi"
        self.curSelection = 0
        self.updateSelection()
        self.done = False

        #Configure GPIO Pins
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        for pin in self.ALLPINS:
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.add_event_detect(pin, GPIO.BOTH, callback=self.button_callback)

        subprocess.run(["stty", "-echo"])
        #We stop listening when starting the video so that video navigation does not affect file navigation.
        while self.done == False:
            with keyboard.Listener(on_press=self.on_press) as self.listener:
                self.listener.join()
        subprocess.run(["stty", "echo"])


    def updateSelection(self):
        os.system('clear')
        print("simple media player.  Push h for help")
        print("-----------------------------")
        print(self.curDir)
        print("-----------------------------")
        i = 0
        for f in os.listdir(self.curDir):
            if i == self.curSelection:
                print("    **" + f)
            else:
                print("    " + f)
            i = i + 1

    def on_press(self, key):
        #print("Key " + str(key))
      #try:
        if key == Key.up:
            if self.curSelection > 0:
                self.curSelection -= 1
        elif key == Key.down:
            if self.curSelection < len(os.listdir(self.curDir)) - 1:
                self.curSelection += 1
        elif key == Key.left:
            self.curDir = os.path.dirname(self.curDir)
            self.curSelection = 0
        elif key == Key.enter or key == Key.right:
            files = os.listdir(self.curDir)
            selFile = self.curDir + "/" + files[self.curSelection]
            if os.path.isfile(selFile):
                self.listener.stop()
                proc = subprocess.run(["omxplayer", selFile])
            elif os.path.isdir(selFile):
                self.curDir = selFile
                self.curSelection = 0
        elif key == Key.esc or key.char == ('q'):
            self.done = True
            return False
        elif key.char == ('s'):
            self.done = True
            subprocess.run(["shutdown", "-P", "now"])
            return False
        elif key.char == ('h'):
            print("Navigate to a file or folder with up and down arrows")
            print("enter a folder with right arrow")
            print("select a folder with right arrow")
            print("return to parrent directory with left arrow")
            print()
            print("When playing File:")
            print("Space to pause")
            print("Escape to exit")
            print("Arrow to navigate forward backward in video")
            return True
      #except:
      #  pass

        self.updateSelection()

    def button_callback(self, channel):
        print("Button " + str(channel))


player = simplePiMediaPlayer(5, 6, 13, 19, 26)

#while True:
    #print(str(GPIO.input(5)) + str(GPIO.input(6)) + str(GPIO.input(19)) + str(GPIO.input(26)))
#    time.sleep(1)


