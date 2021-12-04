import csv
import os
import time
from tqdm import tqdm
import tabulate
from art import tprint
from colorama import Fore, Style, Back
import copy

def main():
    startTime = time.time()
    with open(os.path.dirname(os.path.realpath(__file__))+'/input.txt', 'r') as f:
        content = f.read().split("\n\n")
    content[0] = content[0].split(',')
    for i in range(1,len(content)):
        content[i] = content[i].split("\n")
        for j in range(len(content[i])):
            content[i][j] = content[i][j].strip(" ").replace("  ",",").replace(" ",",").split(",")
    
    print(Fore.GREEN)
    tprint('Aoc Day 4' + "\U0001F385")
    print(Fore.CYAN + Back.RESET)
    print(Fore.BLUE + tabulate.tabulate([["Part 1: ", part1(content)],["Part 2: ", part2(content)]]))
    print (Style.RESET_ALL + '[Finished in {:.4f}ms]'.format(1000*(time.time() - startTime)),"\U0001F605")

def part1(content):
    bingo=False
    bing_nums = content[0]
    cards = copy.deepcopy(content[1:])
    for bing_num in tqdm(bing_nums,ncols=90,desc="Part 1 \U0001F914",unit_scale=True):
        for c_index, card in enumerate(cards):
            for r_index, row in enumerate(card):
                if bing_num in row:
                    row_index = row.index(bing_num)
                    cards[c_index][r_index][row.index(bing_num)] = 'x'
                    # Horizontal Bingo
                    if cards[c_index][r_index].count('x') == len(cards[c_index][r_index]):
                        bingo=bing_num
                    # Vertical Bingo
                    if [row_s[row_index] for row_s in cards[c_index]].count("x") == len([row_s[row_index] for row_s in cards[c_index]]):
                        bingo=bing_num
                    if bingo:
                        counter = 0
                        for r_index, row in enumerate(card):
                            for num in row:
                                if num != "x":
                                    counter = counter + int(num)
                        return int(bing_num) * counter

def part2(content):
    bingo=False
    bing_nums = content[0]
    cards = copy.deepcopy(content[1:])
    win_history = []
    card_win_list = []
    
    for bing_num in tqdm(bing_nums,ncols=90,desc="Part 2 \U0001F914",unit_scale=True):
        for c_index, card in enumerate(cards):
            for r_index, row in enumerate(card):
                if bing_num in row:
                    row_index = row.index(bing_num)
                    cards[c_index][r_index][row.index(bing_num)] = 'x'
                    # Horizontal Bingo
                    if cards[c_index][r_index].count('x') == len(cards[c_index][r_index]) and c_index not in card_win_list:
                        bingo=bing_num
                        card_win_list.append(c_index)
                    # Vertical Bingo
                    if [row_s[row_index] for row_s in cards[c_index]].count("x") == len([row_s[row_index] for row_s in cards[c_index]]) and c_index not in card_win_list:
                        bingo=bing_num
                        card_win_list.append(c_index)
                    if bingo:
                        bingo = False
                        counter = 0
                        for r_index, row_win in enumerate(card):
                            for num in row_win:
                                if num != "x":
                                    counter = counter + int(num)
                        win_history.append([c_index, bing_num, int(bing_num) * counter])
    return win_history[-1][2]


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(Fore.CYAN + Back.RED)
        print("Good job idiot, here is a medal: \U0001F3C5")
        raise(e)
