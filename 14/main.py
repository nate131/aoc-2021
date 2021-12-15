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
    tprint('Aoc Day '+ os.path.basename(os.path.dirname(os.path.realpath(__file__))) + "\U0001F385")
    print(Fore.CYAN + Back.RESET)
    print(Fore.BLUE + tabulate.tabulate([["Part 1: ", part1(content)],["Part 2: ", part2(content)]]))
    print (Style.RESET_ALL + '[Finished in {:.4f}ms]'.format(1000*(time.time() - startTime)),"\U0001F605")

def part1(content):
    polymer = content[0]
    rule_list = content[2:]
    action_list = {}
    for i in tqdm(range(10),ncols=90,desc="Part 1 \U0001F914",unit_scale=True):
        for rule in rule_list:
            r = rule.split(' -> ')
            #polymer = polymer.replace(r[0],r[0][0]+r[1]+r[0][1])
            #print(polymer)
            res = [i for i in range(len(polymer)) if polymer.startswith(r[0], i)]
            #print(r[0],r[1],res)
            if len(res) > 0:
                for pos in res:
                    action_list[pos] = r[1]
        for k, v in sorted(action_list.items(),reverse=True): 
            polymer = polymer[:k+1]+v+polymer[k+1:]
        #print(polymer)
    most_common = collections.Counter(polymer).most_common()[0][1]
    least_common = collections.Counter(polymer).most_common()[-1][1]
    return (most_common-least_common)

def part2(content):
    polymer = content[0]
    rule_list = content[2:]
    poly_dict = {}
    for i in range(len(polymer)-1):
        if polymer[i:i+2] in poly_dict:
            poly_dict[polymer[i:i+2]] += 1
        else:
            poly_dict[polymer[i:i+2]] = 1
    for i in range(len(rule_list)):
        r = rule_list[i].split(' -> ')
        if r[0][0] + r[1] not in poly_dict:
            poly_dict[r[0][0] + r[1]] = 0
        if r[1] + r[0][1] not in poly_dict:
            poly_dict[r[1] + r[0][1]] = 0
    for i in range(40):
        actions = {}
        del_list = []
        for i in range(len(rule_list)):
            r = rule_list[i].split(' -> ')
            if r[0][0] + r[1] not in actions:
                actions[r[0][0] + r[1]] = 0
            if r[1] + r[0][1] not in actions:
                actions[r[1] + r[0][1]] = 0
        for rule in rule_list:
            r = rule.split(' -> ')
            if r[0] in poly_dict.keys():
                if poly_dict[r[0]] > 0:
                    del_list.append(r[0])
                    actions[r[0][0]+r[1]] += copy.copy(poly_dict[r[0]])
                    actions[r[1]+r[0][1]] += copy.copy(poly_dict[r[0]])
                    #print("remove: ",r[0]," add ",poly_dict[r[0]]," of ",r[0][0]+r[1]," and ",poly_dict[r[0]], " of ",r[1]+r[0][1])
        for key in del_list:
            poly_dict[key] = 0
        for key, value in actions.items():
            if value >0:
                poly_dict[key] += value
    letter_dict = {}
    for key,value in poly_dict.items():
        if key[0] not in letter_dict:
            letter_dict[key[0]] = 0
        if key[1] not in letter_dict:
            letter_dict[key[1]] = 0
        letter_dict[key[0]] = letter_dict[key[0]] + value
        letter_dict[key[1]] = letter_dict[key[1]] + value
    
    #print(letter_dict)
    most_common = letter_dict[max(letter_dict, key=letter_dict.get)]
    least_common = letter_dict[min(letter_dict, key=letter_dict.get)]
    #print(most_common, least_common)
    return ((most_common-least_common+1)//2)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(Fore.CYAN + Back.RED)
        print("Good job idiot, here is a medal: \U0001F3C5")
        raise(e)
