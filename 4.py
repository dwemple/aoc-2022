input = open("4_input.txt", 'r')
resultOne,resultTwo  = 0,0
for i in input:
    one, two = i.split(',', 2)
    sOne, eOne = one.split('-', 2)
    sTwo, eTwo = two.split('-', 2)
    if ((int(sOne) <= int(sTwo) and int(eOne) >= int(eTwo))
    or (int(sTwo) <= int(sOne) and int(eTwo) >= int(eOne))):
        resultOne += 1
    if (int(eOne) >= int(sTwo) and int(sOne) <= int(sTwo)) or (int(eTwo) >= int(sOne) and int(sTwo) <= int(sOne)):
        resultTwo += 1
print(resultOne)   
print(resultTwo)   
# 976 too hight