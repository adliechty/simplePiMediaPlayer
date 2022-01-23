import RPi.GPIO as GPIO
import subprocess
import time
import os
import curses

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
        self.curDir = "/media/usb0"
        self.curSelection = 0
        self.done = False

        self.key = ""
        # create curses window (blank screen with text)
        self.win = curses.initscr()
        curses.curs_set(0); # turn off blinking cursor
        self.win.keypad(True)
        self.win.nodelay(False)
        self.win.clear()
        self.updateSelection()
        while (1):
          key = self.win.getch()
          self.process_press(key)
          if self.done:
              break
        curses.endwin()


    def updateSelection(self):
        self.win.clear()
        self.win.addstr("simple media player.  Push h for help\n")
        self.win.addstr("-----------------------------\n")
        self.win.addstr(self.curDir + "\n")
        self.win.addstr("-----------------------------\n")
        i = 0
        for f in os.listdir(self.curDir):
            if i == self.curSelection:
                self.win.addstr("****" + f + "\n")
            else:
                self.win.addstr("    " + f + "\n")
            i = i + 1

    def process_press(self, key):
        self.key = key
        if key == curses.KEY_UP:
            if self.curSelection > 0:
                self.curSelection -= 1
        elif key == curses.KEY_DOWN:
            if self.curSelection < len(os.listdir(self.curDir)) - 1:
                self.curSelection += 1
        elif key == curses.KEY_LEFT:
            self.curDir = os.path.dirname(self.curDir)
            self.curSelection = 0
        elif key == curses.KEY_ENTER or key == curses.KEY_RIGHT:
            files = os.listdir(self.curDir)
            selFile = self.curDir + "/" + files[self.curSelection]
            if os.path.isfile(selFile):
                proc = subprocess.run(["omxplayer", selFile])
                #Flush any keys pushed while player was open, don't use for navigation
                curses.flushinp()
            elif os.path.isdir(selFile):
                self.curDir = selFile
                self.curSelection = 0
        elif key == ord('q'):
            self.done = True
            return False
        elif key == ord('s'):
            self.done = True
            subprocess.run(["shutdown", "-P", "now"])
            return False
        elif key == ord('h'):
            self.win.addstr("\n")
            self.win.addstr("Navigate to a file or folder with up and down arrows\n")
            self.win.addstr("enter a folder with right arrow\n")
            self.win.addstr("select a folder with right arrow\n")
            self.win.addstr("return to parrent directory with left arrow\n")
            self.win.addstr("\n")
            self.win.addstr("When playing File:\n")
            self.win.addstr("Space to pause\n")
            self.win.addstr("Escape to exit\n")
            self.win.addstr("Arrow to navigate forward backward in video\n")
            return True

        self.updateSelection()


player = simplePiMediaPlayer(5, 6, 13, 19, 26)
