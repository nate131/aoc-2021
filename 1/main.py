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
        content = [int(line.rstrip()) for line in f]
    
    print(Fore.GREEN)
    tprint('Aoc Day 1' + '\U0001F385')
    print(Fore.CYAN + Back.RESET)
    print(Fore.BLUE + tabulate.tabulate([["Part 1: ", part1(content)],["Part 2: ", part2(content)]]))
    print (Style.RESET_ALL + '[Finished in {:.10f}s]'.format(time.time() - startTime),"\U0001F605")

def part1(content):
    counter = 0
    for i in tqdm(range(len(content)),ncols=90,desc="Part 1 \U0001F914",unit_scale=True):
        if i==0:
            buffer = content[i]
            continue
        if content[i] > buffer:
            counter+=1
        buffer = content[i]
        #time.sleep(0.001)
    return str(counter)

def part2(content):
    counter = 0
    for i in tqdm(range(len(content)-3),ncols=90,desc="Part 2 \U0001F914",unit_scale=True):
        if i==0:
            buffer = content[i] + content[i+1] + content[i+2]
            continue
        if content[i] + content[i+1] + content[i+2] > buffer:
            counter+=1
        buffer = content[i] + content[i+1] + content[i+2]
        #time.sleep(0.001)
    return str(counter)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(Fore.CYAN + Back.RED)
        print("Good job idiot, here is a medal: \U0001F3C5")
        raise(e)
