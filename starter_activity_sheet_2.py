# starter program week 2 - perhaps this could be a task

def conversation():
    print("Welcome to my conversation program", end="\n\n")

    # combine the next two lines into one command.
    print("Do you like cycling? Answer yes or no")
    answer = input()

    # chenge this so that the user can enter YES as well.
    if answer == "yes":
        print("That's good - you will get very fit")
    else:
        print("Perhaps you like some other sport. ")
    
    print("Goodbye")

# Add command here to run the function
conversation()
