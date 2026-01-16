import threading

def task1():
    print("Thread 1 is running")
t1=threading.Thread(target=task1)
t2=threading.Thread(target=task1)
t1.start()
t2.start()
t1.join()
t2.join()
print("Main thread ends")