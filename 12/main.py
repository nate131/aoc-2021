import csv
import os
import time
from typing import final
from tqdm import tqdm
import tabulate
from art import tprint
from colorama import Fore, Style, Back
import copy
import re
import itertools

total_hist=[]

def main():
    startTime = time.time()
    with open(os.path.dirname(os.path.realpath(__file__))+'/input.txt', 'r') as f:
        content = f.read().split("\n")
    
    print(Fore.GREEN)
    tprint('Aoc Day '+ os.path.basename(os.path.dirname(os.path.realpath(__file__))) + "\U0001F385")
    print(Fore.CYAN + Back.RESET)
    print(Fore.BLUE + tabulate.tabulate([
    ["Part 1: ", part1(content),'[Finished in {:.4f}ms]'.format(1000*(time.time() - startTime))],
    ["Part 2: ", part2(content),'[Finished in {:.4f}ms]'.format(1000*(time.time() - startTime))]
    ]))
    print (Style.RESET_ALL + '[Finished in {:.4f}ms]'.format(1000*(time.time() - startTime)),"\U0001F605")

paths = []

def map_ways(pathways,current,history,small_count):
    global paths
    history.append(current)
    for option in pathways[current]:
        if option == 'start':
            paths.append(history+['start']) 
            #print(history+['start'])
            continue
        if (option.isupper() or history.count(option) < small_count[option] ) and option not in  ['end','start']:
            map_ways(pathways,option,copy.copy(history),small_count)

def part1(content):
    global paths
    pathways = {}
    for path in content:
        conns = path.split('-')
        if conns[0] in pathways:
            pathways[conns[0]].append(conns[1])
        else:
            pathways[conns[0]]= [conns[1]]
        if conns[1] in pathways:
            pathways[conns[1]].append(conns[0])
        else:
            pathways[conns[1]]= [conns[0]]
    limits = {}
    for key in pathways.keys():
        limits[key] = 1
    map_ways(pathways,'end',[],limits)
    return len(paths)

def part2(content):
    global paths
    paths = []
    pathways = {}
    for path in content:
        conns = path.split('-')
        if conns[0] in pathways:
            pathways[conns[0]].append(conns[1])
        else:
            pathways[conns[0]]= [conns[1]]
        if conns[1] in pathways:
            pathways[conns[1]].append(conns[0])
        else:
            pathways[conns[1]]= [conns[0]]
    print("")
    limits = {}
    path_lims = []

    for key in pathways.keys():
        limits[key] = 1
    for i, (j,k) in enumerate(limits.items()):
        if j.islower() and j not in ['start','end']:
            limits[j] = 2
            map_ways(pathways,'end',[],limits)
            for path in paths:
                if path not in path_lims:
                    path_lims.append(copy.copy(path))
            paths = []
            limits[j] = 1
    #print(len(path_lims))
    return len(path_lims)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(Fore.CYAN + Back.RED)
        print("Good job idiot, here is a medal: \U0001F3C5")
        raise(e)
