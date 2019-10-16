import random

# please enter how many games you want to play
game = int(input("How many games"))
for i in range(game):
    # asking user a random number between 1-25
    randomnumber = random.randint(1,26)
    select = int(input("Select an number"))
    count = 0
    while(select != randomnumber):
        if(select > randomnumber0):
            print("Higher")
            count = count + 1
        else:
            print("Lower")
            count = count + 1

    print("The number of attempts taken by you is:")
    print(count)

