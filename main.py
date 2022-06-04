import random
import time

score = 100

def correct():
    int(score) + 10

def incorrect():
    int(score) - 20
    

def afl1_puzzle():
    print("The Addition Puzzle")
    print("In this puzzle you will be given two numbers and you need to complete the calculation that is given. If your answer is correct you pass the puzzle however if you get it incorrect you will fail the puzzle.")
    number_random = random.randrange(1, 90)
    print("What is " + str(number_random) + " + " + str(number_random) + " ?")
    answer = int(number_random) * 2
    answer_2 = input("Answer: ")

    if int(answer_2) == int(answer):
        print("Correct!")
        print("Puzzle Completed")
        correct()
        time.sleep(2)
        print("")

    else:
        print("Incorrect!")
        print("Puzzle Failed")
        incorrect()
        time.sleep(2)
        print("")

afl1_puzzle()