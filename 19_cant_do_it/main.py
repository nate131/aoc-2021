import csv
import os
import time
from tqdm import tqdm
import tabulate
from art import tprint
from colorama import Fore, Style, Back
import copy
import re
import numpy as np

def main():
    startTime = time.time()
    with open(os.path.dirname(os.path.realpath(__file__))+'/input.txt', 'r') as f:
        content = f.read().split("\n\n")
    
    print(Fore.GREEN)
    tprint('Aoc Day '+ os.path.basename(os.path.dirname(os.path.realpath(__file__))) + "\U0001F385")
    print(Fore.CYAN + Back.RESET)
    print(Fore.BLUE + tabulate.tabulate([["Part 1: ", part1(content)],["Part 2: ", part2(content)]]))
    print (Style.RESET_ALL + '[Finished in {:.4f}ms]'.format(1000*(time.time() - startTime)),"("+format((round(time.time() - startTime,2)))+"s)","\U0001F605")

def rotations(scanner):
    rots = []
    for i in range(24):
        rots.append([])
    for coord in scanner:
        #positive x
        rots[ 0].append((+coord[0],+coord[1],+coord[2]))
        rots[ 1].append((+coord[0],-coord[2],+coord[1]))
        rots[ 2].append((+coord[0],-coord[1],-coord[2]))
        rots[ 3].append((+coord[0],+coord[2],-coord[1]))
        #negative x
        rots[ 4].append((-coord[0],-coord[1],+coord[2]))
        rots[ 5].append((-coord[0],+coord[2],+coord[1]))
        rots[ 6].append((-coord[0],+coord[1],-coord[2]))
        rots[ 7].append((-coord[0],-coord[2],-coord[1]))
        #positive y
        rots[ 8].append((+coord[1],+coord[2],+coord[0]))
        rots[ 9].append((+coord[1],-coord[0],+coord[2]))
        rots[10].append((+coord[1],-coord[2],-coord[0]))
        rots[11].append((+coord[1],+coord[0],-coord[2]))
        #negative y
        rots[12].append((-coord[1],-coord[2],+coord[0]))
        rots[13].append((-coord[1],+coord[0],+coord[2]))
        rots[14].append((-coord[1],+coord[2],-coord[0]))
        rots[15].append((-coord[1],-coord[0],-coord[2]))
        #positive z
        rots[16].append((+coord[2],+coord[0],+coord[1]))
        rots[17].append((+coord[2],-coord[1],+coord[0]))
        rots[18].append((+coord[2],-coord[0],-coord[1]))
        rots[19].append((+coord[2],+coord[1],-coord[0]))
        #negative z
        rots[20].append((-coord[2],-coord[0],+coord[1]))
        rots[21].append((-coord[2],+coord[1],+coord[0]))
        rots[22].append((-coord[2],+coord[0],-coord[1]))
        rots[23].append((-coord[2],-coord[1],-coord[0]))
    return rots

def attempt_match(scanner1,scanner_list):
    for scanner2 in scanner_list:
        for sc2rot in scanner2:
            for sc2point in sc2rot:
                

def part1(content):
    data = {}
    for scanner,coords in enumerate(content):
        data[scanner] = [[int(y) for y in x.split(",")] for x in coords.split("\n")[1:]]
    print(data)
    all_scanners = []
    for num,scanner in enumerate(data.values()):
        print(scanner)
        all_scanners.append(rotations(scanner))
    
    attempt_match(all_scanners[0],all_scanners[1:])
    
    print(all_scanners)
    return False

def part2(content):
    return False


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(Fore.CYAN + Back.RED)
        print("Good job idiot, here is a medal: \U0001F3C5")
        raise(e)
