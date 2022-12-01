input = open("1_input.txt", 'r')
x = 0
list = []
for i in input:
    if i != '\n':
        x = x + int(i)
    else:
        list.append(x)
        x = 0

biggest, second, smallest = 0, 0, 0
for i in list:
    if i > biggest:
        smallest = second
        second = biggest
        biggest = i
    elif i > second:
        smallest = second
        second = i
    elif i > smallest:
        smallest = i


print("Biggest: " + str(biggest))
print("First three top: " + str(biggest + second + smallest))