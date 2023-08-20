import random

while True:
    my_answer = input('Choose: Rock, Paper or Scissors: ').lower()

    if my_answer == 'quit':
        break

    # if my_answer !='rock' and my_answer !='paper' and my_answer != 'scissors':
    #     print('Please choose correct answer!')
    #     continue
    if my_answer not in ['rock', 'paper', 'scissors']:
        print('Please choose correct answer!')
        continue


    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print(f'The computer choice is: {computer_choice}')

    if my_answer == computer_choice:
        print('Its a draw!!')
    elif (my_answer == 'paper' and computer_choice == 'rock') or (my_answer == 'rock' and computer_choice == 'scissors') or (my_answer == 'scissors' and computer_choice == 'paper'):
        print('You WON!!!')
        break
    # elif my_answer == 'rock' and computer_choice == 'scissors':
    #     print('You WON!!!')
    #     break
    # elif my_answer == 'scissors' and computer_choice == 'paper':
    #     print('You WON!!!')
    #     break
    else:
        print('You LOST!!')
