import random
playing =True
number = str(random.randint(1,10))
print("i will generate a nimber from 10 to 20, you to guess the number one digit at a time.")
print("the game ends when you get 1 hero!")
while playing:
    guess = input("give me your best guess! \n")
    if number == guess:
        print("you win the game")
        print("the number was", number)
        break
    else:
        print("your guess isnt right,  try again. \n")