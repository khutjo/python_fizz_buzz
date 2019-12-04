#!/usr/bin/python

count = 1;

def fectorOfFive(count):
    if count % 5 == 0:
        return True
    else:
        return False

def fectorOfThree(count):
    if count % 3 == 0:
        return True
    else:
        return False

def chooseaction(count):
    three = fectorOfThree(count)
    five = fectorOfFive(count)
    
    if three and five:
        print("FizzBuzz " + str(count))
    elif three:
        print("Buzz " + str(count))
    elif five:
        print("Fizz " + str(count))
    else:
        print(count)


while count <= 100:
    chooseaction(count)
    count = count + 1
