import random

print("welcome to the game")
print("You have to guess the number between 1 to 50")
attempt=int(input("Enter the number of attempts you want: "))
print(f"You have to guess the number between 1 to 50 in {attempt} tries")

num=random.randint(1,50)

j=2

for i in range(attempt-1,0,-1):
    num1 = int(input("Enter the number: "))
    if num1==num:
        print("Congrats Your guess is right")
        break
    elif num1 > num:
        print("wrong Answer, Try guessing a lower Number")
        print(f"You have only {i} tries left")

    elif num1<num:
        print("Wrong Answer, Try guessing a Higher Number")
        print(f"You have only {i} tries left")

    j=i

if j ==1:
    print("You Lost")
print("Game Over")
