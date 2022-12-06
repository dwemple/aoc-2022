with open("6_input.txt", 'r') as f:
    input = f.read()

flag = True
firstMarker = ""
counter = 0
for i in input:
    # change counter to 3 for part 1
    if counter > 13:
        firstMarker = firstMarker[1:] + i
        for k in firstMarker:
            if(firstMarker.count(k)) > 1:
                flag = False
                break
        if flag:
            print(counter+1)
            exit(0)
        flag = True
    else:
        firstMarker += i
    counter += 1
    