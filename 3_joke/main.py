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
    tprint('Aoc Day 3' + "\U0001F385")
    print(Fore.CYAN + Back.RESET)
    print(Fore.BLUE + tabulate.tabulate([["Part 1: ", part1(content)],["Part 2: ", part2(content)]]))
    print (Style.RESET_ALL + '[Finished in {:.4f}ms]'.format(1000*(time.time() - startTime)),"\U0001F605")

def part1(content):
    x, y = "", ""
    length = len(content[0])
    transposed={}
    for i in tqdm(range(len(content)),ncols=90,desc="Part 1 \U0001F914",unit_scale=True):
        for num, bit in enumerate(content[i]):
            if num in transposed:
                transposed[num] = transposed[num]+bit
            else:
                transposed[num] = bit
    for val in transposed:
        if transposed[val].count('1') > len(transposed[val])/2:
            x = x+'1'
            y = y+'0'
        else:
            x = x+'0'
            y = y+'1'
    return str(int(x,2) * int(y,2))

def part2(content):
    oxygen = content.copy()
    carbon = content.copy()
    for i in tqdm(range(len(oxygen[0])),ncols=90,desc="Part 2a \U0001F914",unit_scale=True):
        slice = [oxygen[k][i] for k in range(len(oxygen))]
        if slice.count('1') >= len(oxygen)/2:
            remove_list = []
            for j in range(len(oxygen)):
                if oxygen[j][i] == '0':
                    remove_list.append(j)
            remove_list.reverse()
            for dele in remove_list:
                oxygen.pop(dele)
        else:
            remove_list = []
            for j in range(len(oxygen)):
                if oxygen[j][i] == '1':
                    remove_list.append(j)
            remove_list.reverse()
            for dele in remove_list:
                oxygen.pop(dele)

    for i in tqdm(range(len(carbon[0])),ncols=90,desc="Part 2b \U0001F914",unit_scale=True):
        if len(carbon) < 2:
            continue
        slice = [carbon[k][i] for k in range(len(carbon))]
        if slice.count('1') >= len(carbon)/2:
            remove_list = []
            for j in range(len(carbon)):
                if carbon[j][i] == '1':
                    remove_list.append(j)
            remove_list.reverse()
            for dele in remove_list:
                carbon.pop(dele)
        else:
            remove_list = []
            for j in range(len(carbon)):
                if carbon[j][i] == '0':
                    remove_list.append(j)
            remove_list.reverse()
            for dele in remove_list:
                carbon.pop(dele)
    return int(oxygen[0],2) * int(carbon[0],2)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(Fore.CYAN + Back.RED)
        print("Good job idiot, here is a medal: \U0001F3C5")
        raise(e)
