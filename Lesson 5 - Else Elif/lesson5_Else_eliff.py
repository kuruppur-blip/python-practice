playing = True 
score = 0 

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
    fifthquestion = input("Which movie was filmed in New Zealand?").upper()
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
        print("The answer is: " + sixthquestion)
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
    #print("The answer is AUCKLAND.")
        print("Well done.")
        print("The answer is: " + seventhquestion)
    elif seventhquestion == "AUCKLAND.":
        print("Well done.")
        print("The answer is: " + seventhquestion)
    else: 
        print("Uh oh! That's not right.")
        print("The answer is: " + seventhquestion)

# print("Eighth Question;")
# eighthquestion = input("What major tectonic feature runs through New Zealnd?").upper()
# if eighthquestion == "THE ALPINE FAULT":
# #print("The answer is THE ALPINEFAULT.")
#     print("Well done.")
#     print("The answer is: " + eighthquestion)
# elif eighthquestion == "THE ALPINE FAULT.":
#     print("Well done.")
#     print("The answer is: " + eighthquestion)
# else:
#     print("Uh oh! That's not right.")
#     print("The answer is: " + eighthquestion)

# print("Ninth Question;")
# ninthquestion = input("Which New Zealand bird is the world's only alpine parrot?").upper()
# if ninthquestion == "KEA":
# #print("The answer is KEA")
#     print("Well done.")
#     print("The answer is: " + ninthquestion)
# elif ninthquestion == "KEA.":
#     print("Well done.")
#     print("The answer is: " + ninthquestion)
# else:
#     print("Uh oh! That's not right.")
#     print("The answer is: " + ninthquestion)

# print("Tenth Question;")
# tenthquestion = input("Who was the first person to reach the summit of MOunt EVerest, and is one of New Zealand's most famous figures?").upper()
# if tenthquestion == "EDMUND HILLARY":
# #print("The answer is EDMUND HILLARY.")
#     print("Well done.")
#     print("The answer is: " + tenthquestion)
# elif tenthquestion == "EDMUND HILLARY.":
#     print("Well done.")
#     print("The answer is: " + tenthquestion)
# else:
#     print("Uh oh! That's not right.")
#     print("The answer is: " + tenthquestion)


print("WELL DONE! 👍")
print("Thank you for playing")
print("Bye bye. ╰(*°▽°*)╯")

