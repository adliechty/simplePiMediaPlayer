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
```sudo raspi-config```
select System Options
select S1 Wireless LAN to configure WIFI
Go through prompts
Configure Localization Options --> Locale and Localization options -> Keyboard
System Options -> Auto login
if asked to reboot, reboot
```ping www.google.com```
if success (says 64 bytes from ...", WIFI is setup
```ctrl-c```

# Update Package manager
```sudo apt-get udpate```
   - Takes a few min
```sudo apt-get upgrade```
   - Takes more than a few min, less than an hour
```
# Install Git
sudo apt install git

# Install omxplayer from source as no longer supported with apt install :(

# setup keyboard layout
"""sudo dpkg-reconfigure keyboard-configuration"""
go through menus
```setupcon```
This did not work :(

