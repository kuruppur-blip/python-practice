# =====================================================================
# Task: Country Guessing Game
# =====================================================================
print(" WELCOME ") 
print("To the country guessing game.(❁´◡`❁)")
print("You have to guess the country that has been chosen by the user.")
# VALUES
# TODO: Create a variable to store the correct country (e.g., "Italy").
country = "Monaco"
# TODO: Create a variable to keep track of the user's current guess. 
#       (Hint: Start it as an empty string "" so the loop runs at least once!)
guess = ""  


# LOOP
# TODO: Start a 'while' loop. 
#       The loop should keep running AS LONG AS the user's guess 
#       is NOT EQUAL to the correct country.
while guess != 'Monaco':
    
    # TODO: Ask the user for their guess and save it to your guess variable.
    #       (Remember: This changes the loop condition so it doesn't run forever!)
    guess = input("what country is it?")
    # TODO: (Optional) Add an 'if' statement inside the loop.
    #       If they guessed wrong, print an encouraging message or an extra hint.
    if guess != country:
        print("Try again...")
        input("What country is it?")

    #       If they guessed right, the loop will automatically exit on the next check!
    else: 
        guess == country
        print("Well done...")
# GAME OVER / WINNING MESSAGE
# TODO: Print a congratulatory message celebrating their win!
input("Congradulations!!!")
# ================================================================
# EXTENSION
# TODO: Add an introduction
# TODO: Add a scoring system (starts at 20, lose 1 point for each wrong guess)
# TODO: Add a lose condition (if score reaches 0)

#==================================================================
# EXPERT
# TODO: Make the game unique (use a list of countries and randomly select one)
# TODO: Add a play again option