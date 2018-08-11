import random

def MAGIC_NUMBER_CONSOLE_TITLE():
    print("\n====MAGIC NUMBERS====")
    print("---------------------")
    print("= Try to guess the ==")
    print("= magic number in  ==")
    print("= {} chances or less = ".format(chances))
    print("=====================")    

# generates a list of random, positive integers
# @param1   number of integers
# @param2   inclusive upper random range
# @return   list of numbers
def r_number_gen(count, max_int):
    my_number = [random.randint(0,max_int)]
    if count > 1:
        my_number.extend(r_number_gen(count-1,max_int))
    return my_number

def magic_number_program(chances):
    #difficulty settings
    TOTAL_NUMBERS = 3
    MAX_INT       = 9
    
    magic_numbers = r_number_gen(TOTAL_NUMBERS,MAX_INT)

    correct_guess = False
    previous_guess = []

    attempt = 0
    while attempt<chances:
        #get the user's guess
        attempt_string = "\n==========\nThis is attempt {} of {}".format(attempt+1,chances)
        user_number = int(input("{}\nEnter a number between 0 and {} (inclusive): ".format(attempt_string,MAX_INT)))

        #check the user's previous guesses to avoid repeat
        if user_number in previous_guess:
            print("\nYou've already guessed that number!")
        else:
            if user_number in magic_numbers:
                print("\n{} is a magic number!".format(user_number))
                print("Congratulations! You've won!")
                return
            else:
                print("\n{} was not the correct number.".format(user_number))
                if attempt+1==chances:
                    print("OOOOOOH, YOU HAVE FAILED!!!!")
                previous_guess.append(user_number)
                attempt+=1


magic_number_program(3)
    

