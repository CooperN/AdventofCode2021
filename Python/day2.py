import pathlib
filepath = pathlib.Path(__file__).parent.parent.joinpath("Inputs/day2.txt")
raw_data = open(filepath).read()
data = raw_data.split('\n')
directions = [i.split() for i in data]

horizontal = 0
depth = 0

for i in directions:
    if(i[0] ==  'forward'):
        horizontal += int(i[1])
    elif(i[0] ==  'down'):
        depth += int(i[1])
    elif(i[0] ==  'up'):
        depth -= int(i[1])
print('Horizontal: ' + str(horizontal))
print('Depth: ' + str(depth))
print('First Answer: ' + str(horizontal*depth))

aim = 0
depth = 0
horizontal = 0

for i in directions:
    if(i[0] ==  'forward'):
        horizontal += int(i[1])
        depth += int(i[1])*aim
    elif(i[0] ==  'down'):
        aim += int(i[1])
    elif(i[0] ==  'up'):
        aim -= int(i[1])
print('Depth: ' + str(depth))
print('aim: ' + str(aim))
print('Second Answer: ' + str(horizontal*depth))