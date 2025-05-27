import time

def quiz():
    score = 0
    rage = 0
    print("Hello")
    time.sleep(1.5)
    print("This is a quiz.")
    time.sleep(1.5)
    print("You will fail!")
    time.sleep(3)
    print("Good luck!")
    
    yn = input("Do you want to play? ")
    if yn.lower() == "yes":
        print("Great!")
    elif yn.lower() == "no":
        print("Goodbye")
        quit()
    else:
        print("yes or no only...")
        time.sleep(1.5)
        print('NOW BEGIN AGAIN AND GET IT RIGHT THIS TIME')
        quit()
    time.sleep(1.5)
    print("Question 1")
    time.sleep(1.5)
    print("Which tool is primarily used to smooth wood surfaces?")
    time.sleep(1)
    print("1. Hammer")
    time.sleep(1)
    print("2. Hand plane")
    time.sleep(1)
    print("3. Screwdriver")
    time.sleep(1)
    print("4. Saw")
    time.sleep(1)
    answer_one = input("Enter your answer (1, 2, 3 or 4): ")
    if answer_one == "2":
        print("Correct!")
        score += 1
    else:
        print("Incorrect, the answer is Hand plane. If you continue down this path of wrongness you will be punished")
        rage += 1
    time.sleep(2)
    print("Question 2")
    time.sleep(2)
    print("What is the name of the joint commonly used to connect two pieces of wood at a right angle?")
    time.sleep(1)
    print("1. Dovetail joint")
    time.sleep(1)
    print("2. Mortise and tenon joint")
    time.sleep(1)
    print("3. Butt joint")
    time.sleep(1)
    print("4. Lap joint")
    time.sleep(1)
    answer_two = input("Enter your answer (1, 2, 3 or 4): ")
    if answer_two == "3":
        print("Correct!")
        score += 1
    elif answer_two != "3" and rage == 1:
        print("Incorrect, the answer is Butt joint")
        print("You have been punished for your wrongness")
        rage += 1
    elif answer_two != "3" and rage == 0:
        print("Incorrect, the answer is Butt joint")
        print("if you continue down this path of wrongness you will be punished")
        rage += 1
    time.sleep(1.5)
    print("Question 3")
    time.sleep(1.5)
    print("Which type of saw is best for cutting curves in wood?")
    time.sleep(1)
    print("1. Circular saw")
    time.sleep(1)
    print("2. Jigsaw")
    time.sleep(1)
    print("3. Table saw")
    time.sleep(1)
    print("4. Miter saw")
    time.sleep(1)
    answer_three = input("Enter your answer (1, 2, 3 or 4): ")
    if answer_three == "2":
        print("Correct!")
        score += 1
    elif rage == 2 and answer_three != "2":
        print("Incorrect, the answer is Jigsaw")
        print("3 out of 5... you will see the consequences")
        rage += 1
    print("question 4")
    time.sleep(1.5)
    print("Which wood is commonly used for making furniture due to its strength and appearance?")
    time.sleep(1)
    print("1. Pine")
    time.sleep(1)
    print("2. Oak")
    time.sleep(1)
    print("3. Balsa")
    time.sleep(1)
    print("4. Cedar")
    time.sleep(1)
    answer_four = input("Enter your answer (1, 2, 3 or 4): ")
    if answer_four == "2":
        print("Correct!")
        score += 1
    elif rage == 3 and answer_four != "2":
        print("Incorrect, the answer is Oak")
        print("4 out of 5... you will see the consequences")
        rage += 1
    print("question 5")
    time.sleep(1.5)
    print("What is the purpose of wood stain?")
    time.sleep(1)
    print("1. To glue wood pieces together")
    time.sleep(1)
    print("2. To protect wood from insects")
    time.sleep(1)
    print("3. To change the color of wood")
    time.sleep(1)
    print("4. To make wood waterproof")
    time.sleep(1)
    answer_five = input("Enter your answer (1, 2, 3 or 4): ")
    if answer_five == "3":
        print("Correct!")
        score += 1
    elif rage == 4 and answer_five != "3":
        print("Incorrect, the answer is To change the color of wood")
        print("5 out of 5... The void is coming for you")
        quit()
    print("question 6")
    time.sleep(1.5)
    print("Which tool is used to measure angles in woodworking?")
    time.sleep(1)
    print("1. Square")
    time.sleep(1)
    print("2. Level")
    time.sleep(1)
    print("3. Caliper")
    time.sleep(1)
    print("4. Tape measure")
    time.sleep(1)
    answer_six = input("Enter your answer (1, 2, 3 or 4): ")
    if answer_six == "1":
        print("Correct!")
        score += 1
    elif rage == 4 and answer_six != "1":
        print("Incorrect, the answer is Square")
        print("5 out of 5... The void is coming for you")
        quit()
    print("question 7")
    time.sleep(1.5)
    print("What is the process of joining wood pieces using glue and pressure called?")
    time.sleep(1)
    print("1. Laminating")
    time.sleep(1)
    print("2. Sanding")
    time.sleep(1)
    print("3. Carving")
    time.sleep(1)
    print("4. Finishing")
    time.sleep(1)
    answer_seven = input("Enter your answer (1, 2, 3 or 4): ")
    if answer_seven == "1":
        print("Correct!")
        score += 1
    elif rage == 4 and answer_seven != "1":
        print("Incorrect, the answer is Laminating")
        print("5 out of 5... The void is coming for you")
        quit()
    print("question 8")
    time.sleep(1.5)
    print("Which finish is commonly used to give wood a glossy, protective surface?")
    time.sleep(1)
    print("1. Varnish")
    time.sleep(1)
    print("2. Paint")
    time.sleep(1)
    print("3. Oil")
    time.sleep(1)
    print("4. Wax")
    time.sleep(1)
    answer_eight = input("Enter your answer (1, 2, 3 or 4): ")
    if answer_eight == "1":
        print("Correct!")
        score += 1
    elif rage == 4 and answer_eight != "1":
        print("Incorrect, the answer is Varnish")
        print("5 out of 5... The void is coming for you")
        quit()
    print("question 9")
    time.sleep(1.5)
    print("What is the name of the tool used to drive nails into wood?")
    time.sleep(1)
    print("1. Chisel")
    time.sleep(1)
    print("2. Mallet")
    time.sleep(1)
    print("3. Hammer")
    time.sleep(1)
    print("4. Clamp")
    time.sleep(1)
    answer_nine = input("Enter your answer (1, 2, 3 or 4): ")
    if answer_nine == "3":
        print("Correct!")
        score += 1
    elif rage == 4 and answer_nine != "3":
        print("Incorrect, the answer is Hammer")
        print("5 out of 5... The void is coming for you")
        quit()
    print("question 10")
    time.sleep(1.5)
    print("Which of these is a softwood?")
    time.sleep(1)
    print("1. Mahogany")
    time.sleep(1)
    print("2. Oak")
    time.sleep(1)
    print("3. Pine")
    time.sleep(1)
    print("4. Maple")
    time.sleep(1)
    answer_ten = input("Enter your answer (1, 2, 3 or 4): ")
    if answer_ten == "3":
        print("Correct!")
        score += 1
    elif rage == 4 and answer_ten != "3":
        print("Incorrect, the answer is Pine")
        print("5 out of 5... The void is coming for you")
        quit()
    print("You got " + str(score) + " out of 10")
    if score == 10:
        print("You are a genius!")
    elif score >= 8:
        print("You are very smart!")
    elif score >= 5:
        print("You are average")
    else:
        print("How did you get here?")

quiz()
