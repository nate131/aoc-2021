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

def display(start,x_range,y_range,history):
    #print(start,x_range,y_range,history)
    #print([start[0],x_range[0],x_range[1]]+[x[0] for x in history])
    size_x = [max([start[0],x_range[0],x_range[1]]+[x[0] for x in history]),min([start[0],x_range[0],x_range[1]]+[x[0] for x in history])]
    size_y = [max([start[1],y_range[0],y_range[1]]+[x[1] for x in history]),min([start[1],y_range[0],y_range[1]]+[x[1] for x in history])]
    #print(range(size_x[1],size_x[0]))
    #print(range(size_y[1],size_y[0]))
    for y in range(size_y[0],size_y[1]-1,-1):
        line_str = "" #"y: "+str(y)
        for x in range(size_x[1],size_x[0]+1,1):
            #print(x,y)
            if [x,y] == [0,0]:
                line_str += "S"
            elif [x,y] in history:
                line_str += "#"
            elif x_range[1] >= x >= x_range[0] and y_range[1] >= y >= y_range[0]:
                line_str += "T"
            else:
                line_str += "."
        print(line_str)

def part1(content):
    start = [0,0]
    history = [[0,0]]
    x_range = [int(x) for x in content[0].split(" ")[2][2:-1].split("..")]
    y_range = [int(x) for x in content[0].split(" ")[3][2:].split("..")]
    current = start
    winners = []
    angle_max = []
    for speed in range(184):
        for angle in range(1000):
            current_speed = speed
            current_angle = angle
            current_pos = [0,0]
            history = []
            for step in range(30000):
                current_pos = [current_pos[0]+current_speed,current_pos[1]+current_angle]
                history.append(current_pos)
                if current_speed != 0 and current_speed > 0:
                    current_speed -= 1
                elif current_speed != 0 and current_speed < 0:
                    current_speed += 1
                current_angle -= 1
                if current_pos[0] <= x_range[1] and current_pos[0] >= x_range[0] and current_pos[1] >= y_range[0] and current_pos[1] <= y_range[1]:
                    winners.append(history)
                    angle_max.append(angle)
                    #print(speed,angle)
                    #display(start,x_range,y_range,history)
                    break
                if current_pos[0] > x_range[1] or current_pos[1] < y_range[0]:
                    break
    max_y = 0
    for x in winners:
        y_vals = [z[1] for z in x]
        if max(y_vals) > max_y:
            max_y = max(y_vals)
    print(max_y)
    print(max(angle_max))
    return max_y

def part2(content):
    start = [0,0]
    history = [[0,0]]
    x_range = [int(x) for x in content[0].split(" ")[2][2:-1].split("..")]
    y_range = [int(x) for x in content[0].split(" ")[3][2:].split("..")]
    current = start
    winners = []
    angle_max = []
    for speed in range(200):
        velo_found = False
        for angle in range(200,-400,-1):
            current_speed = speed
            current_angle = angle
            current_pos = [0,0]
            history = []
            for step in range(200000):
                current_pos = [current_pos[0]+current_speed,current_pos[1]+current_angle]
                history.append(current_pos)
                if current_pos[0] <= x_range[1] and current_pos[0] >= x_range[0] and current_pos[1] >= y_range[0] and current_pos[1] <= y_range[1]:
                    winners.append(str(speed)+"xxx"+str(angle))
                    angle_max.append(angle)
                    #display(start,x_range,y_range,history)
                if current_pos[0] >= x_range[1] or current_pos[1] <= y_range[0]:
                    break
                if current_speed != 0 and current_speed > 0:
                    current_speed -= 1
                elif current_speed != 0 and current_speed < 0:
                    current_speed += 1
                current_angle -= 1
        #print(speed,angle,"rejected")
    print(max(angle_max))
    print(winners)
    print(len(winners))
    return len(list(set(winners)))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(Fore.CYAN + Back.RED)
        print("Good job idiot, here is a medal: \U0001F3C5")
        raise(e)
