import random
diff = input('Choose a level of difficulty from 1 to 5 or choose the premade level mode (type digits 1 to 5 or level): ')


# Level 1
if diff == "1":
    
    number = random.randint(0, 9)
    
    guess = input("Choose a number between 0 and 9: ")
    
    if str(guess) == str(number):
        print("")
        print("YAY! You won. Rerun the program to start another game")
        
    while str(guess) > str(number):
        guess = input("You guess was bigger than the actual number, try again: ")
        
    if str(guess) == str(number):
        print("")
        print("YAY! You won. Rerun the program to start another game")
        
    
        
    while str(guess) < str(number):
        guess = input("You guess was lower than the actual number, try again: ")
        
    if str(guess) == str(number):
        print("")
        print("YAY! You won. Rerun the program to start another game")
            

# Level 2

if diff == "2":
    
    number = random.randint(0, 25)
    
    guess = input("Choose a number between 0 and 25: ")
    
    if str(guess) == str(number):
        print("")
        print("YAY! You won. Rerun the program to start another game")
        
    while str(guess) > str(number):
        guess = input("You guess was bigger than the actual number, try again: ")
        
    if str(guess) == str(number):
        print("")
        print("YAY! You won. Rerun the program to start another game")
        
    
        
    while str(guess) < str(number):
        guess = input("You guess was lower than the actual number, try again: ")
        
    if str(guess) == str(number):
        print("")
        print("YAY! You won. Rerun the program to start another game")


# Level 3

if diff == "3":
    
    number = random.randint(0, 99)
    
    print(number)
    guess = input("Choose a number between 0 and 99: ")
    
    if str(guess) == str(number):
        print("")
        print("YAY! You won. Rerun the program to start another game")
        
    while str(guess) > str(number):
        guess = input("You guess was bigger than the actual number, try again: ")
        
    if str(guess) == str(number):
        print("")
        print("YAY! You won. Rerun the program to start another game")
        
    
        
    while str(guess) < str(number):
        guess = input("You guess was lower than the actual number, try again: ")
        
    if str(guess) == str(number):
        print("")
        print("YAY! You won. Rerun the program to start another game")


# Level 4

if diff == "4":
    
    number = random.randint(0, 500)
    
    print(number)
    guess = input("Choose a number between 0 and 500: ")
    
    if str(guess) == str(number):
        print("")
        print("YAY! You won. Rerun the program to start another game")
        
    while str(guess) > str(number):
        guess = input("You guess was bigger than the actual number, try again: ")
        
    if str(guess) == str(number):
        print("")
        print("YAY! You won. Rerun the program to start another game")
        
    
        
    while str(guess) < str(number):
        guess = input("You guess was lower than the actual number, try again: ")
        
    if str(guess) == str(number):
        print("")
        print("YAY! You won. Rerun the program to start another game")


# Level 5

if diff == "5":
    
    number = random.randint(0, 999)
    
    print(number)
    guess = input("Choose a number between 0 and 999: ")
    
    if str(guess) == str(number):
        print("")
        print("YAY! You won. Rerun the program to start another game")
        
    while str(guess) > str(number):
        guess = input("You guess was bigger than the actual number, try again: ")
        
    if str(guess) == str(number):
        print("")
        print("YAY! You won. Rerun the program to start another game")
        
    
        
    while str(guess) < str(number):
        guess = input("You guess was lower than the actual number, try again: ")
        
    if str(guess) == str(number):
        print("")
        print("YAY! You won. Rerun the program to start another game")


# Main Level Mode

lives = []

if diff == "level":
    
    number = random.randint(0, 5)
    
    print(number)
    guess = input("Choose a number between 0 and 5: ")
    
    if str(guess) == str(number):
        print("")
        print("Nice job, you beat the first level and you still have " + str(lives))
    
    while str(guess) != str(number):
        while len(lives) < 5:
        
            if str(guess) > str(number):
                lives.append("boom")
                guess = input("Your guess was too high, try again: ")
            
            if str(guess) < str(number):
                lives.append("boom")
                guess = input("Your guess was too low, try again: ")
        
            if len(lives) >= 5:
                print("")
                print("You have lost:( the number was " + str(number))
    
    if str(guess) == str(number):
        print("")
        print("Nice! you won the first round.")
        print("The actual number was " + str(number))
        print("And you only used " + str(len(lives)) + " out of 5 lives!")
        print("")
        print("Round 2!")
        
        number = random.randint(0, 9)
    
    print(number)
    guess = input("Choose a number between 0 and95: ")
    
    if str(guess) == str(number):
        print("")
        print("Nice job, you beat the first level and you still have " + str(lives))
    
        while str(guess) != str(number):
            while len(lives) < 5:
            
                if str(guess) > str(number):
                    lives.append("boom")
                    guess = input("Your guess was too high, try again: ")
                
                if str(guess) < str(number):
                    lives.append("boom")
                    guess = input("Your guess was too low, try again: ")
            
                if len(lives) >= 5:
                    print("")
                    print("You have lost:( the number was " + str(number))
        
        if str(guess) == str(number):
            print("")
            print("Nice! you won the first round.")
            print("The actual number was " + str(number))
            print("And you only used " + str(len(lives)) + " out of 5 lives!")
            print("")
            print("Round 3!")
            
            number = random.randint(0, 25)
    
            print(number)
            guess = input("Choose a number between 0 and 25: ")
            
            if str(guess) == str(number):
                print("")
                print("Nice job, you beat the first level and you still have " + str(lives))
            
            while str(guess) != str(number):
                while len(lives) < 5:
                
                    if str(guess) > str(number):
                        lives.append("boom")
                        guess = input("Your guess was too high, try again: ")
                    
                    if str(guess) < str(number):
                        lives.append("boom")
                        guess = input("Your guess was too low, try again: ")
                
                    if len(lives) >= 5:
                        print("")
                        print("You have lost:( the number was " + str(number))
            
            if str(guess) == str(number):
                print("")
                print("Nice! you won the first round.")
                print("The actual number was " + str(number))
                print("And you only used " + str(len(lives)) + " out of 5 lives!")
                print("")
                print("Round 4!")
                
                number = random.randint(0, 25)
    
                print(number)
                guess = input("Choose a number between 0 and 50: ")
                
                if str(guess) == str(number):
                    print("")
                    print("Nice job, you beat the first level and you still have " + str(lives))
                
                while str(guess) != str(number):
                    while len(lives) < 5:
                    
                        if str(guess) > str(number):
                            lives.append("boom")
                            guess = input("Your guess was too high, try again: ")
                        
                        if str(guess) < str(number):
                            lives.append("boom")
                            guess = input("Your guess was too low, try again: ")
                    
                        if len(lives) >= 5:
                            print("")
                            print("You have lost:( the number was " + str(number))
                
                if str(guess) == str(number):
                    print("")
                    print("Nice! you won the first round.")
                    print("The actual number was " + str(number))
                    print("And you only used " + str(len(lives)) + " out of 5 lives!")
                    print("")
                    print("Round 5!")
                    print("")
                    print("This is all for now, we will have nore updates comming in the future.")
                    print("Please report all bugs here: https://forms.gle/8PjeBDkzvDiqFuTt8")
        

        
# Incorrect Command

else:
    print("Incorrect command")
    print("Rerun the program to start playing")
