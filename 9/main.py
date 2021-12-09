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
    tprint('Aoc Day 9' + "\U0001F385")
    print(Fore.CYAN + Back.RESET)
    print(Fore.BLUE + tabulate.tabulate([["Part 1: ", part1(content)],["Part 2: ", part2(content)]]))
    print (Style.RESET_ALL + '[Finished in {:.4f}ms]'.format(1000*(time.time() - startTime)),"\U0001F605")

def part1(content):
    # parse content into list of lists
    map = []
    for i in content:
        map.append([j for j in i])
    answer = 0
    # enumerate over list of lists by element
    for x,xval in enumerate(map):
        for y,yval in enumerate(map[x]):
            # verify each permutation (corners/sides/middle) and verify if current pos is lowest of neighbours
            if x==0 and y==0:
                neighbours = [map[x+1][y],map[x][y+1],map[x+1][y+1]]
                if all(int(record) > int(map[x][y]) for record in neighbours):
                    answer = answer + int(map[x][y]) + 1
            elif x==len(map)-1 and y==len(map[0])-1:
                neighbours = [map[x-1][y],map[x][y-1],map[x-1][y-1]]
                if all(int(record) > int(map[x][y]) for record in neighbours):
                    answer = answer + int(map[x][y]) + 1
            elif x==0 and y==len(map[0])-1:
                neighbours = [map[x+1][y],map[x][y-1],map[x+1][y-1]]
                if all(int(record) > int(map[x][y]) for record in neighbours):
                    answer = answer + int(map[x][y]) + 1
            elif x==len(map)-1 and y==0:
                neighbours = [map[x-1][y],map[x][y+1],map[x-1][y+1]]
                if all(int(record) > int(map[x][y]) for record in neighbours):
                    answer = answer + int(map[x][y]) + 1
            elif x==0:
                neighbours = [map[x][y-1],map[x][y+1],map[x+1][y-1],map[x+1][y],map[x+1][y+1]]
                if all(int(record) > int(map[x][y]) for record in neighbours):
                    answer = answer + int(map[x][y]) + 1
            elif y==0:
                neighbours = [map[x-1][y],map[x-1][y+1],map[x][y+1],map[x+1][y],map[x+1][y+1]]
                if all(int(record) > int(map[x][y]) for record in neighbours):
                    answer = answer + int(map[x][y]) + 1
            elif x==len(map)-1:
                neighbours = [map[x][y-1],map[x][y+1],map[x-1][y-1],map[x-1][y],map[x-1][y+1]]
                if all(int(record) > int(map[x][y]) for record in neighbours):
                    answer = answer + int(map[x][y]) + 1
            elif y==len(map[0])-1:
                neighbours = [map[x-1][y],map[x-1][y-1],map[x][y-1],map[x+1][y],map[x+1][y-1]]
                if all(int(record) > int(map[x][y]) for record in neighbours):
                    answer = answer + int(map[x][y]) + 1
            else:
                neighbours = [map[x-1][y-1],map[x-1][y],map[x-1][y+1],map[x][y-1],map[x][y+1],map[x+1][y-1],map[x+1][y],map[x+1][y+1]]
                if all(int(record) > int(map[x][y]) for record in neighbours):
                    answer = answer + int(map[x][y]) + 1
    return answer

known_low_points = []

def find_size(x,y,map,map2):
    # find the total number of positions surrounding initial point bounded by 9s
    # from each point search up/down/left/right until a 9 is hit. each value found not a 9 recursively use the same function to go around corners
    volume = 0
    for x1 in range(x,len(map)):
        if map[x1][y] != "9" :
            if map2[x1][y] != "x":
                known_low_points.append([x1,y])
                map2[x1][y] = "x"
                volume = volume+1+find_size(x1,y,map,map2)
        else:
            break
    for x1 in range(x,0,-1):
        if map[x1][y] != "9":
            if map2[x1][y] != "x":
                known_low_points.append([x1,y])
                map2[x1][y] = "x"
                volume = volume+1+find_size(x1,y,map,map2)
        else:
            break
    for y1 in range(y,len(map[0])):
        if map[x][y1] != "9":
            if map2[x][y1] != "x":
                known_low_points.append([x,y1])
                volume = volume+1
                map2[x][y1] = "x"
                volume= volume+find_size(x,y1,map,map2)
        else:
            break
    for y1 in range(y,-1,-1):
        if map[x][y1] != "9":
            if map2[x][y1] != "x":
                known_low_points.append([x,y1])
                volume = volume+1
                map2[x][y1] = "x"
                volume= volume+find_size(x,y1,map,map2)
        else:
            break
        
    return volume

def part2(content):
    # parse content
    map = []
    basin_sizes = []
    for i in content:
        map.append([j for j in i])
    map2 = copy.deepcopy(map)
    answer = 0
    # enumerate over list of lists map
    for x,xval in enumerate(map):
        for y,yval in enumerate(map[x]):
            # for each value in list of lists map check if neighbours are all higher
            # test this by getting the neighbours per scenario (left, right, top, bottom side/wall or if its in the middle and all 8 surrounding points are indexes)
            if x==0 and y==0:
                neighbours = [map[x+1][y],map[x][y+1],map[x+1][y+1]]
                if all( int(record) > int(map[x][y]) for record in neighbours):
                    basin_sizes.append(find_size(x,y,map,map2))
            elif x==len(map)-1 and y==len(map[0])-1:
                neighbours = [map[x-1][y],map[x][y-1],map[x-1][y-1]]
                if all( int(record) > int(map[x][y]) for record in neighbours):
                    basin_sizes.append(find_size(x,y,map,map2))
            elif x==0 and y==len(map[0])-1:
                neighbours = [map[x+1][y],map[x][y-1],map[x+1][y-1]]
                if all( int(record) > int(map[x][y]) for record in neighbours):
                    basin_sizes.append(find_size(x,y,map,map2))
            elif x==len(map)-1 and y==0:
                neighbours = [map[x-1][y],map[x][y+1],map[x-1][y+1]]
                if all( int(record) > int(map[x][y]) for record in neighbours):
                    basin_sizes.append(find_size(x,y,map,map2))
            elif x==0:
                neighbours = [map[x][y-1],map[x][y+1],map[x+1][y-1],map[x+1][y],map[x+1][y+1]]
                if all( int(record) > int(map[x][y]) for record in neighbours):
                    basin_sizes.append(find_size(x,y,map,map2))
            elif y==0:
                neighbours = [map[x-1][y],map[x-1][y+1],map[x][y+1],map[x+1][y],map[x+1][y+1]]
                if all( int(record) > int(map[x][y]) for record in neighbours):
                    basin_sizes.append(find_size(x,y,map,map2))
            elif x==len(map)-1:
                neighbours = [map[x][y-1],map[x][y+1],map[x-1][y-1],map[x-1][y],map[x-1][y+1]]
                if all( int(record) > int(map[x][y]) for record in neighbours):
                    basin_sizes.append(find_size(x,y,map,map2))
            elif y==len(map[0])-1:
                neighbours = [map[x-1][y],map[x-1][y-1],map[x][y-1],map[x+1][y],map[x+1][y-1]]
                if all( int(record) > int(map[x][y]) for record in neighbours):
                    basin_sizes.append(find_size(x,y,map,map2))
            else:
                neighbours = [map[x-1][y-1],map[x-1][y],map[x-1][y+1],map[x][y-1],map[x][y+1],map[x+1][y-1],map[x+1][y],map[x+1][y+1]]
                if all( int(record) > int(map[x][y]) for record in neighbours):
                    basin_sizes.append(find_size(x,y,map,map2))
    # sort the list and return product of top 3 sizes
    return sorted(basin_sizes, reverse=True)[0]*sorted(basin_sizes, reverse=True)[1]*sorted(basin_sizes, reverse=True)[2]


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(Fore.CYAN + Back.RED)
        print("Good job idiot, here is a medal: \U0001F3C5")
        raise(e)
