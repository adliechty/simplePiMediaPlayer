import sys
import evdev
from evdev import ecodes as e

#xboxdrv was not working well, so made it in python instead
#This code maps a code from an input device such as a USB game controller to a keyboard key
#THis is mainly so that either a keyboard or gamepad can be used for the same program
#and that program does not have to write code to support both a keybard and a gamepad.

SNES_X     = 288
SNES_A     = 289
SNES_B     = 290
SNES_Y     = 291
SNES_SEL   = 296
SNES_START = 297

#keypad gets a value of 0 for left, 127 for not pushed, and 255 for right
SNES_LEFT_RIGHT = 0
#keypad gets a value of 0 for up, 127 for not pushed, and 255 for down
SNES_UP_DOWN    = 1

print("first argument specifices device...eg /dev/input/event3")
device = evdev.InputDevice(sys.argv[1])

with evdev.uinput.UInput() as ui:
    for event in device.read_loop():
        if event.type == e.EV_KEY:
            #print("Button:")
            #print(evdev.categorize(event))
            #print(event.code)
            #print(event.type)
            #print(event.value)
            if event.code == SNES_X:
                ui.write(e.EV_KEY, e.KEY_Q, event.value)
            if event.code == SNES_Y:
                ui.write(e.EV_KEY, e.KEY_H, event.value)
            if event.code == SNES_SEL:
                ui.write(e.EV_KEY, e.KEY_S, event.value)
            elif event.code == SNES_START:
                ui.write(e.EV_KEY, e.KEY_SPACE, event.value)
            ui.syn()

        elif event.type == e.EV_ABS:
            if event.code == SNES_LEFT_RIGHT:
                if event.value == 0:
                    ui.write(e.EV_KEY, e.KEY_LEFT, 1)
                elif event.value == 255:
                    ui.write(e.EV_KEY, e.KEY_RIGHT, 1)
                elif event.value == 127:
                    ui.write(e.EV_KEY, e.KEY_LEFT, 0)
                    ui.write(e.EV_KEY, e.KEY_RIGHT, 0)
            elif event.code == SNES_UP_DOWN:
                if event.value == 0:
                    ui.write(e.EV_KEY, e.KEY_UP, 1)
                elif event.value == 255:
                    ui.write(e.EV_KEY, e.KEY_DOWN, 1)
                elif event.value == 127:
                    ui.write(e.EV_KEY, e.KEY_UP, 0)
                    ui.write(e.EV_KEY, e.KEY_DOWN, 0)
            ui.syn()


        #print("type:" + str(event.type))
        #print(event)
        #ui.write(e.EV_KEY, e.KEY_A, 1)
        #ui.syn()
