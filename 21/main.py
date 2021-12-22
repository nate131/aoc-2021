import csv
import os
import time
from tqdm import tqdm
import tabulate
from art import tprint
from colorama import Fore, Style, Back
import copy
import re
# import sys
# x=8000
# sys.setrecursionlimit(x)

def main():
    startTime = time.time()
    with open(os.path.dirname(os.path.realpath(__file__))+'/input.txt', 'r') as f:
        content = f.read().split("\n")
    
    print(Fore.GREEN)
    tprint('Aoc Day '+ os.path.basename(os.path.dirname(os.path.realpath(__file__))) + "\U0001F385")
    print(Fore.CYAN + Back.RESET)
    print(Fore.BLUE + tabulate.tabulate([["Part 1: ", part1(content)],["Part 2: ", part2(content)]]))
    print (Style.RESET_ALL + '[Finished in {:.4f}ms]'.format(1000*(time.time() - startTime)),"("+format((round(time.time() - startTime,2)))+"s)","\U0001F605")

def part1(content):
    player_data = {}
    board_segments = 10
    num_dice = 3
    print(board_segments)
    for line,data in enumerate(content):
        player_data[line] = {}
        player_data[line]['start'] = int(data.split(" ")[-1])
        player_data[line]['current'] = int(data.split(" ")[-1])
        player_data[line]['score'] = 0
        player_data[line]['wins'] = 0
    print(player_data)
    turns = 1
    while max([x['score'] for x in player_data.values()]) < 1000:
        player_offset = 0
        for player_number, player in enumerate(player_data.values()):
            #print("rolled", turns+player_offset,turns+1+player_offset,turns+2+player_offset,"=",turns+player_offset +turns+1+player_offset +turns+2+player_offset)
            player['current'] = int(repr(player['current'] + turns+player_offset +turns+1+player_offset +turns+2+player_offset)[-1])
            if player['current'] == 0: player['current'] = 10
            player['score'] += player['current']
            #print(player_number+1,player)
            if player['score'] >= 1000: return (turns+2+player_offset) * min([x['score'] for x in player_data.values()])
            player_offset += 3
        turns += player_offset
    return False

def part2(content):
    global winners
    global universes
    player_data = {}
    board_segments = 10
    print(board_segments)
    for line,data in enumerate(content):
        player_data[line] = {}
        player_data[line]['start'] = int(data.split(" ")[-1])
        player_data[line]['current'] = int(data.split(" ")[-1])
        player_data[line]['score'] = 0
        player_data[line]['identicality'] = 1
    roll_dice(player_data,0)
    print(winners)
    print(universes)

winners = [0,0]
universes = 0
def roll_dice(player_data,turn):
    global winners
    global universes
    universes += 27
    next_turn = 1 if turn==0 else 0
    # Roll 3, 1 occurance
    # - move to new position (could be n-1 mod 10 +1)
    player_data[turn]['current'] = int(repr(player_data[turn]['current'] + 3)[-1])
    if player_data[turn]['current'] == 0: player_data[turn]['current'] = 10
    # - increment score by current position
    player_data[turn]['score'] += player_data[turn]['current']
    # - if win, increment win count for player
    if player_data[turn]['score'] >= 21: 
        winners[turn] += player_data[turn]['identicality'] + 1
    # - multiply current identicality by number of occurances of this event and do the next players roll with current player data
    player_data[turn]['identicality'] = player_data[turn]['identicality'] * 1
    if player_data[turn]['score'] < 21: roll_dice(copy.deepcopy(player_data),next_turn)
    # - Rollback the identicality score and player score to calculate if rolled 1 higher
    player_data[turn]['identicality'] = player_data[turn]['identicality'] / 1
    player_data[turn]['score'] -= player_data[turn]['current']

    # Roll 4, 3 occurance
    player_data[turn]['current'] = int(repr(player_data[turn]['current'] + 1)[-1])
    if player_data[turn]['current'] == 0: player_data[turn]['current'] = 10
    player_data[turn]['score'] += player_data[turn]['current']
    if player_data[turn]['score'] >= 21: 
        winners[turn] += player_data[turn]['identicality'] + 3
    player_data[turn]['identicality'] = player_data[turn]['identicality'] * 3
    
    if player_data[turn]['score'] < 21: roll_dice(copy.deepcopy(player_data),next_turn)
    player_data[turn]['identicality'] = player_data[turn]['identicality'] / 3
    player_data[turn]['score'] -= player_data[turn]['current']

    # Roll 5, 6 occurance
    player_data[turn]['current'] = int(repr(player_data[turn]['current'] + 1)[-1])
    if player_data[turn]['current'] == 0: player_data[turn]['current'] = 10
    player_data[turn]['score'] += player_data[turn]['current']
    if player_data[turn]['score'] >= 21: 
        winners[turn] += player_data[turn]['identicality'] + 6
    player_data[turn]['identicality'] = player_data[turn]['identicality'] * 6
    
    if player_data[turn]['score'] < 21: roll_dice(copy.deepcopy(player_data),next_turn)
    player_data[turn]['identicality'] = player_data[turn]['identicality'] / 6
    player_data[turn]['score'] -= player_data[turn]['current']
    
    # Roll 6, 7 occurance
    player_data[turn]['current'] = int(repr(player_data[turn]['current'] + 1)[-1])
    if player_data[turn]['current'] == 0: player_data[turn]['current'] = 10
    player_data[turn]['score'] += player_data[turn]['current']
    if player_data[turn]['score'] >= 21: 
        winners[turn] += player_data[turn]['identicality'] + 7
    player_data[turn]['identicality'] = player_data[turn]['identicality'] * 7
    
    if player_data[turn]['score'] < 21: roll_dice(copy.deepcopy(player_data),next_turn)
    player_data[turn]['identicality'] = player_data[turn]['identicality'] / 7
    player_data[turn]['score'] -= player_data[turn]['current']
    
    # Roll 7, 6 occurance
    player_data[turn]['current'] = int(repr(player_data[turn]['current'] + 1)[-1])
    if player_data[turn]['current'] == 0: player_data[turn]['current'] = 10
    player_data[turn]['score'] += player_data[turn]['current']
    if player_data[turn]['score'] >= 21: 
        winners[turn] += player_data[turn]['identicality'] + 6
    player_data[turn]['identicality'] = player_data[turn]['identicality'] * 6
    
    if player_data[turn]['score'] < 21: roll_dice(copy.deepcopy(player_data),next_turn)
    player_data[turn]['identicality'] = player_data[turn]['identicality'] / 6
    player_data[turn]['score'] -= player_data[turn]['current']
   
    # Roll 8, 3 occurance
    player_data[turn]['current'] = int(repr(player_data[turn]['current'] + 1)[-1])
    if player_data[turn]['current'] == 0: player_data[turn]['current'] = 10
    player_data[turn]['score'] += player_data[turn]['current']
    if player_data[turn]['score'] >= 21: 
        winners[turn] += player_data[turn]['identicality'] + 3
    player_data[turn]['identicality'] = player_data[turn]['identicality'] * 3
    
    if player_data[turn]['score'] < 21: roll_dice(copy.deepcopy(player_data),next_turn)
    player_data[turn]['identicality'] = player_data[turn]['identicality'] / 3
    player_data[turn]['score'] -= player_data[turn]['current']
    
    # Roll 9, 1 occurance
    player_data[turn]['current'] = int(repr(player_data[turn]['current'] + 1)[-1])
    if player_data[turn]['current'] == 0: player_data[turn]['current'] = 10
    player_data[turn]['score'] += player_data[turn]['current']
    if player_data[turn]['score'] >= 21: 
        winners[turn] += player_data[turn]['identicality'] + 1
        #print(universes,player_data)
    if player_data[turn]['score'] < 21: roll_dice(copy.deepcopy(player_data),next_turn)
    



if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(Fore.CYAN + Back.RED)
        print("Good job idiot, here is a medal: \U0001F3C5")
        raise(e)
