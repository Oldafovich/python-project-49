import prompt
import random


def game():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    end = 0
    while i < 20:
        number = random.randint(1, 100)
        print('Question: ' + str(number))
        ans = prompt.string('Your answer: ')
        if number % 2 == 0:
            answer = 'yes'
        if number % 2 != 0:
            answer = 'no'
        if answer == ans:
            end += 1
            print('Correct!')
        if answer != ans:
            return print(ans + ' is wrong answer ;(. Correct answer was ' + answer + '.'"\nLet's try again," + name + '!')
        if end == 3:
            return print('Congratulations, ' + name + '!')
        i += 1
