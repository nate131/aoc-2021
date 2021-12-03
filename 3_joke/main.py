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
        content = [line.rstrip() for line in f]
    
    print(Fore.GREEN)
    tprint('Aoc Day 3 Joke' + "\U0001F385")
    print(Fore.CYAN + Back.RESET)
    print(Fore.BLUE + tabulate.tabulate([["Part 1: ", part1(content)],["Part 2: ", part2(content)]]))
    print (Style.RESET_ALL + '[Finished in {:.4f}ms]'.format(1000*(time.time() - startTime)),"\U0001F605")

def part1(content):
    known_good = []
    start=0
    starting_number = start
    for i in tqdm(range(5438112790695821312),ncols=120,desc="Part 1 \U0001F914",unit_scale=False):
        for j in range(1000):
            current_number = starting_number + 1
            starting_number = current_number
            iterations = 0
            while iterations < 1000000000:
                iterations = iterations + 1
                if current_number in known_good:
                    known_good.append(starting_number)
                    break
                if current_number % 2 == 0:
                    current_number = current_number/2
                else:
                    current_number = (current_number * 3) + 1
                if current_number == 1:
                    known_good.append(starting_number)
                    break
                if iterations == 1000000000:
                    print(str(starting_number) + "too many iterations!!")


def part2(content):
    return "1"

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(Fore.CYAN + Back.RED)
        print("Good job idiot, here is a medal: \U0001F3C5")
        raise(e)
