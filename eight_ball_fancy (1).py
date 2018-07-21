import random
import sys

while True:
    userQuestion = input("What is your question? enter q to quit ")
    response = random.randint(1, 5)

    if userQuestion == "q":
        sys.exit()


    if response == 1:
        print ("It is certain.")

    if response == 2:
        print ("Ask again later")

    if response == 3:
        print ("My sources say no")

    if response == 4:
        print ("Yes, definitely")

    if response == 5:
        print ("Very doubtful")
