craftsmen = ['Johannes','Florah','Collen','Emmanuel','Vuyisile','Tefo','Wiseman']
print(craftsmen[0])

craftsmen.append('Xolani')
print (craftsmen)

del craftsmen[2], craftsmen[0]
print(craftsmen)


craftsmen[0] = 20
print (craftsmen)

for name in craftsmen:
    print ("Hello I am " + str(name))
