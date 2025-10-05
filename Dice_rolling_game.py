# PLAN THE LOOP
import random

while True:
    # Ask user questions: Roll dice?
    # so that it can accept both uppercase and lowercase y/n
    choice = input('Roll the dice? (y/n): '). lower()
# if user enter y
    if choice == 'y':
        # generate two random numbers between 1 and 6
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
    # print the numbers

        print(f'You rolled a {dice1} and a {dice2}.')

# if user enter n,
    elif choice == 'n':  # print thank you message
        print('Thank you for playing the game!')
        break
    # terminate the loop
    else:
        # print error - invalid Choice
    print('Invalid choice. Please enter y or n.')
