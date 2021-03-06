import csv
import os
import time
from tqdm import tqdm
import tabulate
from art import tprint
from colorama import Fore, Style, Back

def main():
    startTime = time.time()
    with open(os.path.dirname(os.path.realpath(__file__))+'/input.txt', 'r') as f:
        content = [line.split(" ") for line in f]
    
    print(Fore.GREEN)
    tprint('Aoc Day 2' + "\U0001F385")
    print(Fore.CYAN + Back.RESET)
    print(Fore.BLUE + tabulate.tabulate([["Part 1: ", part1(content)],["Part 2: ", part2(content)]]))
    print (Style.RESET_ALL + '[Finished in {:.4f}ms]'.format(1000*(time.time() - startTime)),"\U0001F605")

def part1(content):
    x, y = 0, 0
    for i in tqdm(range(len(content)),ncols=90,desc="Part 1 \U0001F914",unit_scale=True):
        command, value = content[i][0], int(content[i][1])
        if command == "forward": x = x + value
        elif command == "down": y = y + value
        elif command == "up": y = y - value
    return str(x*y)

def part2(content):
    x, y, z = 0, 0 ,0
    for i in tqdm(range(len(content)),ncols=90,desc="Part 2 \U0001F914",unit_scale=True):
        command, value = content[i][0], int(content[i][1])
        if command == "forward":
            x = x + (value)
            z = z + (value * y)
        elif command == "down": y = y + value
        elif command == "up": y = y - value
    return str(x*z)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(Fore.CYAN + Back.RED)
        print("Good job idiot, here is a medal: \U0001F3C5")
        raise(e)
