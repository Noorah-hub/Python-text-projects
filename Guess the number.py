import random

def game():
    print("You put in a range of numbers,the computer picks a number"
    "from the range and you guess it.\nEasy Peasy!!!")

    first=input("Type in a number: ")
    if first.isdigit():
        first=int(first)

        if first<=0:
            print("Type in a number larger than 0.")
            quit()
    else:
        print("Please type in a number.")
        quit()

    randomnum=random.randint(0, first)       
    guesses=0

    while True:
        guesses+=1
        user=input("Make a guess: ")
        if user.isdigit():
            user=int(user)
        else:
            print("Please type a number.")
            continue

        if user==randomnum:
            print("You got it!!")   
            break   
        elif  user>randomnum:
            print("You were above the number!!")
        else:
            print("You were below the number!!")
    print("You got it in", guesses,"guesses!!")             

    hol=input("Do you want to play again? Yes/No").title()
    if hol == "Yes":
            game()
    elif hol == "No":
        print("Game Over!")    


game()




