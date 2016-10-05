def check_age():
    age =  int (input('How old are you? ' ))

    print (age)

    if age < 18:
        print ('Hello youngstar')

    elif age < 30:
        print ('Hello student')  

    elif age < 60 and age >= 30 :
            print ('Hello middle age')
            
    else:
        print ('Hello pensioner')

    if age == 0:
        return False
    else:
        return True


while check_age():
    print('')


