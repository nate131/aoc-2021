import csv
import os
import time
from tqdm import tqdm
import tabulate
from art import tprint
from colorama import Fore, Style, Back
import copy
import re
import collections

def main():
    startTime = time.time()
    with open(os.path.dirname(os.path.realpath(__file__))+'/input.txt', 'r') as f:
        content = f.read().split("\n")
    
    print(Fore.GREEN)
    tprint('Aoc Day 8' + "\U0001F385")
    print(Fore.CYAN + Back.RESET)
    print(Fore.BLUE + tabulate.tabulate([["Part 1: ", part1(content)],["Part 2: ", part2(content)]]))
    print (Style.RESET_ALL + '[Finished in {:.4f}ms]'.format(1000*(time.time() - startTime)),"\U0001F605")

def part1(content):
    answer = 0
    for i in content:
        splita = i.split("|")
        for j in splita[1].rstrip().split(" "):
            #print(len(i))
            if len(j) in [2,3,4,7]:
                answer = answer + 1
    return answer

def part2(content):
    codes = []
    for num,line in enumerate(content):
        test_nums = line.split("|")[0].rstrip().split(" ")
        c = []
        f = []
        # Determine numbers
        # test for num 1
        for digit in test_nums:
            if len(digit) == 2:
                c = [char for char in digit]
                f = [char for char in digit]
        for digit in test_nums:
            if len(digit) == 3:
                for letter in digit:
                    if letter not in c:
                        a = [letter]
        # test for num 4
        b = []
        d = []
        for digit in test_nums:
            if len(digit) == 4:
                for letter in digit:
                    if letter not in c:
                        b.append(letter)
                        d.append(letter)
        # test for num 8
        e = []
        g = []
        for digit in test_nums:
            if len(digit) == 7:
                for letter in digit:
                    if letter not in a+b+c+d+f:
                        e.append(letter)
                        g.append(letter)
        # test for num 0
        for digit in test_nums:
            letters = [char for char in digit]
            if len(digit) == 6 and b[0] in letters and b[1] not in letters:
                temp = b.copy()
                b = [temp[0]]
                d = [temp[1]]
                break
            elif len(digit) == 6 and b[1] in letters and b[0] not in letters:
                temp = b.copy()
                b = [temp[1]]
                d = [temp[0]]
                break
        # test for num 6
        for digit in test_nums:
            letters = [char for char in digit]
            if len(digit) == 6 and c[0] in letters and c[1] not in letters:
                temp = c.copy()
                f = [temp[0]]
                c = [temp[1]]
                break
            if len(digit) == 6 and c[1] in letters and c[0] not in letters:
                temp = c.copy()
                f = [temp[1]]
                c = [temp[0]]
                break
        # test for num 9
        for digit in test_nums:
            letters = [char for char in digit]
            if len(digit) == 6 and g[0] in letters and g[1] not in letters:
                temp = g.copy()
                g = [temp[0]]
                e = [temp[1]]
                break
            if len(digit) == 6 and g[1] in letters and g[0] not in letters:
                temp = g.copy()
                g = [temp[1]]
                e = [temp[0]]
                break

        # Test Numbers
        test_nums = line.split("|")[1].lstrip().split(" ")
        code = ""
        for digits in test_nums:
            letters = [char for char in digits]
            if set(letters) == set(a+b+c+e+f+g): number = '0'
            elif set(letters) == set(c+f): number = '1'
            elif set(letters) == set(a+c+d+e+g): number = '2'
            elif set(letters) == set(a+c+d+f+g): number = '3'
            elif set(letters) == set(b+c+d+f): number = '4'
            elif set(letters) == set(a+b+d+f+g): number = '5'
            elif set(letters) == set(a+b+d+e+f+g): number = '6'
            elif set(letters) == set(a+c+f): number = '7'
            elif set(letters) == set(a+b+c+d+e+f+g): number = '8'
            elif set(letters) == set(a+b+c+d+f+g): number = '9'
            code = code + number
        codes.append(code)
            

    return sum([int(i) for i in codes])


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(Fore.CYAN + Back.RED)
        print("Good job idiot, here is a medal: \U0001F3C5")
        raise(e)
