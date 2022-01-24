# simplePiMediaPlayer
A simple media player for rasberry pi.
Plays music and videos from a USB drive.

  - Rasberry Pi Zero
  - Portable HDMI display (I used adifruit 5in display)
  - USB HUB
  - USB conference speaker/microphone
  - USB power bank
  - USB in line power switch
  - Wood fence post
  - screws to mount

# Setting up your Rasberry Pi Zero
WARNING:  Use Raspberry pi lite *buster* as the newer bulsey does not support omx player.  I tried vlc player, but was having trouble getting command line arguments for that to work.  For example it did not return to command line terminal despite trying --play-and-exit and trying vlc://quit at the end.  So, omxplayer it is.

Install raspberry pi lite to SD card using raspberry PI imaging utility.
Insert SD card into pi zero
boot
login username: pi
password: rasberry

# Enable WIFI, keyboard layout
```sudo raspi-config
```
select System Options
select S1 Wireless LAN to configure WIFI
Go through prompts
Configure Localization Options --> Locale and 
Localization options -> Keyboard
System Options -> Auto login
if asked to reboot, reboot

# Update Package manager
```sudo apt-get udpate
```
   - Takes a few min
```sudo apt-get upgrade
```
   - Takes more than a few min, less than an hour
# Install Git
```sudo apt install git
```

# Install omxplayer
```sudo apt install omxplayer
wget https://files.pimylifeup.com/omxplayer/bigbuckbunny_30sclip.mp4
omxplayer bigbuckunny_30sclip.mpf
```

# Install usb mount
```wget https://github.com/nicokaiser/usbmount/releases/download/0.0.24/usbmount_0.0.24_all.deb
sudo dpkg -i usbmount_0.0.24_all.deb
```
auto mounts a USB drive when plugged in.
Must get latest version from github, otherise USB doesn't get auto detected as automount is supposed to do.

# Install python3
```sudo apt install python3
sudo rm /usr/bin/python
sudo ln -s /usr/bin/python3 /usr/bin/python
sudo apt install python3-pip
```

# clone this repository
mkdir Git
cd Git
git clone https://github.com/adliechty/simplePiMediaPlayer.git
cd simplePiMediaPlayer

# Modify .bashrc to set program as startup
sudo nano /home/pi/.bashrc
add
python /home/pi/Git/simplePiMediaPlayer/simplePiMediaPlayer.py

# Using a USB gamepad to control the media player
```sudo apt install xboxdrv
sudo apt install evtest
````
Above is used to map usb game pad to keyboard keys
Program uses, up, down, left, right, space, q, s, and h

ls /dev/input/event\*
evtest /dev/input/event1
evtest /dev/input/event2
do once for every event listed above.  Each time hit a key pad on controller to determine which controller is one to that event type.
Once found record what each button is.  Here is example for the super nintendo USB pad I had from iNNEXT on amazon:

ABX_X       left = 0 right = 255 center = 127
ABS_Y       up = 0 down = 255 center = 127
BTN_BASE4   0, 1    start
BTN_BASE3   0, 1    select
BTN_TOP     0, 1    Y
BTN_TRIGGER 0, 1  X
BTN_THUMB   0, 1  A
BTN_THUMB2  0, 1  B
BTN_TOP2    0, 1  top left
BTN_PINKIE  0, 1  top right
