input = open("5_input.txt", 'r')
regex = 0
stacks = [[] for _ in range(9)]
instructions = []
for i in input:
    if regex <= 9:
        if regex < 8:
            for k in range(0,9):
                stacks[k].append(i[4*k+1])
        regex += 1
    else:
        split = i.split(' ', 6)
        split[5] = split[5].strip('\n')
        instructions.append([int(split[1]), int(split[3]), int(split[5])])
for items in stacks:
    while(' ' in items):
        items.remove(' ')
for i in instructions:
    #print("Instruction: move " + str(i[0]) + " amount of items from " + str(i[1]) + " to " + str(i[2]))
    #print("------ Pre:")
    #print(str(i[1]) + ": " + str(stacks[i[1]-1]))
    #print(str(i[2]) + ": " + str(stacks[i[2]-1]))
    temp = []
    for k in range(0, i[0]):
    # part 1
    #    stacks[i[2]-1].insert(0, stacks[i[1]-1].pop(0))
    # part 2
        temp.append(stacks[i[1]-1].pop(0))
    stacks[i[2]-1] = temp + stacks[i[2]-1]
    temp.clear()
    # end of part 2
    #print("------ Post:")
    #print(str(i[1]) + ": " + str(stacks[i[1]-1]))
    #print(str(i[2]) + ": " + str(stacks[i[2]-1]))

result = ""
for i in stacks:
    result += i[0]
    print(i)

print(result)

# wrong QPJPLRNNP


