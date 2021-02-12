def switch_analogue(dice_choice):
    switcher = {
        "D2" : "2",
        "D4" : "4",
        "D6" : "6",
        "D8" : "8",
        "D10" : "10",
        "D12" : "12",
        "D20" : "20",
        "D100" : "100"       
    }
    return switcher.get(dice_choice, "Not an option, try again.")

print(switch_analogue("D20"))

print (switch_analogue("D4"))

print(switch_analogue("D33"))