import random
print("1:Stone, 2:Paper, 3:Scissors\n")

uscore = 0
cscore = 0

for _ in range(1,6):

    try:
        user = int(input("Choose Your Option: "))

    except ValueError:
        print("Please enter a number.")
        continue
        
    com = random.randint(1,3)

    if user < 1 or user > 3:
        print("Wrong Input, Give Me Correct Input.")
        continue

    elif user == 1 and com == 3:
        print("You Won The Round.\n")
        uscore += 1

    elif user == 2 and com == 1:
        print("You Won The Round.\n")
        uscore += 1

    elif user == 3 and com == 2:
        print("You Won The Round.\n")
        uscore += 1

    elif user == com:
        print("This Round Is Draw.\n")

    else:
        print("Computer Won The Round.\n")
        cscore += 1

    print(f"Your Current Score: {uscore}\tComputer Current Score: {cscore}\n")


if uscore == cscore:
    print("This Game Is Draw Between You And Computer.😑")

elif uscore > cscore:
    print("Congratulations, You Won This Whole Game.🥳🎉")

else:
    print("Computer Won This Whole Game.😈")