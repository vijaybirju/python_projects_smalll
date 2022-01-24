#generate random number by compter
#guess number by me 
#check condition and print out put
'''alogorithm
1. Genrate a random number from a specific no
2. Take input from user(which is actually guess(variable))
3. Check whether input belongs to generated number. If YES then apply  loop to check again and again our guess is right/wrong. If NO then print guess is out of range
4. If guess is smaller


'''
import random
#make variable to pass from function
guess=0

def guess_number(guess):
    number = random.randint(2,500) #genrate random number
    while guess != number:#loop until right guess
        guess=int(input("guess the number"))
        if guess<number:
            print("Number is too small")
        else:
            print("Number is too big")
    return f"yea you guess correct number {guess}"


print(guess_number(guess)) #use print statement to call funtion so that return get printed 

