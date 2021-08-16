from timeit import default_timer as timer
import math
userInput = int(input("Choose a 10 digit passcode"))


start = timer()
for i in range(1, 100000000):

    if i == userInput:

        print("PASSWORD HACKED " + str(i))
        break
end = timer()
timetaken = end-start
print(str(round(timetaken, 2)) + " seconds taken")
if timetaken>60:
    print(math.floor(timetaken/60) + " minutes " + timetaken%60 + " seconds")



