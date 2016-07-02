craftsmen = ['Johannes','Florah','Collen','Emmanuel','Vuyisile','Tefo','Wiseman']
print(craftsmen[0])

last_names = ['Parker','Weni','Chuene','Mashaba','Mathews','Phoko','Zulu']

ages = [15,25,20,10,17,19,20]


'''craftsmen.append('Xolani')
print (craftsmen)

del craftsmen[2], craftsmen[0]
print(craftsmen)


craftsmen[0] = 20
print (craftsmen)'''

for name,last,age in zip(craftsmen,last_names,ages):
    print ("Hello I am {0} {1} \n I am {2} old" .format(name,last,age))


