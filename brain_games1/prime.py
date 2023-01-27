import prompt
import random
def game():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if given number is prime. Otherwise answer "no"')
    i = 0
    end = 0   
    while i < 20:
        random_number = random.randint(2,10)
        for i in range(2, int(random_number/2)+1):
            if (random_number % i) == 0:
                answer = 'no'
                break
            else:
                answer = 'yes'
        else:
            answer = 'yes'
        print('Question: ' + str(random_number))
        ans = prompt.string('Your answer: ')          
        if answer == ans:
            end += 1
            print('Correct!')
        if answer != ans:
            return print(str(ans) + ' is wrong answer ;(. Correct answer was ' +  str(answer) + '.'"\nLet's try again," + name + '!')
        if end == 3:
            return print('Congratulations, ' + name + '!')
        i += 1
