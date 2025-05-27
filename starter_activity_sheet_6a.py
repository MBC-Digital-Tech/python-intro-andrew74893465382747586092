from turtle import *
import webbrowser
## What would you expect the computer to do? Write the output exactly as you think it will appear.

def starter():
  number = 0
  while number <= 5:
    print ("Hello")
    number = number + 1
  print ("Goodbye")





def onehundred():
  number = 0
  while number <= 99:
    print ("Today is Monday")
    number = number + 1



def ninenine():
  num = int(input("Enter a number: "))
  while num != 99:
    num = int(input("Enter a number: "))
  print("You entered 99, so we will stop now.")


def storm():
  storm = input("What was the name of the most recent storm? ")
  storm = storm.lower()
  while storm != "doris":
    print("No, that is not correct. Try again.")
    storm = input("What was the name of the most recent storm? ")
    storm = storm.lower()
  print("You got it! The most recent storm was Doris.")




def bored():
  bored = input("Are you bored yet? y/n: ")
  bored = bored.lower()
  while bored != "y":
    bored = input("Are you bored yet? ")
    bored = bored.lower()
  print("Got to you in the end")



def one_to_ten():
  number = 1
  while number <= 10:
    print(number)
    number = number + 1

def one_to_ten_two():
  number = 1
  for counter in range(10):
    print(number)
    number = number + 1



def ten_to_one():
  number = 10
  while number >= 1:
    print(number)
    number = number - 1

def ten_to_one_two():
  number = 10
  for counter in range(10):
    print(number)
    number = number - 1





def cities():
        try:
         cit = int(input("How many cities are there in England? ONLY NUMBERS OR ELSE! "))
        
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
                print("You didn't heed my warning")