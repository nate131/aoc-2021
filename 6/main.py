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
        content = f.read().split(",")
    
    print(Fore.GREEN)
    tprint('Aoc Day 6' + "\U0001F385")
    print(Fore.CYAN + Back.RESET)
    ans = part2(content)
    print(Fore.BLUE + tabulate.tabulate([["Part 1: ", ans[0]],["Part 2: ", ans[1]]]))
    print (Style.RESET_ALL + '[Finished in {:.4f}ms]'.format(1000*(time.time() - startTime)),"\U0001F605")

def part1(content):
    # Fish generation via list mapping
    p1_con = content.copy()
    for day in tqdm(range(0,80),ncols=90,desc="Part 1 \U0001F914",unit_scale=True):
        for i,t in enumerate(p1_con):
            t = int(t)
            if t == 0:
                p1_con[i] = 6
                p1_con.append('9')
            else:
                p1_con[i] = int(p1_con[i]) - 1
    #print(len(p1_con))
    return len(p1_con)

def part2(content,iterate_count=256):
    answer=[]
    # Fish generation via counter array
    p2_con = content.copy()
    timers=[]
    # Map current fish into counter array (key=timer,val=count)
    for i in range(9):
        timers.append(content.count(str(i)))
    # Generate fish per day (move 0th element to end of list and copy it to 6th timer as per rules)
    for day in tqdm(range(0,iterate_count),ncols=90,desc="Part 2 \U0001F914",unit_scale=True):
        timers.append(timers.pop(0))
        timers[6] = timers[6] + timers[8]
        if day == 79: answer.append(sum(timers))
    answer.append(sum(timers))
    #print(answer)
    return answer


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(Fore.CYAN + Back.RED)
        print("Good job idiot, here is a medal: \U0001F3C5")
        raise(e)
