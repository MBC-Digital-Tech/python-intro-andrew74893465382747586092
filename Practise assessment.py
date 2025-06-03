import time

#defines what dog breeds are avaliable in a list so they can be easily extracted#
dog_breeds = ["Labrador","German Shepherd","Beagle","Bulldog","Poodle"]
max_age = 15


name = input("What is your name: ")


print("Avaliable dog breeds")
time.sleep(1)
print(f"1. {dog_breeds[0]}")
time.sleep(.1)
print(f"2. {dog_breeds[1]}")
time.sleep(.1)
print(f"3. {dog_breeds[2]}")
time.sleep(.1)
print(f"4. {dog_breeds[3]}")
time.sleep(.1)
print(f"5. {dog_breeds[4]}")
while True:
    try:
        pref_breed = int(input("enter the number of your preferred dog breed: "))
        
        if pref_breed < 6 and pref_breed > 0:
        break
       
    except:
        ValueError
        print("Please enter a valid number (1-5)")
    
   


    
    

#### else:
##print("invalid input, please enter a valid number(1-5)")##
##print(f"you entered {pref_breed}")###
##pref_age = int(input("Enter preferred age of dog(1-15): "))#####
