# starter program week 3 - perhaps this could be a task

def cooking():
    print("Meal planner")
    print()

    # change these to your favourite meals
    print("1. Chicken")
    print("2. Pork chops")
    print("3. Burger and chips")
    print("4. Pizza")  
    # add one more meal here
    print()
    # adapt the next line to add in the 4.
    
    # combine the line above and below into one command that accepts an integer instead of a string.
    answer = int(input("Which of these meals is your favourite? (1, 2, 3 or 4) "))
    # adapt the if else block to include the fourth meal and compares integers instead of strings.
    if answer == 1:
        print("Chicken curry coming up")
    elif answer == 2:
        print("Veggie lasagne coming up")
    elif answer == 3:
        print("Burger and salad coming up!")
    elif answer == 4:
        print("Pizza coming up!")
    print("Enjoy!")
    
# add a command to run the function above.

cooking()