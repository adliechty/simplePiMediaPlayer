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
```
sudo apt-get udpate
```
   - Takes a few min
```
sudo apt-get upgrade
```
   - Takes more than a few min, less than an hour
# Install Git
```
sudo apt install git
```

# Install omxplayer
```
sudo apt install omxplayer
wget https://files.pimylifeup.com/omxplayer/bigbuckbunny_30sclip.mp4
omxplayer bigbuckunny_30sclip.mpf
```

# Install usb mount
```
wget https://github.com/nicokaiser/usbmount/releases/download/0.0.24/usbmount_0.0.24_all.deb
sudo dpkg -i usbmount_0.0.24_all.deb
```
auto mounts a USB drive when plugged in.
Must get latest version from github, otherise USB doesn't get auto detected as automount is supposed to do.

# Install python3
```
sudo apt install python3
sudo rm /usr/bin/python
sudo ln -s /usr/bin/python3 /usr/bin/python
sudo apt install python3-pip
```

# clone this repository
mkdir Git
cd Git
git clone https://github.com/adliechty/simplePiMediaPlayer.git
cd simplePiMediaPlayer

# Using a USB gamepad to control the media player
```
pip3 install evdev
```
add this:
KERNEL=="uinput", MODE="0666
to top of
/etc/udev/rules.d/99-com.rules (or whatever .rules is in there)
run sudo udevadm control --reload-rules && sudo udevadm trigger

# Modify .bashrc to set program as startup
```
sudo nano /home/pi/.bashrc
```
add

\#The following is needed to get a gamepad to work with python evdev
sudo udevadm control --reload-rules && sudo udevadm trigger
sudo modprobe uinput
\#Sleep added to wait for uinput to be loaded
sleep 5
\# The following program maps gampad keys to keyboard keys
python /home/pi/Git/simplePiMediaPlayer/mapControllerToKeys.py /dev/input/event3 &
\# simple Media Player
python /home/pi/Git/simplePiMediaPlayer/simplePiMediaPlayer.py

