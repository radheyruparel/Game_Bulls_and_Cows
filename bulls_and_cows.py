#
##Author: Radhey Ruparel
##Description: A 2-player code-breaking console game called Bulls and Cows. 
##This game is related to the code breaking board game Mastermind. 
##

#In order for the game to exit and different stages
from os import _exit as exit

#Printing about the header in the game
print('''-----------------------------------------
------- WELCOME TO BULLS AND COWS -------
-----------------------------------------''')

#Users are able to input their nicknames for the gameplay 
Nickname_Player_One=input('Player 1, enter your username:\n')
Nickname_Player_Two=input('Player 2, enter your username:\n')

#Player one is able to input their codes for the game
Code_Player_One=input(Nickname_Player_One+', enter your code:\n')

#Validate the code input, accodring the rules of the game, lowercase and lenght of 3 charcters
if Code_Player_One.isalpha()!= True or Code_Player_One.islower()!= True or len(Code_Player_One)!=3:
    print(Nickname_Player_One+', that code is not valid. Exiting.')
    exit(0)
  
#Validate the code input, accodring the rules of the game, all three are not the same
if (Code_Player_One[0]==Code_Player_One[1] or Code_Player_One[2]==Code_Player_One[1] or
Code_Player_One[2]==Code_Player_One[0]):
    print(Nickname_Player_One+', that code is not valid. Exiting.')
    exit(0)

#Player two is able to input their codes for the game
Code_Player_Two=input(Nickname_Player_Two+', enter your code:\n')

#Validate the code input, accodring the rules of the game, lowercase and lenght of 3 charcters
if Code_Player_Two.isalpha()!= True or Code_Player_Two.islower()!= True or len(Code_Player_Two)!=3:
    print(Nickname_Player_Two+', that code is not valid. Exiting.')
    exit(0)
  
#Validate the code input, accodring the rules of the game, all three are not the same
if (Code_Player_Two[0]==Code_Player_Two[1] or Code_Player_Two[2]==Code_Player_Two[1] or
Code_Player_Two[2]==Code_Player_Two[0]):
    print(Nickname_Player_Two+', that code is not valid. Exiting.')
    exit(0)
    
#The guessing gameplay
main_index=0

#This the loop for all guesses of player one
while main_index<2:
    while main_index==0: 
        cows_index=0 #To control the loops for cows   
        bull_index=0#To control the loops for cows   
        cows_points=0 #To count points for cows 
        bull_points=0 #To count points for bulls 
        
        #To get player one's input, in order to guess the code
        Guess_Player_One=input(str(Nickname_Player_One)+', enter guess:\n')
        
        #This loop calcutes the bull points
        while bull_index<3:
            #Checking for the correct character at correct position
            if Guess_Player_One[bull_index]==Code_Player_Two[bull_index]: 
                bull_points +=1
            if bull_points==3: #If player one guess the code
                print(Nickname_Player_One,'wins!')
                exit(0)
            bull_index +=1
        
        #This loop calcutes the cow points
        while cows_index<3:
            cows_index_2=0 
            #Checking for the correct character at different position
            while cows_index_2<3:
                if (Guess_Player_One[cows_index]==Code_Player_Two[cows_index_2] and 
                cows_index != cows_index_2):
                    cows_points+=1
                cows_index_2+=1
            cows_index +=1
        print('  * bulls:',bull_points)
        print('  * cows: ',cows_points)
        main_index = 1 #To fail the loop and give the second player a chance 

    while main_index==1: 
        cows_index=0 #To controll the loops for cows   
        bull_index=0#To controll the loops for cows   
        cows_points=0 #To count points for cows 
        bull_points=0 #To count points for bulls 
        
        #To get player two's input, in order to guess the code
        Guess_Player_Two=input(str(Nickname_Player_Two)+', enter guess:\n')
        
        #This loop calcutes the bull points
        while bull_index<3:
            #Checking for the correct character at correct position
            if Guess_Player_Two[bull_index]==Code_Player_One[bull_index]: 
                bull_points +=1
            if bull_points==3: #If player one guess the code
                print(Nickname_Player_Two,'wins!')
                exit(0)
            bull_index +=1
        
        #This loop calcutes the cow points
        while cows_index<3:
            cows_index_2=0 
            #Checking for the correct character at different position
            while cows_index_2<3:
                if (Guess_Player_Two[cows_index]==Code_Player_One[cows_index_2] and 
                cows_index != cows_index_2):
                    cows_points+=1
                cows_index_2+=1
            cows_index +=1
        print('  * bulls:',bull_points)
        print('  * cows: ',cows_points)
        main_index = 0 #To fail the loop and give the frist player a chance 