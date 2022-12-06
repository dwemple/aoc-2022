input = open("3_input.txt", 'r')
first, second = [], []
result = ""
temp = []
for i in input:
    size1 = int((len(i)) / 2)
    first = i[:size1]
    second = i[size1:]
    for k in first:
        for j in second:
            if k == j:
                temp.append(k)
    result += temp[0]
    temp.clear()

firstgroup = []
secondgroup = []
char = ""
cher = ""
res = ""
tempo = 0

hey = open("3_input.txt", 'r')
for i in hey:
    if tempo < 3:
        firstgroup.append(i)
    elif tempo < 6:
        secondgroup.append(i)

    if tempo == 5:
        for f in firstgroup[0]:
            if (firstgroup[1].find(f) != -1 and
            firstgroup[2].find(f) != -1):
                char += f
        for f in secondgroup[0]:
            if (secondgroup[1].find(f) != -1 and
            secondgroup[2].find(f) != -1):
                cher += f
        
        res += char[0]
        res += cher[0]
        char = ""
        cher = ""
        firstgroup.clear()
        secondgroup.clear()
        tempo = -1
        
    tempo += 1


counter = 0
triples = 0
transform = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for a in result:
    counter += transform.find(a) + 1
for a in res:
    triples += transform.find(a) + 1
print(counter)
print(triples)