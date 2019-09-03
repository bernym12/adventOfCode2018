from itertools import cycle
'''
input: Takes in the the text file, parses it,
and ouputs the numbers in a list
'''
def readFile(input_text):
    with open(input_text,'r') as f:
        input = [int(x.strip('\n')) for x in f.readlines()]
    return input

input = readFile('input.txt')
print('Part 1: ', sum(input))

input = cycle(input)
vals = {}
numb = next(input)
while(True):
    numb += next(input)
    if numb in vals.keys():
        print("Part 2: ", numb)
        vals[numb] += 1
        break
    else:
        vals.update({numb : 1})