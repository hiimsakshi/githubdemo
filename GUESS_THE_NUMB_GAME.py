#WRITE A PROGRAM TO MAKE A GAME OF GESS THE NUMBER
#KEEP SOME POINTS IN MIND- 1. IF NUMBER IS GREATER THAN THE HIDDEN NUMBER,THEN
# PRINT THE HIDDEN NUMBER IS SMALLER THAN THIS NUMBER, ELSE PRINT THE NUMBER IS GREATER THAN THIS NUMBER
#KEEP THE NUMBER OF GUESS ATTEMPTS FIXED TO 10
#PRINT CONGO YOU GUESSED IT RIGHT IF GUSSED CORRECTLY ELSE THE ABOVE WITH A STATEMENT
#NUMBER OF ATTEMPTS LEFT = __
n = 18
number_of_guesses = 1
print("Welcome to the game of GUESS THE NUMBER")
print( " SOME RULES:")
print("You will get a total of 10 attempts to guess the number correctly")
print("After every failed attempt you will get a hint and the number of attempts will decrease")
while(number_of_guesses<=10):
    num = int(input("GUESS A NUMBER"))
    if num>18:
        print("YOU GUESSED TOO BIG,GUESS A SMALLER NUMBER")
    elif num<18:
        print("YOU GUESSED TOO LOW, GUESS A BIGGER NUMBER")
    else:
        print("YOU GUESSED THE RIGHT NUMBER,", "YOU WON")
        break
    print(10-number_of_guesses,"no. of guesses left")
    number_of_guesses = number_of_guesses+1
if number_of_guesses>10:
    print("you lost the game")