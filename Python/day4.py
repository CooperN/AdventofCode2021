import pathlib
import pandas as pd

filepath = pathlib.Path(__file__).parent.parent.joinpath("Inputs/day4.txt")
raw_data = open(filepath).read()
data = raw_data.split('\n\n')
drawnNumbers = data.pop(0)
card = []
blankcard = pd.DataFrame([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
cards = []
calledcards = []
for line in data:
    for row in line.split('\n'):
        card.append(list(map(int,row.split())))
    cards.append(pd.DataFrame(card))
    calledcards.append(blankcard)
    card = []

i=0

for num in drawnNumbers:
    i=0
    for card in cards:
        card[:] = card.replace(num,"x")
        




test2 = cards[0].isin([31])
test3 = cards[0].replace(31,"x")

testcard = pd.DataFrame([['x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x']])
pos = testcard*test2
print(test2)
print(test3)




