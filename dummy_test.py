import threading
import time

def a():
    print("a0")
    time.sleep(2)
    print("a1")
    threading.Thread(target=b).start()
    time.sleep(3)
    print("a2")

def b():
    print("b0")
    time.sleep(2)
    print("b1")
    threading.Thread(target=c).start()
    time.sleep(3)
    print("b2")

def c():
    print("c0")
    time.sleep(2)
    print("c1")
    threading.Thread(target=a).start()
    time.sleep(3)
    print("c2")

threading.Thread(target=a).start()