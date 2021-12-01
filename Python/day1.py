import io
import pathlib
filepath = pathlib.Path(__file__).parent.parent.joinpath("Inputs/day1.txt")
raw_data = open(filepath).read()
data = raw_data.split('\n')
data = [int(i) for i in data]

n=999999999999999999999999
num = 0
count = 0
test = None
for i in data:
    if n<i:
        count+=1
    n = i
print("first answer = " + str(count))
i = 0
countb = 0
while i < len(data)-3:
    numa = data[i] + data[i+1] + data[i+2]
    numb = data[i+1] + data[i+2] + data[i+3]
    if numa<numb:
        countb +=1
    i+=1
print("second answer = " + str(countb))

"""     if num+1 < len(data):
        if data[num] < data[num+1]:
            count += 1
            print(str(num) + ' + ' + str(num+1) + " + " + " next ")
            if test is None:
                 test = (str(data[num]) + ' + ' + str(data[num+1]) + " + " + "next")
        num += 1 """


