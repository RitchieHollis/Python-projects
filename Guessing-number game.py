# -*- coding: utf-8 -*-
"""
Number guessing game

Author: WC
"""

import random

def loop():
    score = 0
    
    random_number = int(random.randint(1,10))
    while True:

            num_pers = input("Zgadnij liczbe od 1 do 10: ")
            if int(num_pers) < 0 or int(num_pers) > 10:
                print("Musisz wybrac liczbe od 1 do 10")
                loop()
            """if type(num_pers) != int:
                print("Musisz podac liczbe")
                loop()"""
            if int(num_pers) == random_number:
                score = score + 1
                print ("Dobrze!")
                print("Zajelo ci to: ",score,"prob")
                choice2 = input("Chcesz zagrac jeszcze raz? (Tak/Nie): ")

                if choice2.lower() == 'tak':
                    loop()
                elif choice2.lower() == 'nie':
                   print("Okej, milego dnia :-D")
                   input()
                   return
                   
            elif int(num_pers) > random_number:
                print("Zle! Tepy chuju! Ta liczba jest nizsza")
                score = score + 1
            elif int(num_pers) < random_number:
                print("Zle! Tepy chuju! Ta liczba jest wyzsza")
                score = score + 1
    
def main_game():
    

    player_name = input("Jak sie nazywasz?: ")
    choice = input("Hej {}, chcesz zagrac w gre zgadywanie liczb? (Tak/Nie) ".format(player_name))
    if choice.lower() == "tak":
       loop()
       
            
               
    elif choice.lower() == "nie":
        print("Okej, milego dnia :-D")
        input()
        return
    
    
# The following makes this program start running at main_game() 
# when executed as a stand-alone program.    
if __name__ == '__main__':
    main_game()
    
    