import csv
import os
import time
from tqdm import tqdm
import tabulate
from art import tprint
from colorama import Fore, Style, Back
import copy
import re
import math

def main():
    startTime = time.time()
    with open(os.path.dirname(os.path.realpath(__file__))+'/input.txt', 'r') as f:
        content = f.read().split("\n")
    
    print(Fore.GREEN)
    tprint('Aoc Day '+ os.path.basename(os.path.dirname(os.path.realpath(__file__))) + "\U0001F385")
    print(Fore.CYAN + Back.RESET)
    print(Fore.BLUE + tabulate.tabulate([["Part 1: ", part1(content)],["Part 2: ", part2(content)]]))
    print (Style.RESET_ALL + '[Finished in {:.4f}ms]'.format(1000*(time.time() - startTime)),"("+format((round(time.time() - startTime,2)))+"s)","\U0001F605")

def add_fish(first,second):
    #print("add fish:",first," + ",second,"="+"["+first+","+second+"]")
    return "["+first+","+second+"]"
temp = ""
def reduce(number):
    global temp
    explode(number)
    while number != temp:
        number = temp
        explode(temp)
    split(number)
    if number != temp:
        number = temp
        reduce(temp)
    

def explode(number):
    global temp
    levels = 0
    for scan in range(len(number)):
        if number[scan] == "[":
            levels += 1
        elif number[scan] == "]":
            levels -= 1
        if levels == 5:
            #print("level 5 found on pos " + str(scan),number)
            pair = re.compile('\[(\d+),(\d+)\]') # find pair that is 4 levels deep
            reg_num = re.compile('(\d+)') # find pair that is 4 levels deep
            result = re.search(pair,number[scan:])
            left_num = result.group(1)
            right_num = result.group(2)
            #print(left_num,right_num)
            
            # search right
            #print("search starting right num in ",number[scan+result.span(2)[1]+1:])
            first_right = re.search(reg_num,number[scan+result.span(2)[1]+1:])
            #print("search start char",result.span(1),result.span(2))
            if first_right:
                #print("first right num is",first_right.group(1))
                #print(first_right.span(1))
                number = number[0:scan+result.span(2)[1]+first_right.span(1)[0]+1] + str(int(result.group(2))+ int(first_right.group(1))) + number[scan+result.span(2)[1]+first_right.span(1)[1]+1:]
                #print("changed first right",number)
            number = number[0:scan] + "0" + number[scan +result.span(2)[1]+1:]
            #print("replaced tuple with 0",number)
            # search left
            #print("search starting left num in ",number[:scan+result.span(1)[0]-1])
            all_left = re.finditer(reg_num,number[:scan+result.span(1)[0]-1])
            first_left = False
            for iteration in all_left:
                first_left = iteration
            if first_left:
                #print("first left num is",first_left.group(0))
                #print(first_left.span(1))
                number = number[0:first_left.start()] + str(int(result.group(1))+ int(first_left.groups()[-1])) + number[first_left.end():]
                #print("changed first left",number)
            #else: print("No left")
            temp = number
            return number
    temp = number
    return number

def split(number):
    global temp
    reg_num = re.compile('(\d\d+)') # find all digits
    doube_digit = re.search(reg_num,number)
    if doube_digit:
        #print(doube_digit.group(1))
        half_double = float(doube_digit.group(1))/2
        new_val = "["+str(math.floor(half_double)) + "," + str(math.ceil(half_double)) + "]"
        #print("replacement double:",doube_digit.group(1),"/2",half_double,new_val)
        number = number[0:doube_digit.span(1)[0]] + new_val + number[doube_digit.span(1)[1]:]
        #print("after split",number)
    temp = number
    return number

def magnitude(number):
    #print("start mag",number)
    pair = re.compile('\[(\d+),(\d+)\]') # find pair that is 4 levels deep
    result = True
    while re.search(pair,number):
        result = re.search(pair,number)
        number = number[0:result.span(1)[0]-1] + str((int(result.group(1)) * 3) + (int(result.group(2)) * 2)) + number[result.span(2)[1]+1:]
        #print("finish mag",number)
    return number


def part1(content):
    global temp
    start = content[0]
    #print(start)
    #print(content[1])
    for add_pair,pair_val in enumerate(tqdm(content,ncols=90,desc="Part 1 \U0001F914",unit_scale=True)):
        if add_pair == 0:
            continue
        next = add_fish(start,content[add_pair])
        next = reduce(next)
        start = temp
    return magnitude(start)

def part2(content):
    global temp
    mag_list = []
    for first_pair,f_val in enumerate(tqdm(content,ncols=90,desc="Part 2 \U0001F914",unit_scale=True)):
        for second_pair,s_val in enumerate(content):
            temp = ""
            if first_pair == second_pair: continue
            next = add_fish(f_val,s_val)
            next = reduce(next)
            mag_val = int(magnitude(temp))
            #print("fishnum ",first_pair,"(",f_val,")+ fishnum ",second_pair,"(",s_val,") mag is ",mag_val)
            mag_list.append(mag_val)
    #print(mag_list)
    #print()
    return max(mag_list)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(Fore.CYAN + Back.RED)
        print("Good job idiot, here is a medal: \U0001F3C5")
        raise(e)
