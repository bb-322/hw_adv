import os
import time
import threading


def file_deletion(file, event2):
    while True:
        event2.wait()
        if os.path.exists(file):
            os.remove(file)
            event2.clear()
            break
        else: pass

def text_finder(file, event, event2):
    global data
    while True:
        event.wait()
        with open(file, 'r') as f:
            data = f.read()
        if 'Wow!' in data:
            event2.set()
            event.clear()
        else: time.sleep(5)

def file_finder(file, event):
    while True:
        if os.path.exists(file):
            if not event.is_set():
                event.set()
        else:
            if event.is_set():
                event.clear()
        time.sleep(5)

event = threading.Event()
event2 = threading.Event()
filename = '853890451.txt'

t1 = threading.Thread(target=file_finder, args=(filename, event))
t2 = threading.Thread(target=text_finder, args=(filename, event, event2))
t3 = threading.Thread(target=file_deletion, args=(filename, event2))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()