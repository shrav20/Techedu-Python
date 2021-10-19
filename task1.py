import random
import math
low=int(input("enter lower bound - "))
up = int(input('enter upper bound - '))
#generated random no. between up and low
x = random.randint(low,up)
print("\n only", round(math.log(up -low + 1, 2)),"chances are granted to guess\n")
ct = 0
while ct<math.log(up-low + 1, 2):
    ct += 1
    guess=int(input("Guess a number -"))
    if x ==guess:
        print("congratulations!")
        break
    elif x>guess:
        print("number is small , please try again!!")
    elif x<guess:
        print("number is high , please try again!!")
if ct >math.log(up - low + 1,2):
    print("\n the number was ",x)
