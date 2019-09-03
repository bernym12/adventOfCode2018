def readFile(input_text):
    with open(input_text,'r') as f:
        input = [x.strip('\n') for x in f.readlines()]
    return input

''' 
if string has 2 of one letter increment a count.
if string has 3 of one letter, increment a sep. count.
if string has both forms, incr. both counts.
each type can only count once per word.
'''

def part1():
    input = readFile('input.txt')
    twos = 0
    threes = 0
    for word in input:
        two_for_word = 0
        three_for_word = 0
        for letter in word:
            if (word.count(letter) == 2) and (two_for_word == 0):
                twos += 1
                two_for_word = 1
            elif (word.count(letter) == 3) and (three_for_word == 0):
                threes += 1
                three_for_word = 1
    print('Checksum: ', twos*threes)


if __name__=='__main__':
    part1()