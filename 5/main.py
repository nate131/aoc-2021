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
    for i,line in enumerate(content):
        m = re.search(pattern,line)
        # find if increment or decrement 
        if int(m.group("x1")) <= int(m.group("x2")):
            xmod = 1
        else:
            xmod = -1
        if int(m.group("y1")) <= int(m.group("y2")):
            ymod = 1
        else:
            ymod = -1
        # skip if diagonal
        if m.group("x1") == m.group("x2") or m.group("y1") == m.group("y2"):
            # loop over lines and add x,y to dictionary (+1 each time to find crossing lines)
            for j in range(int(m.group("x1")),int(m.group("x2"))+xmod,xmod):
                for k in range(int(m.group("y1")),int(m.group("y2"))+ymod,ymod):
                    if matrix.get(str(j)+","+str(k)):
                        matrix[str(j)+","+str(k)] = matrix[str(j)+","+str(k)] + 1
                    else:
                        matrix[str(j)+","+str(k)] = 1
    answer = 0
    for k,v in matrix.items():
        if v > 1:
            answer = answer + 1
    return answer

def part2(content):
    # parse line to groups
    pattern = r"(?P<x1>\d+),(?P<y1>\d+) -> (?P<x2>\d+),(?P<y2>\d+)"
    matrix = {}
    for i,line in enumerate(content):
        m = re.search(pattern,line)
        # find if increment or decrement 
        if int(m.group("x1")) <= int(m.group("x2")):
            xmod = 1
        else:
            xmod = -1
        if int(m.group("y1")) <= int(m.group("y2")):
            ymod = 1
        else:
            ymod = -1
        # if line not diagonal use p1 logic
        if m.group("x1") == m.group("x2") or m.group("y1") == m.group("y2"):
            for j in range(int(m.group("x1")),int(m.group("x2"))+xmod,xmod):
                for k in range(int(m.group("y1")),int(m.group("y2"))+ymod,ymod):
                    if matrix.get(str(j)+","+str(k)):
                        matrix[str(j)+","+str(k)] = matrix[str(j)+","+str(k)] + 1
                    else:
                        matrix[str(j)+","+str(k)] = 1
        # if line diagonal
        else:
            minx = int(m.group("x1"))
            maxx = int(m.group("x2"))
            miny = int(m.group("y1"))
            maxy = int(m.group("y2"))
            diff = abs(minx - maxx)
            # increment/decrement using x/ymod once per line length and add to x,y dictionary
            for c in range(diff+1):
                if matrix.get(str(minx)+","+str(miny)):
                    matrix[str(minx)+","+str(miny)] = matrix[str(minx)+","+str(miny)] + 1
                else:
                    matrix[str(minx)+","+str(miny)] = 1
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
