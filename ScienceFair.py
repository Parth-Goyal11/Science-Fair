from timeit import default_timer as timer
import math
import random
from numba import jit, cuda, f8, uint8, uint32

import numpy as np





userInput = (input("Choose a passcode"))
passwordIteration = " "
broken = False
bruteForce = True
characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                  "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                  "l", "m", "n", "o", "p", "q", "r", "s", "t", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3",
                  "4", "5", "6", "7", "8", "9", "0"]
start = timer()
if (bruteForce):
    with open('10-million-combos.txt', 'r') as combos:
        for line in combos:
            if bruteForce == False:
                break
            for word in line.split():
                if word == userInput:
                    print(">>>>>>>>>DICTIONARY ATTACK SUCCESSFUL<<<<<<<<<<")
                    print("PASSWORD HACKED " + "by dictionary")
                    bruteForce = False
                    break
        if bruteForce == True:
            print("Attack Failed")
if (bruteForce):
    for a in characters:
        if broken:
            break
        for b in characters:
            if broken:
                break
            for c in characters:
                if broken:
                    break
                for d in characters:
                    passwordIteration = a + b + c + d  #Add for loops depending on passcode length
                    if passwordIteration == userInput:
                        print("PASSWORD HACKED " + str(passwordIteration))
                        broken = True
                        break
end = timer()
timetaken = end - start
print(str(round(timetaken, 2)) + " seconds taken")
if timetaken > 60:
    print(math.floor(timetaken / 60) + " minutes " + timetaken % 60 + " seconds")




