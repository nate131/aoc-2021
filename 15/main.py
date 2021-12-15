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
    tprint('Aoc Day '+ os.path.basename(os.path.dirname(os.path.realpath(__file__))) + "\U0001F385")
    print(Fore.CYAN + Back.RESET)
    print(Fore.BLUE + tabulate.tabulate([["Part 1: ", part1(content)],["Part 2: ", part2(content)]]))
    print (Style.RESET_ALL + '[Finished in {:.4f}ms]'.format(1000*(time.time() - startTime)),"("+format((round(time.time() - startTime,2)))+"s)","\U0001F605")

def print_path(pathway):
    global prev
    found=True
    value = [len(pathway)-1,len(pathway[0])-1]
    final_path = []
    while found:
        if value == [0,0]:
            found=False
        else:
            #print(value)
            final_path.append([value[0],value[1]])
            value = prev[value[0]][value[1]]
    for x,xval in enumerate(pathway):
        strr = ""
        for y,yval in enumerate(pathway[x]):
            if [x,y] in final_path:
                strr += " x"+str(yval)
            else: strr += " "+str(yval)
        print(strr)

min_score = 470 # 470
last_printout = time.time()
prev = []
distance = []

def go(x,y,pathway):
    global distance
    distance = []
    for x,xval in enumerate(pathway):
        distance.append([1000000 for val in xval])
    global prev
    prev = []
    for x,xval in enumerate(pathway):
        prev.append([1000000 for val in xval])
    distance[0][0] = 0
    for test in range(7):
        for iter in range(len(pathway)+1):
            for x in range(iter):
                y=iter-1
                options = [[x+1,y],[x,y-1],[x,y+1],[x-1,y]]
                for option in options:
                    if 0 <= option[0] < len(pathway):
                        if 0 <= option[1] < len(pathway[0]):
                            if distance[option[0]][option[1]] > distance[x][y] + int(pathway[option[0]][option[1]]):
                                distance[option[0]][option[1]] = distance[x][y] + int(pathway[option[0]][option[1]])
                                prev[option[0]][option[1]] = [x,y]
            for y in range(iter):
                x=iter-1
                options = [[x+1,y],[x,y-1],[x,y+1],[x-1,y]]
                for option in options:
                    if 0 <= option[0] < len(pathway):
                        if 0 <= option[1] < len(pathway[0]):
                            if distance[option[0]][option[1]] > distance[x][y] + int(pathway[option[0]][option[1]]):
                                distance[option[0]][option[1]] = distance[x][y] + int(pathway[option[0]][option[1]])
                                prev[option[0]][option[1]] = [x,y]
    #print_path(distance)


def part1(content):
    pathway = []
    for x,xval in enumerate(content):
        pathway.append([int(val) for val in xval])
    go(0,0,pathway)
    return distance[len(pathway)-1][len(pathway[0])-1]

def part2(content):
    pathway = []
    for x,xval in enumerate(content):
        pathway.append([int(val) for val in xval]+[int(val)+1 for val in xval]+[int(val)+2 for val in xval]+[int(val)+3 for val in xval]+[int(val)+4 for val in xval])
    for x,xval in enumerate(content):
        pathway.append([int(val)+1 for val in xval]+[int(val)+2 for val in xval]+[int(val)+3 for val in xval]+[int(val)+4 for val in xval]+[int(val)+5 for val in xval])
    for x,xval in enumerate(content):
        pathway.append([int(val)+2 for val in xval]+[int(val)+3 for val in xval]+[int(val)+4 for val in xval]+[int(val)+5 for val in xval]+[int(val)+6 for val in xval])
    for x,xval in enumerate(content):
        pathway.append([int(val)+3 for val in xval]+[int(val)+4 for val in xval]+[int(val)+5 for val in xval]+[int(val)+6 for val in xval]+[int(val)+7 for val in xval])
    for x,xval in enumerate(content):
        pathway.append([int(val)+4 for val in xval]+[int(val)+5 for val in xval]+[int(val)+6 for val in xval]+[int(val)+7 for val in xval]+[int(val)+8 for val in xval])
    for x,xval in enumerate(pathway):
        for y,yval in enumerate(pathway[x]):
            if pathway[x][y] > 9:
                pathway[x][y] = pathway[x][y] - 9
    go(0,0,pathway)
    return distance[len(pathway)-1][len(pathway[0])-1]


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(Fore.CYAN + Back.RED)
        print("Good job idiot, here is a medal: \U0001F3C5")
        raise(e)
