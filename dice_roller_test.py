from random import randint

repeat = True

while repeat:
    print("You rolled", randint(1, 20))
    print("Do you want to roll again? Y/N")
    repeat = ("y" or "yes") in input().lower()