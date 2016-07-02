craftsmen = ['Johannes','Florah','Collen','Emmanuel','Vuyisile','Tefo','Wiseman']
print(craftsmen[0])

last_names = ['Parker','Weni','Chuene','Mashaba','Mathews','Phoko','Zulu']


'''craftsmen.append('Xolani')
print (craftsmen)

del craftsmen[2], craftsmen[0]
print(craftsmen)


craftsmen[0] = 20
print (craftsmen)'''

for name,last in zip(craftsmen,last_names):
    print ("Hello I am {0} {1} " .format(name,last))


