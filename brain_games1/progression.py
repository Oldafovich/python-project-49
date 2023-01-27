import prompt
import random
def game():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('What number is missing in the progression?')
    i = 0
    end = 0
    o = 0
    list = []
    random_number1 = random.randint(1,10)     
    while i <= 9:
        list.append(random_number1)
        random_number1 += 2
        i += 1
    while o < 20:
        random_number2 = random.randint(0,9)
        answer = list[random_number2]
        list[random_number2] = '..'
        str_number = (" ".join(map(str, list)))
        print('Question: ' + str_number)
        ans = prompt.string('Your answer: ')
        if str(answer) == str(ans):
            list[random_number2] = answer
            end += 1
            print('Correct!')
        if str(answer) != str(ans):
            return print(str(ans) + ' is wrong answer ;(. Correct answer was ' +  str(answer) + '.'"\nLet's try again," + name + '!')
        if end == 3:
            return print('Congratulations, ' + name + '!')
        i += 1

