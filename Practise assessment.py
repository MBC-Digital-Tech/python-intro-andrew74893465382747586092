import time
import webbrowser
#defines what dog breeds are avaliable in a list so they can be easily extracted#
dog_breeds = ["Labrador","German Shepherd","Beagle","Bulldog","Poodle"]
max_age = 15

yes = ["yes", "yes please", "yea",'yee',"indeed","i am in agreement",'yeeeee',"y", "ye","sure"]
no = ['nooooooo', 'no','never','i would hate that','noo',"n","nah", "nah g"]
name = input("What is your name: ")

i = 1

print("Avaliable dog breeds")
for breed in dog_breeds:
    print(f"{i}. {breed}")
    time.sleep(.1)
    i = i + 1

while True:
    try:
        pref_breed = int(input("enter the number of your preferred dog breed: "))
        
        if pref_breed < 6 and pref_breed > 0:
            break
        else:
            print("Please enter a valid number (1-5)")
    except:
        ValueError
        print("Please enter a valid number (1-5)")


while True:
    try:
        pref_age = int(input("enter the preferred age of your dog: "))
        
        if pref_age <= max_age and pref_age > 0:
            break
        else:
            print("Please enter a valid number (1-15)")
    except:
        ValueError
        print("Please enter a valid number (1-15)")



final_breed = dog_breeds[pref_breed-1]

print(f"Thank you, {name}!")
time.sleep(1)
print(f"You prefer a {final_breed} that is about {pref_age} years old.")
time.sleep(1.5)
print("Good luck finding your perfect furry friend!")
time.sleep(1)

while True:
    google = input("Want to see your potential dog: ")
    googlel = google.lower()
    if googlel not in no and not in yes:
        print("I dunno what you mean, try again")
    elif googlel in yes and pref_breed == 1:
        webbrowser.open("https://www.google.com/search?q=labrador&sca_esv=b42e03ff43b61ad3&rlz=1C1GCEB_enNZ1164NZ1164&ei=zno_aNihE_2WseMPmZyN2A0&ved=0ahUKEwjYwPr8qdaNAxV9S2wGHRlOA9sQ4dUDCBE&uact=5&oq=labrador&gs_lp=Egxnd3Mtd2l6LXNlcnAiCGxhYnJhZG9yMg0QLhiABBixAxhDGIoFMg0QLhiABBixAxhDGIoFMgoQABiABBhDGIoFMgoQABiABBhDGIoFMgoQABiABBhDGIoFMgoQABiABBhDGIoFMgoQABiABBhDGIoFMgUQABiABDIFEAAYgAQyBRAAGIAEMhwQLhiABBixAxhDGIoFGJcFGNwEGN4EGN8E2AEBSIAgUIIFWNgdcAJ4AZABApgBtQOgAYgcqgEFMy01LjS4AQPIAQD4AQGYAgmgAqEWqAITwgIKEAAYsAMY1gQYR8ICDRAuGIAEGLADGEMYigXCAg0QABiABBiwAxhDGIoFwgIOEAAYsAMY5AIY1gTYAQHCAhMQLhiABBiwAxhDGMgDGIoF2AEBwgITEC4YgAQYQxi0AhiKBRjqAtgBAsICExAAGIAEGEMYtAIYigUY6gLYAQLCAhAQLhgDGLQCGOoCGI8B2AEBwgIQEAAYAxi0AhjqAhiPAdgBAcICEhAuGAMYtAIY6gIYChiPAdgBAcICChAuGIAEGEMYigXCAhQQLhiABBixAxjRAxiDARjHARiKBcICCBAAGIAEGLEDwgIREC4YgAQYsQMY0QMYgwEYxwHCAgsQLhiABBjHARivAcICCBAuGIAEGLEDwgILEAAYgAQYsQMYgwHCAhkQLhiABBhDGIoFGJcFGNwEGN4EGN8E2AEBwgIQEC4YgAQYsQMYQxjUAhiKBcICDRAuGIAEGEMY1AIYigXCAhAQLhiABBixAxhDGIMBGIoFmAMG8QWxf4w2wqE804gGAZAGE7oGBggBEAEYCboGBAgCGAeSBwcyLjMtMy40oAfA2AGyBwUzLTMuNLgHkxbCBwMyLTnIByg&sclient=gws-wiz-serp&safe=active&ssui=on")
        break
    elif googlel in yes and pref_breed == 2:
        webbrowser.open("https://www.google.com/search?q=germaqn+shepherd&sca_esv=b42e03ff43b61ad3&rlz=1C1GCEB_enNZ1164NZ1164&ei=1Hw_aI_LCqaP4-EP-bqwsAQ&ved=0ahUKEwiPhfLzq9aNAxWmxzgGHXkdDEYQ4dUDCBE&uact=5&oq=germaqn+shepherd&gs_lp=Egxnd3Mtd2l6LXNlcnAiEGdlcm1hcW4gc2hlcGhlcmQyChAuGIAEGLEDGA0yBxAAGIAEGA0yBxAAGIAEGA0yBxAAGIAEGA0yBxAAGIAEGA0yBxAAGIAEGA0yBxAAGIAEGA0yBxAAGIAEGA0yBxAAGIAEGA0yBxAAGIAEGA0yGRAuGIAEGLEDGA0YlwUY3AQY3gQY3wTYAQFIpRtQAFitGXAAeAGQAQCYAbIDoAHjKKoBBTMtNi43uAEDyAEA-AEBmAINoAKcKcICChAuGIAEGEMYigXCAgoQABiABBhDGIoFwgILEAAYgAQYsQMYgwHCAg4QABiABBixAxiDARiKBcICERAuGIAEGLEDGNEDGIMBGMcBwgIFEC4YgATCAhkQLhiABBhDGIoFGJcFGNwEGN4EGN8E2AEBwgINEC4YgAQYsQMYQxiKBcICHBAuGIAEGLEDGEMYigUYlwUY3AQY3gQY3wTYAQHCAg0QLhiABBixAxjJAxgNwgIcEC4YgAQYsQMYyQMYDRiXBRjcBBjeBBjfBNgBAZgDALoGBggBEAEYFJIHBjMtMy4xMKAHmasCsgcGMy0zLjEwuAecKcIHBDItMTPIBzE&sclient=gws-wiz-serp&safe=active&ssui=on")
        break
    elif googlel in yes and pref_breed == 3:
        webbrowser.open("https://www.google.com/search?q=beagle&sca_esv=b42e03ff43b61ad3&rlz=1C1GCEB_enNZ1164NZ1164&ei=Bn0_aMbzL_vc4-EPkaG8-Ac&ved=0ahUKEwjGjoOMrNaNAxV77jgGHZEQD38Q4dUDCBE&uact=5&oq=beagle&gs_lp=Egxnd3Mtd2l6LXNlcnAiBmJlYWdsZTINEC4YgAQYsQMYQxiKBTIKEAAYgAQYQxiKBTIKEAAYgAQYQxiKBTIKEAAYgAQYQxiKBTIKEAAYgAQYQxiKBTIKEAAYgAQYQxiKBTIKEAAYgAQYQxiKBTIFEAAYgAQyBRAAGIAEMgUQABiABDIcEC4YgAQYsQMYQxiKBRiXBRjcBBjeBBjfBNgBAUjcLlCuBlj0KHABeAKQAQSYAckFoAGiK6oBCTMtNC4yLjQuMbgBA8gBAPgBAZgCCaAC6RioAhTCAgQQABhHwgIQEC4YgAQYsQMYQxjJAxiKBcICCxAAGIAEGJIDGIoFwgIKEC4YgAQYQxiKBcICHxAuGIAEGLEDGEMYyQMYigUYlwUY3AQY3gQY3wTYAQHCAhMQLhiABBhDGLQCGIoFGOoC2AECwgITEAAYgAQYQxi0AhiKBRjqAtgBAsICFhAuGIAEGEMY1AIYtAIYigUY6gLYAQLCAhAQABgDGLQCGOoCGI8B2AEBwgIQEC4YAxi0AhjqAhiPAdgBAcICDRAuGIAEGEMY1AIYigXCAhwQLhiABBhDGNQCGIoFGJcFGNwEGN4EGN8E2AEBwgIZEC4YgAQYQxiKBRiXBRjcBBjeBBjfBNgBAZgDBeIDBRIBMSBA8QVWP85mp1kQG4gGAZAGCLoGBggBEAEYFLoGBAgCGAeSBwkyLjMtMy4zLjGgB6eqArIHBzMtMy4zLjG4B-EYwgcFMC4xLjjIByE&sclient=gws-wiz-serp&safe=active&ssui=on")
        break
    elif googlel in yes and pref_breed == 4:
        webbrowser.open("https://www.google.com/search?q=bulldog&sca_esv=b42e03ff43b61ad3&rlz=1C1GCEB_enNZ1164NZ1164&ei=NH0_aInhI4eUg8UPvZ_bOQ&ved=0ahUKEwiJy-6hrNaNAxUHyqACHb3PNgcQ4dUDCBE&uact=5&oq=bulldog&gs_lp=Egxnd3Mtd2l6LXNlcnAiB2J1bGxkb2cyExAuGIAEGLEDGEMY1AIYyQMYigUyCxAAGIAEGJIDGIoFMgoQABiABBhDGIoFMgoQABiABBhDGIoFMgUQABiABDIFEAAYgAQyBRAAGIAEMggQLhiABBixAzIFEAAYgAQyBRAAGIAEMiIQLhiABBixAxhDGNQCGMkDGIoFGJcFGNwEGN4EGN8E2AEBSO8PUABYnwpwAHgBkAEAmAGBBKABpReqAQczLTMuMy4xuAEDyAEA-AEBmAIHoALFF8ICChAuGIAEGEMYigXCAg0QLhiABBhDGNQCGIoFwgIZEC4YgAQYQxiKBRiXBRjcBBjeBBjfBNgBAcICCxAuGIAEGMcBGK8BwgIOEC4YgAQYsQMY0QMYxwHCAgsQABiABBixAxiDAcICCBAAGIAEGLEDwgIREC4YgAQYsQMY0QMYxwEYigXCAhwQLhiABBhDGNQCGIoFGJcFGNwEGN4EGN8E2AEBwgINEC4YgAQYsQMYQxiKBcICBRAuGIAEwgINEAAYgAQYsQMYQxiKBcICEBAuGIAEGLEDGEMY1AIYigWYAwC6BgYIARABGBSSBwUzLTMuNKAH_twBsgcFMy0zLjS4B8UXwgcDMi03yAcc&sclient=gws-wiz-serp&safe=active&ssui=on")
        break
    elif googlel in yes and pref_breed == 5:
        webbrowser.open("https://www.google.com/search?q=poodle&sca_esv=b42e03ff43b61ad3&rlz=1C1GCEB_enNZ1164NZ1164&ei=UH0_aJTLApaa4-EPpamsqQw&ved=0ahUKEwiUs_qurNaNAxUWzTgGHaUUK8UQ4dUDCBE&uact=5&oq=poodle&gs_lp=Egxnd3Mtd2l6LXNlcnAiBnBvb2RsZTINEC4YgAQYsQMYQxiKBTIKEC4YgAQYQxiKBTIKEAAYgAQYQxiKBTIKEAAYgAQYQxiKBTIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIcEC4YgAQYsQMYQxiKBRiXBRjcBBjeBBjfBNgBAkisEFCeBljsDXABeAGQAQGYAcMFoAHsEaoBCTMtMy4xLjAuMbgBA8gBAPgBAZgCBaACwQyoAhTCAhMQLhiABBhDGLQCGIoFGOoC2AEBwgIWEC4YgAQYQxjUAhi0AhiKBRjqAtgBAcICEBAuGAMYtAIY6gIYjwHYAQLCAhAQABgDGLQCGOoCGI8B2AECwgIQEC4YgAQY0QMYQxjHARiKBcICDRAuGIAEGEMY1AIYigXCAhkQLhiABBhDGIoFGJcFGNwEGN4EGN8E2AECwgINEAAYgAQYsQMYQxiKBcICCBAAGIAEGLEDwgIFEC4YgASYAwbxBeJTcvVh7egPugYECAEYB7oGBggCEAEYCpIHBzEuMy0yLjKgB7ueAbIHBTMtMi4yuAe7DMIHAzItNcgHFQ&sclient=gws-wiz-serp&safe=active&ssui=onn")
        break
    
    elif googlel in no:
         print("sad")
         break


    
    

#### else:
##print("invalid input, please enter a valid number(1-5)")##
##print(f"you entered {pref_breed}")###
##pref_age = int(input("Enter preferred age of dog(1-15): "))#####
