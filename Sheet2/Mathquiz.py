from random import randint
right = 0
x = int(input('Tell me how many question you want to solve? '))
for x in range(x):
    num1 = randint(1, 20)
    num2 = randint (1, 20)
    question = "What is " + str(num1) + " times " + str(num2) + "? "
    answer = int(input(question))
    product = num1 * num2
    if answer == product:
        print('Yes, the answer is ' + str(product) + '!')
        print('Well done you answered correctly!')
        right = right +1
    else:
        print('Sorry that is incorrect!')
        print('The correct answer is ' + str(product) + '.')
x = x + 1
print(" I asked you "  + str(x)  + "questions. You got " + str(right) + ".")
print("Well done!")

