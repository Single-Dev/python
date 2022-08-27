import threading as thr

def myfun():
    for x in range(99):
        print('Hello')

def myFun1():
    for x in range(99):
        print("hi")
        

text1 = thr.Thread(target=myfun)
text = thr.Thread(target=myFun1)

text.start()
text1.start()
