import pathlib
filepath = pathlib.Path(__file__).parent.parent.joinpath("Inputs/day3.txt")
raw_data = open(filepath).read()
data = raw_data.split('\n')
directions = [[int(char) for char in i] for i in data]

def most_used_num(list):
    answerArray = [0,0,0,0,0,0,0,0,0,0,0,0]
    popperlist = directions[:]
    num = 0
    for line in list:
        for i in line:
            if(i == 1):
                answerArray[num] += 1
            elif(i ==0):
                answerArray[num] -= 1
            num += 1
        num = 0
    return answerArray

def getoandl(list):
    answerArray = [0,0,0,0,0,0,0,0,0,0,0,0]
    i = 0
    for num in list:
        if(num>0):
            answerArray[i] = 1
        elif(num<0):
            answerArray[i] = 0
        elif(num==0):
            answerArray[i] = 1
        else:
            answerArray[i] = "you fucked up"
        i+=1
    return answerArray

def flipnum(list):
    i = 0
    answerArray = [0,0,0,0,0,0,0,0,0,0,0,0]
    for char in list:
        if(char == 1):
            answerArray[i] = 0
        elif(char == 0):
            answerArray[i] = 1 
        i+=1
    return answerArray

def converttostring(list):
    hastobestring = ""
    for char in list:
        hastobestring+=str(char)
    return hastobestring
    
def checkmostusedcharacterrolling(list):
    answerArray = [0,0,0,0,0,0,0,0,0,0,0,0]
    num = 0
    popperlist = list[:]
    while(len(popperlist)>1):
        for line in popperlist:
            if(line[num] == 1):
                answerArray[num] += 1
            elif(line[num] ==0):
                answerArray[num] -= 1
        answerArray = getoandl(answerArray)
        for line in reversed(popperlist):
            if(line[num] != answerArray[num]):
                popperlist.remove(line)
        answerArray = [0,0,0,0,0,0,0,0,0,0,0,0]
        num += 1
    return popperlist[0]

def checkleaseusedcharacterrolling(list):
    answerArray = [0,0,0,0,0,0,0,0,0,0,0,0]
    num = 0
    popperlist = list[:]
    while(len(popperlist)>1):
        for line in popperlist:
            if(line[num] == 1):
                answerArray[num] += 1
            elif(line[num] ==0):
                answerArray[num] -= 1
        answerArray = getoandl(answerArray)
        for line in reversed(popperlist):
            if(line[num] == answerArray[num]):
                popperlist.remove(line)
        answerArray = [0,0,0,0,0,0,0,0,0,0,0,0]
        num += 1
    return popperlist[0]


testans = most_used_num(directions)
resultuno = getoandl(testans)
resultunodos = flipnum(resultuno)
gamma = int(converttostring(resultuno), 2)
epsilon = int(converttostring(resultunodos), 2)

print('Answer 1: ' + str(epsilon*gamma))

oxygen = int(converttostring(checkmostusedcharacterrolling(directions)), 2)
codos = int(converttostring(checkleaseusedcharacterrolling(directions)), 2)


print('Answer 2: ' + str(oxygen*codos))
