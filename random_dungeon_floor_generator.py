import random

#defining floors

def floor0():
    print("f0. So you want to proceed to the Dungeon. Only a few humans have survived and the remains the of the dead have become enemies that were forced by Necron the Lord of the Necromancy into these dungeuns. I have one word to tell you; be careful")
def floor1():
    print("f1")
def floor2():
    print("f2")
def floor3():
    print("f3")
def floor4():
    print("f4")
def floor5():
    print("f5")
def floor6():
    print("f6")
def floor7():
    print("f7")

#random floor code

floornumber = random.randrange(0, 7)

#the print text for the floor that you end up in

if int(floornumber) == 0:
    floor0()

elif int(floornumber) == 1:
    floor1()

elif int(floornumber) == 2:
    floor2()

elif int(floornumber) == 3:
    floor3()

elif int(floornumber) == 4:
    floor4()

elif int(floornumber) == 5:
    floor5()

elif int(floornumber) == 6:
    floor6()

elif int(floornumber) == 7:
    floor7()

#Simeon, Thomas, Zac and Jaiden Productions