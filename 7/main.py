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
        content = [int(i) for i in f.read().split(",")]
    
    print(Fore.GREEN)
    tprint('Aoc Day 7' + "\U0001F385")
    print(Fore.CYAN + Back.RESET)
    print(Fore.BLUE + tabulate.tabulate([["Part 1: ", part1(content)],["Part 2: ", part2(content)]]))
    print (Style.RESET_ALL + '[Finished in {:.4f}ms]'.format(1000*(time.time() - startTime)),"\U0001F605")

def part1(content):
    min_fuel = 0
    for i in tqdm(range(min(content),max(content)+1),ncols=90,desc="Part 1 \U0001F914",unit_scale=True):
        fuel = 0
        for crab_pos in content:
            distance = abs(crab_pos - i)
            fuel = fuel + distance
            #fuel = fuel + sum(range(1,abs(crab_pos - i)+1))
        if fuel < min_fuel or i == 0: min_fuel = fuel
    return min_fuel

def part2(content):
    min_fuel = 0
    for i in tqdm(range(min(content),max(content)+1),ncols=90,desc="Part 2 \U0001F914",unit_scale=True):
        fuel = 0
        for crab_pos in content:
            distance = abs(crab_pos - i)
            fuel = fuel + ((distance * (distance+1))//2)
            #fuel = fuel + sum(range(1,abs(crab_pos - i)+1))
        if fuel < min_fuel or i == 0: min_fuel = fuel
    return min_fuel


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(Fore.CYAN + Back.RED)
        print("Good job idiot, here is a medal: \U0001F3C5")
        raise(e)
