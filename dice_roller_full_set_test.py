from random import randint

def d2_roller():
    roll_d2 = randint(1, 2)
    return roll_d2
    
def d4_roller():
    roll_d4 = randint(1, 4)
    return roll_d4

def d6_roller():
    roll_d6 = randint(1, 6)
    return roll_d6

def d8_roller():
    roll_d8 = randint(1, 8)
    return roll_d8

def d10_roller():
    roll_d10 = randint(1, 10)
    return roll_d10

def d12_roller():
    roll_d12 = randint(1, 12)
    return roll_d12

def d20_roller():
    roll_d20 = randint(1, 20)
    return roll_d20

def d100_roller():
    roll_d100 = randint(1, 100)
    return roll_d100

def dice_switcher(dice_choice):
    switcher = {
        "d2" : d2_roller(),
        "d4" : d4_roller(),
        "d6" : d6_roller(),
        "d8" : d8_roller(),
        "d10" : d10_roller(),
        "d12" : d12_roller(),
        "d20" : d20_roller(),
        "d100" : d100_roller()   
    }
    return switcher.get(dice_choice, "Not an option, try again.")


repeat = True

while repeat:
    print("What would you like to roll? (D2, D4, D6, D8, D10, D12, D20, D100) Type stop to quit.")
    user_choice = input().lower()
    if user_choice == "stop":
        print("Thanks for rolling!")
        break
    else:
        print(dice_switcher(user_choice))

""" print(dice_switcher("D20"))

print (dice_switcher("D4"))

print(dice_switcher("D33")) """