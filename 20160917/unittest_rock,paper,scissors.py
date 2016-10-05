import unittest
from random import randint


class TestComputerChoice(unittest.TestCase):
    def test_computer_choice(self):
        computer_choice = ComputerChoice()
        return computer_choice.computer_chose()
        

class ComputerChoice :
    def computer_chose (self):
        computer_chose = randint(1,3)
        if computer_chose == 1:
            print('computer chose rock')
        elif computer_chose == 2:
            print ('computer chose paper')
        else:
            print('computer chose scissors')


class TestUserChoice(unittest.TestCase):
    def test_user_choice(self):
        user_choice = UserChoice()
        return user_choice.user_move()

class UserChoice :
    user_choice = int(input('Rock, Paper,Scissors? '))

    def user_move(self):
        rock = 1
        paper = 2
        scissors = 3
        

        def rock_option():
            if user_move == 1:
                print('it is a tie')
            elif user_move == 2:
                print('you win')
            else :
                print('you lose')
                    
            
        def paper_option():
            if user_move == 1:
                print('you lose')
            elif user_move == 2:
                print('it is a tie')
            else :
                print('you win')

        def scissors_option():
            if user_move == 1:
                print('you win')
            elif user_move == 2:
                print('you lose')
            else :
                print('it is a tie')


    for option in range (1,3):
        if user_choice > 3:
            print ('Select\n 1 for rock \n 2 for paper \n 3 for scissors')

            break





        if user_choice == 0:
            return False
        else:
            return True


while user_move():
    print('')






if __name__ == '__main__':
    unittest.main()
