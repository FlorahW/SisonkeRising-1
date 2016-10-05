from random import randint

def RPS():

    user_choice = int(input('Rock, Paper,Scissors? '))

    rock = 1
    paper = 2
    scissors = 3


    def computer_choice ():
        computer_choice = randint(1,3)
        
        if computer_choice == 1:
            print ("computer chose rock")
        elif computer_choice == 2:
            print ("computer chose paper")
        else:
            print("computer chose scissors")

            return computer_choice
   
                
    def rock_option ():
        if user_choice == 1:
           print ('it is a tie')
        elif user_choice == 2:
            print ('you lose')
        else:
            print ('you win')

    

    for option in range (1,3):
        if user_choice < 1 or user_choice > 3:
            print ('Select\n 1 for rock \n 2 for paper \n 3 for scissors')

            break
    

    if RPS == 0:
        return False
    else :
        return True 

while RPS ():
    print ('')
               

