# starter program week 2 - perhaps this could be a task
import webbrowser
import time
def conversation():
        print("Welcome to my conversation program", end="\n\n")

        sports = input("What is your favourite sport? ")
        sportlow = sports.lower()
        if sportlow == "minecraft":
                print("I love Minecraft too!")
        elif sportlow == "football":
                print("no")
                quit()
        else:

                print(f"I hate {sports}")
                sport2 = input("Know any better ones? ")
        if sport2 == "minecraft":
                print("finally someone with good taste")
        elif sport2 == "football":
                print("no")
                quit()
        else:
                print(f"I guess {sport2} is alright")

        # combine the next two lines into one command. done
        answer = input("Do you like cycling? Answer yes or no ")
        

        # chenge this so that the user can enter YES as well.
        answer_low = answer.lower()
        
        if answer_low == "yes":
                print("That's good - you will get very fit")
        elif answer_low == "no":
                print("Perhaps you like some other sport. ")
        else: print('your not very good at answering questions')
        
        print("Goodbye")

# Add command here to run the function

def cities():
        cit = int(input("How many cities are there in England? ONLY NUMBERS OR ELSE! "))
        try:
                while cit != 51:
                        if cit < 51:
                                print("Too low")
                        elif cit > 51:
                                print("Too high")
                
                        print("Try again")

                        cit = int(input("How many cities are there in England? ONLY NUMBERS OR ELSE! "))
                print("Correct")
        except ValueError:
                webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
                quit()




def age():
        age = int(input("How old are you? "))
        if age >= 13:
                print ("you can have a paper round")
        else:
                print("You are too young for a paper round")



def notninenine():
        num = int(input("Enter a number thats not 99 "))
        if num != 99:
                print("Thank you for not entering 99")

        elif num == 99:
                webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
                

notninenine()