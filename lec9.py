import threading
import time

def func(num):
    for i in range(10,0,-1):
        print(f'thread {num}: ', i)
        time.sleep(1)

thr1 = threading.Thread(target = func, args = (1,)).start()
thr2 = threading.Thread(target = func, args=(2,)).start()
