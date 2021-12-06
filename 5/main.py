import csv
import os
import time
from tqdm import tqdm
import tabulate
from art import tprint
from colorama import Fore, Style, Back
import copy
import re

def main():
    startTime = time.time()
    with open(os.path.dirname(os.path.realpath(__file__))+'/input.txt', 'r') as f:
        content = f.read().split("\n")
    
    print(Fore.GREEN)
    tprint('Aoc Day 5' + "\U0001F385")
    print(Fore.CYAN + Back.RESET)
    print(Fore.BLUE + tabulate.tabulate([["Part 1: ", part1(content)],["Part 2: ", part2(content)]]))
    print (Style.RESET_ALL + '[Finished in {:.4f}ms]'.format(1000*(time.time() - startTime)),"\U0001F605")

def part1(content):
    # parse line to groups
    pattern = r"(?P<x1>\d+),(?P<y1>\d+) -> (?P<x2>\d+),(?P<y2>\d+)"
    matrix = {}
    for i,line in enumerate(tqdm(content,ncols=90,desc="Part 1 \U0001F914",unit_scale=True)):
        if len(line) > 1:
            m = re.search(pattern,line)
            #print(i)
            minx = int(m.group("x1"))
            maxx = int(m.group("x2"))
            miny = int(m.group("y1"))
            maxy = int(m.group("y2"))
            # find if increment or decrement 
            xmod = 1 if minx <= maxx else -1
            ymod = 1 if miny <= maxy else -1
            # skip if diagonal
            if minx == maxx or miny == maxy:
                # loop over lines and add x,y to dictionary (+1 each time to find crossing lines)
                for j in range(minx,maxx+xmod,xmod):
                    for k in range(miny,maxy+ymod,ymod):
                        key = str(j)+","+str(k)
                        if matrix.get(key):
                            matrix[key] = matrix[key] + 1
                        else:
                            matrix[key] = 1
    answer = 0
    for k,v in matrix.items():
        if v > 1:
            answer = answer + 1
    return answer

def part2(content):
    # parse line to groups
    pattern = r"(?P<x1>\d+),(?P<y1>\d+) -> (?P<x2>\d+),(?P<y2>\d+)"
    matrix = {}
    for i,line in enumerate(tqdm(content,ncols=90,desc="Part 2 \U0001F914",unit_scale=True)):
        if len(line) > 1:
            m = re.search(pattern,line)
            minx = int(m.group("x1"))
            maxx = int(m.group("x2"))
            miny = int(m.group("y1"))
            maxy = int(m.group("y2"))
            # find if increment or decrement 
            xmod = 1 if minx <= maxx else -1
            ymod = 1 if miny <= maxy else -1
            # skip if diagonal
            if minx == maxx or miny == maxy:
                # loop over lines and add x,y to dictionary (+1 each time to find crossing lines)
                for j in range(minx,maxx+xmod,xmod):
                    for k in range(miny,maxy+ymod,ymod):
                        key = str(j)+","+str(k)
                        if matrix.get(key):
                            matrix[key] = matrix[key] + 1
                        else:
                            matrix[key] = 1
            # if line diagonal
            else:
                diff = abs(minx - maxx)
                # increment/decrement using x/ymod once per line length and add to x,y dictionary
                for c in range(diff+1):
                    key = str(minx)+","+str(miny)
                    if matrix.get(key):
                        matrix[key] = matrix[key] + 1
                    else:
                        matrix[key] = 1
                    minx = minx + xmod
                    miny = miny + ymod
    answer = 0
    # answer is count of dictionary elements where value > 1
    for k,v in matrix.items():
        if v > 1:
            answer = answer + 1
    return answer


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(Fore.CYAN + Back.RED)
        print("Good job idiot, here is a medal: \U0001F3C5")
        raise(e)
