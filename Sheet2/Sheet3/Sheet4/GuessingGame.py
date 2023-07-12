from random import randint
number = randint(1,1000)
question = ("What number do you wanna guess?")
print("I have chosen a number from 1 through 1000 try to guess which number I guessed!")
guess = 0 
amountofguesses = 0

while True:
    guess = (int(input(question)))
    if guess < number:
        print("The number you have guessed is higher than that")
        amountofguesses = amountofguesses +1
    elif guess > number:
        print("The number that you have guessed is lower than that")
        amountofguesses = amountofguesses +1 
        print("The total amount that you guessed is " +  str(amountofguesses))
    elif guess == number: 
        print("Correct!" + amountofguesses)
        break
         