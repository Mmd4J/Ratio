# Gratio 
**WARNING:** this is an educational project to create a rat which has a control panel in discord and **does not mean** to harm someone. so I do not accept any complains about what you do. 

Welcome. gratio is a discord rat which would have a control panel on discord with a bot.
the installation process is really easy and will be explained detail by details so you do not need to be worried.

## Requirements
* python 3.10 or better
* others are listed in requirements.exe use `pip install -r requirements.txt ` to install them all

## Installation
**Step 1:** Download the source code and extract it to a new folder with a name of your own taste.

**Step 2:** Install the required dependencies including python 3.10(to install other deps you can use `pip install -r requirements.txt `).

**Step 3:** You now have to modify the source code and enter your own token and guild id. the token is located on main.py line 20 which should be replaced with your discord bot token and the guild id should be replaced in main.py line 21.

**Step 4:** the script is now ready to work you now can use 
```python3 main.py``` to run the script and see if it works.

**Step 5 (Optional):** There is an optional way too which will let you to compile the script to .exe using PyInstaller.
`pip install PyInstaller` i'd also suggest you to install auto-py-to-exe too which is basically PyInstaller but with GUI `pip install auto-py-to-exe`.
and then after all you can compile your script to exe by typing autopytoexe.exe in your cmd or either terminal.

## The Structure
To keep it simple the rat would be only acting as a discord bot in the target's computer and will listen to you while you're entering a command and executes that for you.
the code is yet not clean but i'd clean it

## Commands
```
!speak hello: say's hello
!error title
subtitle: shows an error with the specified title and subtitle.
!blockinput: blocks windows input (REQUIRES ADMINISTRATOR)
!shutdown: force shutdowns the target
!restart: force restarts the target
!execute command args: executes windows CMD commands supports args too.
!webcam: sends a picture from the targets' webcam
!browser url: opens a new tab and goes to the specified url.
```

**This rat will only work on windows 10 or higher!
Feel free to contribiute on the rat to make it better!**