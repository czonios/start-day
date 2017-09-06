# Start My Day Script

## Overview

This repository contains a script, written in Python, that I run when I sit at my computer every morning in order to automate opening some browser tabs to check out and play some music while I drink my morning coffee. I added a small bash script in my /bin (the instructions are to create another /bin in your home folder for safety) so I can run it just by opening a terminal (Ctrl+Alt+T), typing `start-day` and pressing Enter.

## Dependencies

  * Python 3
  * Git

## Set up (Linux)

### Contents of this repository

  * The script `PyAutomate.py` is a Python script that does all the work. I encourage you to tailor it to your needs, make it open your favorite email client, music player etc. For me, I just want to open some tabs.
  * The -optional- shell script `start-day` is used to run the Python script from anywhere, by typing `start-day` in your terminal .

### Downloading the scripts

  * Open a terminal, and type the following commands (the first one is optional)
        ```bash
	cd /path/to/desired/location/
	git clone 'https://github.com/czonios/start-day
	cd start-day
	```
  * At this point you might want to open the Python file in your favorite text editor and change a couple things in order to make it suit you.

### (Optional) Adding a shell script to run from anywhere
 
  * It is bad practice to put stuff you make/download in your OS's `/bin` folders. Instead, we are going to make our own, in our Home directory (or anywhere you like). Here's how to do that, assuming you're in the `start-day` directory:
	```bash
	mkdir ~/bin
	cp start-day ~/bin
	```
  * Add this line to your PATH
  	`export PATH=$PATH:~/bin`

  * Now let's make the script executable:
  	```bash
	cd ~/bin
	sudo chmod +x start-day
	```
  * Feel free to edit start-day in your favorite text editor and change the path to the Python file according to where you put it.

### Executing

  * If you followed the optional step, executing is as simple as opening a terminal and running `start-day`.

  * If not, you have to navigate to the folder containing `PyAutomate.py` and run `python3 PyAutomate.py`
