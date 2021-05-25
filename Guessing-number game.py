# -*- coding: utf-8 -*-
"""
Number guessing game

Author: RitchieHollis
game not finished, works in overall
"""

import random

def loop():
    score = 0
    
    random_number = int(random.randint(1,10))
    while True:

            num_pers = input("Choose a number between 1 and 10: ")
            if int(num_pers) < 0 or int(num_pers) > 10:
                print("You must choose a number between 1 ad 10")
                loop()
            """if type(num_pers) != int:
                print("Musisz podac liczbe")
                loop()"""
            if int(num_pers) == random_number:
                score = score + 1
                print ("Good!")
                print("After: ",score,"trials")
                choice2 = input("Wanna play again? (Yes/No): ")

                if choice2.lower() == 'yes':
                    loop()
                elif choice2.lower() == 'no':
                   print("Okay, goodbye :-D")
                   input()
                   return
                   
            elif int(num_pers) > random_number:
                print("Nope, it's lower")
                score = score + 1
            elif int(num_pers) < random_number:
                print("Nope, it's higher")
                score = score + 1
    
def main_game():
    

    player_name = input("Hi, what's your name?: ")
    choice = input("Hey {}, do you want to play a game? (Yes/No) ".format(player_name))
    if choice.lower() == "yes":
       loop()
       
            
               
    elif choice.lower() == "no":
        print("Okay, goodbye :-D")
        input()
        return
    
    
# The following makes this program start running at main_game() 
# when executed as a stand-alone program.    
if __name__ == '__main__':
    main_game()
    
    
