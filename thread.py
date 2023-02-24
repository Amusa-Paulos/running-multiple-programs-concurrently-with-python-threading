#####################################################################################################
################### The script I used for demo at the start of the video  ###########################
#####################################################################################################
import threading, time
def f1():
    for i in range(1,20):
        time.sleep(1)
        print('fun 1:: hello from f1 ', i)


def f2():
    for i in range(1,20):
        time.sleep(1)
        print('fun 2:: hello from f2 ', i)


def f3():
    name = input('Enter your name')
    print('your name is', name)


th1 = threading.Thread(target=f1).start()
th2 = threading.Thread(target=f2).start()
th2 = threading.Thread(target=f3).start()