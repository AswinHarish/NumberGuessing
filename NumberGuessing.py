import random

guess=random.randrange(1,9)
a=0
b=1
while a<=b:
    num=int(input("Enter a number between 1 and 10 : "))
    b+=1
    if guess==num:
        print("Hurray!! You've won :)")
    else:
        print("Wrong Guess :( , Please try again ")