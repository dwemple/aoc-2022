input = open("2_input.txt", 'r')
result = 0
result_two = 0
def getMyScore(me):
    global result
    if me == 'X':
        result += 1
    elif me == 'Y':
        result += 2
    elif me == 'Z':
        result += 3

def getScoreRock(me):
    global result
    if me == 'X':
        result += 3
    elif me == 'Y':
        result += 6
    
def getScorePaper(me):
    global result
    if me == 'Y':
        result += 3
    elif me == 'Z':
        result += 6

def getScoreScissor(me):
    global result
    if me == 'Z':
        result += 3
    elif me == 'X':
        result += 6
def getSecondRock(me):
    global result_two
    if me == 'X':
        result_two += 3
    elif me == 'Y':
        result_two += 1 + 3
    else:
        result_two += 2 + 6
def getSecondPaper(me):
    global result_two
    if me == 'X':
        result_two += 1
    elif me == 'Y':
        result_two += 2 + 3
    else:
        result_two += 3 + 6
def getSecondScissor(me):
    global result_two
    if me == 'X':
        result_two += 2
    elif me == 'Y':
        result_two += 3 + 3
    else:
        result_two += 1 + 6    


enemy, us = [], []
for i in input:
    enemy.append(i[0])
    us.append(i[2])

counter = 0
for i in enemy:
    if i == 'A':
        getScoreRock(us[counter])
        getSecondRock(us[counter])
    elif i == 'B':
        getSecondPaper(us[counter])
        getScorePaper(us[counter])
    elif i == 'C':
        getSecondScissor(us[counter])
        getScoreScissor(us[counter])

    getMyScore(us[counter])
    counter = counter + 1
    
print(str(result))
print(str(result_two))