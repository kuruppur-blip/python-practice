playing = True 
score = 0 

def main():

# Introduction: 
    print("HELLO.👋")
    print("This is a quiz. The quiz will be based on New Zealand to test your knowledge. (●'◡'●)")

# First Question:
print("First Question;")
while "firstquestion" != "WELLINGTON": 
    firstquestion = input("What is the capital of New Zealand?").upper()
    if firstquestion == "WELLINGTON":
    # If they get it right
        score += 1 
        print("The score." + str(score))  
        print("Well done.")
        print("That was easy. Next question...")
        break
    elif firstquestion == "WELLINGTON":
    # If they get it right
        print("Well done!")
        print("That was easy. Next question...")
        break 
    else:
    # If they get it wrong
        print("Uh oh! That's not right.")
        print("Try again...")
        score -= 1  
        print("The score." + str(score))
        continue 
 
# Second Question:
print("Second Question;")
while "secondquestion" != "KIWI":   
    secondquestion = input("What is the national symbol of New Zealand?").upper()
    if secondquestion == "KIWI":
    # If they get it right 
        score += 1 
        print("The score." + str(score))
        print("Well done.")
        print("That was easy. Next question...")
        break 
    elif secondquestion == "KIWI":
    # If they get it right 
        print("Well done")
        print("That was easy. Next question...")
        break 
    else:
    # If they get it wrong 
        print("Uh oh! That's not right.")
        print("Try again...")
        score -= 1 
        print("The score." + str(score))
        continue 

#Third Question:
print("Third Question;")
while "thirdquestion" != "MAORI":
    thirdquestion = input("What is the name of New Zealand's indigenous people?").upper()
    if thirdquestion == "MAORI":
    # If they get it right 
        score += 1 
        print("The score." + str(score))
        print("Well done.")
        print("That was easy. Next question...")
        break 
    elif thirdquestion == "MAORI":
    # If they get it right  
        print("Well done.")
        print("That was easy. Next question...")
        break 
    else:
    # If they get it wrong 
        print("Uh oh! That's not right.")
        print("Try again...")
        score -= 1 
        print("The score." + str(score))
        continue 

#Fourth Question:
print("Fourth Question;")
while "fourthquestion" != "NORTH AND SOUTH ISLANDS": 
    fourthquestion = input("What are the two main islands of New Zealand called?").upper()
    if fourthquestion == "NORTH AND SOUTH ISLANDS":
    # If they get it right 
        score += 1 
        print("The score." + str(score))
        print("Well done.")
        print("That was easy. Next question...")
        break 
    elif fourthquestion == "NORTH AND SOUTH ISLANDS.":
    # If they get it right 
        print("Well done.")
        print("That was easy. Next question")
        break 
    else:
    # If they get it wrong 
        print("Uh oh! That's not right.")
        print("Try again...") 
        score -= 1 
        print("The score." + str(score))
        continue 

#Fifth question: 
print("Fifth question;")
while "fifthquestion" != "THE LORD OF THE RINGS":    
    fifthquestion = input("Which famouse movie that was filmed in New Zealand?").upper()
    if fifthquestion == "THE LORD OF THE RINGS": 
    # If they get it right 
        score += 1 
        print("The score." + str(score))
        print("Well done.")
        print("That was easy. Next question...")
        break 
    elif fifthquestion ==  "THE LORD OF THE RINGS.": 
    # If they get it right 
        print("Well done.")
        print("That was easy. Next question")
        break 
    else:
    # If they get it wrong 
        print("Uh oh! That's not right.")
        print("Try again...")
        score -= 1 
        print("The score." + str(score))
        continue 

#Sixth Question: 
print("Sixth question;")
while "sixthquestion" != "AOTEAROA": 
    sixthquestion = input("What are the Maori name for New Zealand?").upper()
    if sixthquestion == "AOTEAROA":
    # If they get it right 
        score += 1 
        print("The score." + str(score))
        print("Well done.")
        print("That was easy. Next question...")
        break 
    elif sixthquestion == "AOTEAROA.":
    # If they get it right 
        print("Well done.")
        print("That was easy. Next question")
        break 
    else:
    # If they get it wrong 
        print("Uh oh! That's not right.")
        print("Try again...")
        score -= 1 
        print("The score." + str(score))
        continue

#Seventh Question: 
print("Seventh Question;")
while "seventhquestion" != "AUCKLAND":
    seventhquestion = input("Which city is known as the CITY OF SAILS?").upper()
    if seventhquestion == "AUCKLAND":
    # If they get it right 
        score += 1 
        print("The score." + str(score))
        print("Well done.")
        print("That was easy. next question...")
        break 
    elif seventhquestion == "AUCKLAND.":
    # If they get it right 
        print("Well done.")
        print("That was easy. Next question...")
        break 
    else: 
    # If they get it wrong 
        print("Uh oh! That's not right.")
        print("Try again...")
        score -= 1 
        print("The score." + str(score))
        continue

#Eigth Question:
print("Eighth Question;")
while "eigthquestion" != "THE ALPINE FAULT":
    eighthquestion = input("What major tectonic feature runs through New Zealnd?").upper()
    if eighthquestion == "THE ALPINE FAULT":
    # If theu get it right 
        score += 1 
        print("The score." + str(score))
        print("Well done.")
        print("That was easy. Next question...")
        break
    elif eighthquestion == "THE ALPINE FAULT.":
    # If they get it right 
        print("Well done.")
        print("That was easy. Next question...")
        break 
    else:
    # If they get it wrong 
        print("Uh oh! That's not right.")
        print("Try again...") 
        score -= 1 
        print("The score." + str(score))
        continue 

#Ninth Question:
print("Ninth Question;")
while "ninthquestion" != "KEA":
    ninthquestion = input("Which New Zealand bird is the world's only alpine parrot?").upper()
    if ninthquestion == "KEA":
    # If they get it right 
        score += 1 
        print("The score." + str(score))
        print("Well done.")
        print("That was easy. Next question....")
        break 
    elif ninthquestion == "KEA.":
    # If they get it right 
        print("Well done.")
        print("That was easy. Next question...")
        break 
    else:
    # If they get it wrong 
        print("Uh oh! That's not right.")   
        print("Try again...")
        score -= 1 
        print("The score." + str(score))
        continue 

#Tenth Question: 
print("Tenth Question;")
while "tenthquestion" != "EDMUND HILLARY":
    tenthquestion = input("Who was the first person to reach the summit of MOunt EVerest, and is one of New Zealand's most famous figures?").upper()
    if tenthquestion == "EDMUND HILLARY":
    # If they get it right 
        score += 1 
        print("The score." + str(score))
        print("Well done.")
        print("That was easy...")
        break 
    elif tenthquestion == "EDMUND HILLARY.":
    # If they get it right 
        print("Well done.")
        print("That was easy...")
        break 
    else:
    # If they get it wrong
        print("Uh oh! That's not right.")
        print("Try again...")
        score -= 1 
        print("The score." + str(score))
        continue 


print("WELL DONE! 👍")
print("Thank you for playing")
print("Bye bye. ╰(*°▽°*)╯")


# This runs the quiz when the file is executed
if"__main__": 
    main()

 