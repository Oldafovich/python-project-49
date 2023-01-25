import prompt
import random
import math
def game():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Find the greatest common divisor of given numbers.')
    i = 0
    end = 0
    while i < 20:
        number1 = random.randint(1,10)
        number2 = random.randint(1,10)
        answer = math.gcd(number1, number2)
        print('Question: ' + str(number1) + ' ' + str(number2))
        ans = prompt.string('Your answer: ')
        if str(answer) == str(ans):
            end += 1
            print('Correct!')
        if str(answer) != str(ans):
            return print(str(ans) + ' is wrong answer ;(. Correct answer was ' +  str(answer) + '.'"\nLet's try again," + name + '!')
        if end == 3:
            return print('Congratulations, ' + name + '!')
        i += 1
