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
    map = []
    for i in content:
        map.append([j for j in i])
    answer = 0
    for x,xval in enumerate(map):
        for y,yval in enumerate(map[x]):
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
    #print(map2)
    #print(x,y)
    volume = 0
    #print(range(x,len(map)))
    #print(x,y,map[x][y],"new Found!")
    for x1 in range(x,len(map)):
        #print(x1,y,map[x1][y],"test x down")
        if map[x1][y] != "9" :
            if map2[x1][y] != "x":
                #print(x1,y,map[x1][y]," Found Point x down")
                known_low_points.append([x1,y])
                map2[x1][y] = "x"
                volume = volume+1+find_size(x1,y,map,map2)
        else:
            break
    for x1 in range(x,0,-1):
        #print(x1,y,map[x1][y],"test x up")
        if map[x1][y] != "9":
            if map2[x1][y] != "x":
                #print(x1,y,map[x1][y]," Found Point x up")
                known_low_points.append([x1,y])
                map2[x1][y] = "x"
                volume = volume+1+find_size(x1,y,map,map2)
        else:
            break
    for y1 in range(y,len(map[0])):
        #print(x,y1,map[x][y1],"test y right")
        if map[x][y1] != "9":
            if map2[x][y1] != "x":
                #print(x,y1,map[x][y1]," Found Point y right")
                known_low_points.append([x,y1])
                volume = volume+1
                map2[x][y1] = "x"
                volume= volume+find_size(x,y1,map,map2)
        else:
            break
    for y1 in range(y,-1,-1):
        #print(x,y1,map[x][y1],"test y left")
        if map[x][y1] != "9":
            if map2[x][y1] != "x":
                #print(x,y1,map[x][y1]," Found Point y left")
                known_low_points.append([x,y1])
                volume = volume+1
                map2[x][y1] = "x"
                volume= volume+find_size(x,y1,map,map2)
        else:
            break
        
    #print("Points in basin: "+str(volume+1))
    return volume

def part2(content):
    map = []
    basin_sizes = []
    for i in content:
        map.append([j for j in i])
    map2 = copy.deepcopy(map)
    answer = 0
    for x,xval in enumerate(map):
        for y,yval in enumerate(map[x]):
            if x==0 and y==0:
                neighbours = [map[x+1][y],map[x][y+1],map[x+1][y+1]]
                if all( int(record) > int(map[x][y]) for record in neighbours):
                    #print("Found Low Point",x,y,map[x][y])
                    basin_sizes.append(find_size(x,y,map,map2))
            elif x==len(map)-1 and y==len(map[0])-1:
                neighbours = [map[x-1][y],map[x][y-1],map[x-1][y-1]]
                if all( int(record) > int(map[x][y]) for record in neighbours):
                    #print("Found Low Point",x,y,map[x][y])
                    basin_sizes.append(find_size(x,y,map,map2))
            elif x==0 and y==len(map[0])-1:
                neighbours = [map[x+1][y],map[x][y-1],map[x+1][y-1]]
                if all( int(record) > int(map[x][y]) for record in neighbours):
                    #print("Found Low Point",x,y,map[x][y])
                    basin_sizes.append(find_size(x,y,map,map2))
            elif x==len(map)-1 and y==0:
                neighbours = [map[x-1][y],map[x][y+1],map[x-1][y+1]]
                if all( int(record) > int(map[x][y]) for record in neighbours):
                    #print("Found Low Point",x,y,map[x][y])
                    basin_sizes.append(find_size(x,y,map,map2))
            elif x==0:
                neighbours = [map[x][y-1],map[x][y+1],map[x+1][y-1],map[x+1][y],map[x+1][y+1]]
                if all( int(record) > int(map[x][y]) for record in neighbours):
                    #print("Found Low Point",x,y,map[x][y])
                    basin_sizes.append(find_size(x,y,map,map2))
            elif y==0:
                neighbours = [map[x-1][y],map[x-1][y+1],map[x][y+1],map[x+1][y],map[x+1][y+1]]
                if all( int(record) > int(map[x][y]) for record in neighbours):
                    #print("Found Low Point",x,y,map[x][y])
                    basin_sizes.append(find_size(x,y,map,map2))
            elif x==len(map)-1:
                #print("testing ",x,y,map[x][y])
                neighbours = [map[x][y-1],map[x][y+1],map[x-1][y-1],map[x-1][y],map[x-1][y+1]]
                if all( int(record) > int(map[x][y]) for record in neighbours):
                    #print("Found Low Point",x,y,map[x][y])
                    basin_sizes.append(find_size(x,y,map,map2))
            elif y==len(map[0])-1:
                neighbours = [map[x-1][y],map[x-1][y-1],map[x][y-1],map[x+1][y],map[x+1][y-1]]
                if all( int(record) > int(map[x][y]) for record in neighbours):
                    #print("Found Low Point",x,y,map[x][y])
                    basin_sizes.append(find_size(x,y,map,map2))
            else:
                neighbours = [map[x-1][y-1],map[x-1][y],map[x-1][y+1],map[x][y-1],map[x][y+1],map[x+1][y-1],map[x+1][y],map[x+1][y+1]]
                if all( int(record) > int(map[x][y]) for record in neighbours):
                    #print("Found Low Point",x,y,map[x][y])
                    basin_sizes.append(find_size(x,y,map,map2))
    #print(sorted(basin_sizes, reverse=True)[0]*sorted(basin_sizes, reverse=True)[1]*sorted(basin_sizes, reverse=True)[2])
    #print(sorted(basin_sizes, reverse=True))
    #print(map2[0])
    #print(map2[1])
    #print(map2[2])
    #print(map2[3])
    #print(map2[4])
    #print(len(map))
    #print(len(map[0]))
    return sorted(basin_sizes, reverse=True)[0]*sorted(basin_sizes, reverse=True)[1]*sorted(basin_sizes, reverse=True)[2]


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(Fore.CYAN + Back.RED)
        print("Good job idiot, here is a medal: \U0001F3C5")
        raise(e)
