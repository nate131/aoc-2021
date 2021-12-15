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
        content = f.read().split("\n\n")
    
    print(Fore.GREEN)
    tprint('Aoc Day '+ os.path.basename(os.path.dirname(os.path.realpath(__file__))) + "\U0001F385")
    print(Fore.CYAN + Back.RESET)
    print(Fore.BLUE + tabulate.tabulate([["Part 1: ", ""],["Part 2: ", part2(content)]]))
    print (Style.RESET_ALL + '[Finished in {:.4f}ms]'.format(1000*(time.time() - startTime)),"\U0001F605")

def part1(content):
    points = content[0]
    folds = content[1]

    maxx = 0
    maxy = 0
    for line in points.split('\n'):
        point = line.split(",")
        if maxx < int(point[0]): maxx=int(point[0])
        if maxy < int(point[1]): maxy=int(point[1])
    y_list = []
    for y in range(maxy+1):
        x_list = []
        for x in range(maxx+1):
            x_list.append('.')
        y_list.append(x_list)

    for line in points.split('\n'):
        point = line.split(",")
        y_list[int(point[1])][int(point[0])] = '#'

    
    fold_list = []
    for folds in content[1].split('\n'):
        fold_list.append(folds.split(' ')[-1].split('='))
    
    for folds in fold_list:
        if folds[0] == 'y':
            top_half = y_list[:int(folds[1])]
            bottom_half = y_list[int(folds[1])+1:]
            bottom_half.reverse()
            
            new_board = []
            
            for y,yval in enumerate(top_half):
                new_x = []
                for x,xval in enumerate(top_half[y]):
                    if top_half[y][x] == '#' or bottom_half[y][x] == '#':
                        new_x.append('#')
                    else: 
                        new_x.append('.')
                new_board.append(new_x)
            y_list = new_board
            answer = 0
            for x in new_board:
                for y in x:
                    if y == '#': answer = answer + 1
            return answer
        if folds[0] == 'x':
            top_half = [x[:int(folds[1])] for x in y_list]
            bottom_half = [x[int(folds[1])+1:] for x in y_list]
            bottom_half = [x[::-1] for x in bottom_half]
            
            new_board = []
            
            for y,yval in enumerate(top_half):
                new_x = []
                for x,xval in enumerate(top_half[y]):
                    if top_half[y][x] == '#' or bottom_half[y][x] == '#':
                        new_x.append('#')
                    else: 
                        new_x.append('.')
                new_board.append(new_x)

            answer = 0
            for x in new_board:
                for y in x:
                    if y == '#': answer = answer + 1
            return answer

def part2(content):
    points = content[0]
    folds = content[1]

    maxx = 0
    maxy = 0
    for line in points.split('\n'):
        #print(line)
        point = line.split(",")
        #print(point)
        if maxx < int(point[0]): maxx=int(point[0])
        if maxy < int(point[1]): maxy=int(point[1])
    y_list = []
    for y in range(maxy+1):
        x_list = []
        for x in range(maxx+1):
            x_list.append('.')
        y_list.append(x_list)

    for line in points.split('\n'):
        point = line.split(",")
        y_list[int(point[1])][int(point[0])] = '#'

    
    fold_list = []
    for folds in content[1].split('\n'):
        #print(folds)
        fold_list.append(folds.split(' ')[-1].split('='))
    
    for folds in fold_list:
        if folds[0] == 'y':
            top_half = y_list[:int(folds[1])]
            bottom_half = y_list[int(folds[1])+1:]
            bottom_half.reverse()

            #print(maxx,maxy)
            #print("top ",len(top_half))
            #print("bottom ",len(bottom_half))            
            new_board = []
            
            for y,yval in enumerate(top_half):
                new_x = []
                for x,xval in enumerate(top_half[y]):
                    if top_half[y][x] == '#' or bottom_half[y][x] == '#':
                        new_x.append('#')
                    else: 
                        new_x.append('.')
                new_board.append(new_x)
            y_list = new_board
        if folds[0] == 'x':
            top_half = [x[:int(folds[1])] for x in y_list]
            bottom_half = [x[int(folds[1])+1:] for x in y_list]
            bottom_half = [x[::-1] for x in bottom_half]
            #print(maxx,maxy)
            #print("left ",len(top_half))
            #print("right ",len(bottom_half))
            new_board = []
            
            for y,yval in enumerate(top_half):
                new_x = []
                for x,xval in enumerate(top_half[y]):
                    if top_half[y][x] == '#' or bottom_half[y][x] == '#':
                        new_x.append('#')
                    else: 
                        new_x.append('.')
                new_board.append(new_x)
            y_list = new_board
    for x in y_list:
        print(x)
    return "Text Above"


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(Fore.CYAN + Back.RED)
        print("Good job idiot, here is a medal: \U0001F3C5")
        raise(e)
