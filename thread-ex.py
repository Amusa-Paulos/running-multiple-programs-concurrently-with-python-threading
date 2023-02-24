import threading
example = 'hello'
def f1():
    for i in range(1,5):
        print('hello from f1 ', i)


def f2(*argz, sepr):
    print('number from agz ', sepr.join(map(str, argz)))
    # for i in range(1,5):
    #     print('hello from f2 ', i)

# group, target, name, args, kwargs, daemon
# join method
# is_alive method
th1 = threading.Thread(target=f1, name='first thread', daemon=True)
th2 = threading.Thread(target=f2, name='second thread', args=[2,3,4,5,6, 'hello'], kwargs={'sepr': ','})
th1.start()
# print('is th1 still alive ', th1.is_alive())
th2.start()
print('is th1 a daemon ', th1.daemon)
# th2.join() # until th2 terminates
# print(th1.name)
# print(th2.name)
# print('is th1 still alive', th1.is_alive())
print('this is on the main thread')
