import prompt
import random
def game():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('What is the result of the expression?')
    i = 0
    end = 0
    while i < 20:
        number1 = random.randint(1,10 )
        number2 = random.randint(1,10) 
        sum = number1 + number2 
        sum_game = str(number1) + ' + ' + str(number2)
        subtraction = max(number1,number2) - min(number1,number2)
        multiplication = number1 * number2
        multiplication_game = str(number1) + ' * ' + str(number2)
        subtraction_game = str(max(number1,number2)) + ' - ' + str(min(number1,number2))
        chois = random.randint(1,3)
        if chois == 1:
            game = sum_game
        if chois == 2:
            game = subtraction_game
        if chois == 3:
            game = multiplication_game
        if game == sum_game:
            answer = sum
        if game == subtraction_game:
            answer = subtraction
        if game == multiplication_game:
            answer = multiplication
        print('Question: ' + game)
        ans = prompt.string('Your answer: ')
        if str(answer) == str(ans):
            end += 1
            print('Correct!')
        if str(answer) != str(ans):
            return print(str(ans) + ' is wrong answer ;(. Correct answer was ' +  str(answer) + '.'"\nLet's try again," + name + '!')
        if end == 3:
            return print('Congratulations, ' + name + '!')
        i += 1
