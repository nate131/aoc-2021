import csv
import os
import time

def main():
    startTime = time.time()
    print(os.path.dirname(os.path.realpath(__file__)))
    with open(os.path.dirname(os.path.realpath(__file__))+'/input.txt', 'r') as f:
        content = [int(line.rstrip()) for line in f]
    print("Part 1:" + part1(content))
    print("Part 2:" + part2(content))
    print ('[Finished in {:.5f}s]'.format(time.time() - startTime))

def part1(content):
    counter = 0
    for i in range(len(content)):
        if i==0:
            buffer = content[i]
            continue
        if content[i] > buffer:
            counter+=1
        buffer = content[i]
    return str(counter)

def part2(content):
    counter = 0
    for i in range(len(content)-3):
        if i==0:
            buffer = content[i] + content[i+1] + content[i+2]
            continue
        if content[i] + content[i+1] + content[i+2] > buffer:
            counter+=1
        buffer = content[i] + content[i+1] + content[i+2]
    return str(counter)

if __name__ == "__main__":
    main()