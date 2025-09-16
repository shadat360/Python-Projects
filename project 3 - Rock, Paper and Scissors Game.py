import random

choices = ('r','p','s')
emojis = {'r': '🪨','p':'🗞️','s' :'✂️'}

while True:
 user_choice = input('Rock, paper or scissors? (r/p/s):' ).lower()
 if user_choice not in choices:
    print('Invalid choice!')
    continue

 computer_choice = random.choice(choices)

 print(f'you chose {emojis[user_choice]}')
 print(f'computer chose {emojis[computer_choice]}')

 if user_choice == computer_choice:
    print('Tie!')
 elif(
 (user_choice == 'r' and computer_choice == 's') or
 (user_choice == 'p' and computer_choice == 'r') or
 (user_choice == 's' and computer_choice == 'p')
 ):
    print('Congratulations! you won.')

 else: 
  print('Sorry! you lose.')

 while True:
    should_continue = input('Continue? (y/n): ').lower()
    if should_continue == 'y':
        break  
    elif should_continue == 'n':
        print("Thanks for playing!")
        exit()
    else:
        print("Invalid input! Please enter 'y' or 'n'.")
 
 