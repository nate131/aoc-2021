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
    tprint('Aoc Day 11' + "\U0001F385")
    print(Fore.CYAN + Back.RESET)
    print(Fore.BLUE + tabulate.tabulate([["Part 1: ", part1(copy.deepcopy(content))],["Part 2: ", part2(copy.deepcopy(content))]]))
    print (Style.RESET_ALL + '[Finished in {:.4f}ms]'.format(1000*(time.time() - startTime)),"\U0001F605")

def flash(x,y,content):
    to_check = [[x-1,y-1],[x-1,y],[x-1,y+1],[x,y-1],[x,y+1],[x+1,y-1],[x+1,y],[x+1,y+1]]
    for check in to_check:
        if 0 <= check[0] < len(content):
            if 0 <= check[1] < len(content[0]):
                content[check[0]][check[1]] += 1
    return content

def part1(content):
    for x,xval in enumerate(content):
        content[x] = [int(vals) for vals in xval]
    flashed_count = 0
    for generations in range(100):
        for x,xval in enumerate(content):
            for y,yval in enumerate(content[x]):
                content[x][y] += 1
        flashed_at_all = True
        already_flashed = []
        while flashed_at_all:
            flashed_at_all = False
            for x,xval in enumerate(content):
                for y,yval in enumerate(content[x]):
                    if content[x][y] > 9 and [x,y] not in already_flashed:
                        flashed_at_all = True
                        already_flashed.append([x,y])
                        flashed_count += 1
                        content = flash(x,y,content)
                        break
                if flashed_at_all: break
        for x,xval in enumerate(content):
            for y,yval in enumerate(content[x]):
                if content[x][y] > 9:
                    content[x][y] = 0
    return flashed_count

def part2(content):
    for x,xval in enumerate(content):
        content[x] = [int(vals) for vals in xval]
    generations = 0
    flashed_count = 0
    while flashed_count != (len(content) * len(content[0])):
        generations += 1
        flashed_count = 0
        for x,xval in enumerate(content):
            for y,yval in enumerate(content[x]):
                content[x][y] += 1
        flashed_at_all = True
        already_flashed = []
        while flashed_at_all:
            flashed_at_all = False
            for x,xval in enumerate(content):
                for y,yval in enumerate(content[x]):
                    if content[x][y] > 9 and [x,y] not in already_flashed:
                        flashed_at_all = True
                        already_flashed.append([x,y])
                        flashed_count += 1
                        content = flash(x,y,content)
                        break
                if flashed_at_all: break
        for x,xval in enumerate(content):
            for y,yval in enumerate(content[x]):
                if content[x][y] > 9:
                    content[x][y] = 0
    return generations


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(Fore.CYAN + Back.RED)
        print("Good job idiot, here is a medal: \U0001F3C5")
        raise(e)
