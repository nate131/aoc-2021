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
    tprint('Aoc Day 6' + "\U0001F385")
    print(Fore.CYAN + Back.RESET)
    print(Fore.BLUE + tabulate.tabulate([["Part 1: ", part1(content)],["Part 2: ", part2(content)]]))
    print (Style.RESET_ALL + '[Finished in {:.4f}ms]'.format(1000*(time.time() - startTime)),"\U0001F605")

def part1(content):
    bad_char = []
    for x,line in enumerate(content):
        #print(line)
        acceptable_chars = [x for x in '([{<']
        for y,char in enumerate(line):
            if char in acceptable_chars[:4] or char == acceptable_chars[-1]:
                if char == "(": acceptable_chars.append(")")
                if char == "[": acceptable_chars.append("]")
                if char == "{": acceptable_chars.append("}")
                if char == "<": acceptable_chars.append(">")
                if char == ")": acceptable_chars.pop()
                if char == "]": acceptable_chars.pop()
                if char == "}": acceptable_chars.pop()
                if char == ">": acceptable_chars.pop()
            else:
                bad_char.append([x,y,char])
                break
    answer = 0
    for x in bad_char:
        if x[2] == ")": answer += 3
        if x[2] == "]": answer += 57
        if x[2] == "}": answer += 1197
        if x[2] == ">": answer += 25137
    #print(bad_char)
    return answer

def part2(content):
    bad_lines = []
    autocom_scores = []
    for x,line in enumerate(content):
        #print(line)
        acceptable_chars = [x for x in '([{<']
        corrupt = False
        for y,char in enumerate(line):
            if char in acceptable_chars[:4] or char == acceptable_chars[-1]:
                if char == "(": acceptable_chars.append(")")
                if char == "[": acceptable_chars.append("]")
                if char == "{": acceptable_chars.append("}")
                if char == "<": acceptable_chars.append(">")
                if char == ")": acceptable_chars.pop()
                if char == "]": acceptable_chars.pop()
                if char == "}": acceptable_chars.pop()
                if char == ">": acceptable_chars.pop()
            else:
                bad_lines.append(x)
                corrupt = True
                break
        if not corrupt:
            answer = 0
            r_autocoms = acceptable_chars[4:]
            r_autocoms.reverse()
            for autocom in r_autocoms:
                answer = answer * 5
                if autocom == ")": answer += 1
                elif autocom == "]": answer += 2
                elif autocom == "}": answer += 3
                elif autocom == ">": answer += 4
            autocom_scores.append(answer)
    autocom_scores.sort()
    return autocom_scores[(len(autocom_scores) - 1)//2]


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(Fore.CYAN + Back.RED)
        print("Good job idiot, here is a medal: \U0001F3C5")
        raise(e)
