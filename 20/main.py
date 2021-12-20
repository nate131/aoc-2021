import csv
import os
import time
from tqdm import tqdm
import tabulate
from art import tprint
from colorama import Fore, Style, Back
import copy
import re
import numpy as np

def main():
    startTime = time.time()
    with open(os.path.dirname(os.path.realpath(__file__))+'/input.txt', 'r') as f:
        content = f.read().split("\n\n")
    
    print(Fore.GREEN)
    tprint('Aoc Day '+ os.path.basename(os.path.dirname(os.path.realpath(__file__))) + "\U0001F385")
    print(Fore.CYAN + Back.RESET)
    print(Fore.BLUE + tabulate.tabulate([["Part 1: ", part1(content)],["Part 2: ", part2(content)]]))
    print (Style.RESET_ALL + '[Finished in {:.4f}ms]'.format(1000*(time.time() - startTime)),"("+format((round(time.time() - startTime,2)))+"s)","\U0001F605")

def part1(content):
    lookup = ''.join(content[0].split("\n"))
    image_a = np.array([[val for val in x] for x in content[1].split("\n")])
    pad_ammount = 2
    img_arr = np.pad(image_a,pad_width=pad_ammount,mode='constant',constant_values='.')
    
    print(img_arr)
    for generation in range(2):
        final_img = copy.deepcopy(img_arr)
        for y in range(1,img_arr.shape[0]-1):
            for x in range(1,img_arr.shape[1]-1):
                #print(img_arr[y-1:y+2,x-1:x+2])
                strr = "".join("".join(i) for i in img_arr[y-1:y+2,x-1:x+2].astype(str))
                strr = strr.replace(".","0").replace("#","1")
                intt = int(strr,2)
                final_img[y][x] = lookup[intt]
                #print(strr,intt)
        print(final_img)
        img_arr = copy.deepcopy(final_img[1:final_img.shape[0]-1,1:final_img.shape[1]-1])
        pad_ammount = 2
        img_arr = np.pad(img_arr,pad_width=pad_ammount,mode='constant',constant_values='#')
    return np.count_nonzero(final_img[1:final_img.shape[0]-1,1:final_img.shape[1]-1] == '#')

def part2(content):
    lookup = ''.join(content[0].split("\n"))
    image_a = np.array([[val for val in x] for x in content[1].split("\n")])
    pad_ammount = 50
    img_arr = np.pad(image_a,pad_width=pad_ammount,mode='constant',constant_values='.')
    
    print(img_arr)
    for generation in range(50):
        final_img = copy.deepcopy(img_arr)
        for y in range(1,img_arr.shape[0]-1):
            for x in range(1,img_arr.shape[1]-1):
                #print(img_arr[y-1:y+2,x-1:x+2])
                strr = "".join("".join(i) for i in img_arr[y-1:y+2,x-1:x+2].astype(str))
                strr = strr.replace(".","0").replace("#","1")
                intt = int(strr,2)
                final_img[y][x] = lookup[intt]
                #print(strr,intt)
        print(final_img)
        img_arr = copy.deepcopy(final_img[1:final_img.shape[0]-1,1:final_img.shape[1]-1])
        pad_ammount = 2
        if (generation % 2) == 0:
            const_val = '#'
        else:
            const_val = '.'
        img_arr = np.pad(img_arr,pad_width=pad_ammount,mode='constant',constant_values=const_val)
    return np.count_nonzero(final_img[1:final_img.shape[0]-1,1:final_img.shape[1]-1] == '#')


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(Fore.CYAN + Back.RED)
        print("Good job idiot, here is a medal: \U0001F3C5")
        raise(e)
