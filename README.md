# About
A program that automatically logs you into any current game made by Riot Games. This includes League of Legends, Legends of Runeterra and Valorant.
# Installation process
Here's a step-by-step guide on how to install this program.

First execute all of these commands in your command line, one by one:
* `pip install pyperclip`
* `pip install cryptography`
* `pip install pywin32`
* `pip install pyautogui`

Now download or clone the files from GitHub and put them in their own folder where you want to store them.
If you downloaded a zip, make sure to extract it, otherwise you may run into storage permission issues.

You can run the program by running `AutoLogin.pyw`.
If the extension `.pyw` seems strange, it's used to hide the console window when using a GUI.
It can be run with normal Python. No need to install anything else.
More on that here: https://stackoverflow.com/questions/34739315/pyw-files-in-python-program

I recommend you make an easy way for yourself to execute the program, like a desktop shortcut or a taskbar icon.

**That's it!**
# How to use
Video instructions: https://youtu.be/W8Rf1t9zEp0
For the program to log you in, you need to have the Riot Client open on your PC. I can be in the background, but it has to be opened.
After entering accounts in the program, choose the account you want to log into. Make sure Riot Client sign-in is open. Just select the account from the listbox on the left and press confirm. The program will bring Riot Client to the surface and log in. Make sure you don't move your mouse while the program is logging in, since you can mess up it's mouse movements. Also don't move the Riot Client window.
# Recommended settings
It's recommended to use 1920x1080 monitor resolution when using the app, since some values are set as flat values and don't use coefficients.
If you have trouble with this, you can change the values in `login.py`'s `parse_values` function.
If you have multiple monitors, it will only work if the Riot Client is on the main monitor.
The program was created on Python 3.8.5, so that's the known-to-work version.
# Prerequisites
There are prerequisites for the program to work. It needs these modules:
  -[pyperclip](https://pypi.org/project/pyperclip/)
  -[cryptograpy](https://pypi.org/project/cryptography/)
  -[pywin32](https://pypi.org/project/pywin32/)
  -[pyautogui](https://pypi.org/project/PyAutoGUI/)
