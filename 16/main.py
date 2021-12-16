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

version_list = []

def decode_packet(packet,offset):
    version = int(packet[offset:3+offset],2)
    global version_list
    version_list.append(version)
    #print("version",version)
    type = int(packet[3+offset:6+offset],2)
    #print("type",type)
    payload = {}
    payload["version"] = version
    payload["type"] = type
    #print(packet[offset:])
    if type == 4:
        payload["value"] = ""
        #print(packet[6+offset])
        if int(packet[6+offset]) == 1:
            while int(packet[6+offset]) == 1:
                payload["value"]  += packet[7+offset:11+offset]
                offset += 5
        payload["value"]  += packet[7+offset:11+offset]
        payload["value"] = int(payload["value"],2)
        #print(((11+offset) % 4))
        #print((11+offset) + (4 - (11+offset) % 4))
        #while ((11+offset) % 4) != 0:
        #    offset += 1
        final_pos = (11+offset)
        payload["endpos"] = final_pos
        return payload
    else:
        payload["length_ty"] = packet[6+offset]
        if payload["length_ty"] == '1':
            payload["packet_length"] = int(packet[7+offset:7+11+offset],2)
            payload["packet"] = []
            offset = 7+11+offset
            offset_new = offset
            #print("packet_length packs",payload["packet_length"])
            for i in range(payload["packet_length"]):
                #print("offset",offset_new)
                temp = decode_packet(packet,offset_new)
                print(temp)
                offset_new = temp["endpos"]
                payload["packet"].append(temp)
            if payload["type"] == 0:
                payload["value"] = sum([x["value"] for x in payload["packet"]])
            if payload["type"] == 1:
                payload["value"] = math.prod([x["value"] for x in payload["packet"]])
            if payload["type"] == 2:
                payload["value"] = min([x["value"] for x in payload["packet"]])
            if payload["type"] == 3:
                payload["value"] = max([x["value"] for x in payload["packet"]])
            if payload["type"] == 5:
                if payload["packet"][0]["value"] > payload["packet"][1]["value"]:
                    payload["value"] = 1
                else:
                    payload["value"] = 0
            if payload["type"] == 6:
                if payload["packet"][0]["value"] < payload["packet"][1]["value"]:
                    payload["value"] = 1
                else:
                    payload["value"] = 0
            if payload["type"] == 7:
                if payload["packet"][0]["value"] == payload["packet"][1]["value"]:
                    payload["value"] = 1
                else:
                    payload["value"] = 0
            payload["endpos"] = offset_new
            return payload
        if payload["length_ty"] == '0':
            payload["packet_length"] = int(packet[7+offset:7+15+offset],2)
            offset = 7+15+offset
            offset_new = offset
            payload["packet"] = []
            #print("packet_length size",payload["packet_length"])
            while offset_new < offset+payload["packet_length"]-1:
                #print(offset_new,offset+payload["packet_length"])
                temp = decode_packet(packet,offset_new)
                #print(temp)
                offset_new = temp["endpos"]
                print(temp)
                payload["packet"].append(temp)
            if payload["type"] == 0:
                payload["value"] = sum([x["value"] for x in payload["packet"]])
            if payload["type"] == 1:
                payload["value"] = math.prod([x["value"] for x in payload["packet"]])
            if payload["type"] == 2:
                payload["value"] = min([x["value"] for x in payload["packet"]])
            if payload["type"] == 3:
                payload["value"] = max([x["value"] for x in payload["packet"]])
            if payload["type"] == 5:
                if payload["packet"][0]["value"] > payload["packet"][1]["value"]:
                    payload["value"] = 1
                else:
                    payload["value"] = 0
            if payload["type"] == 6:
                if payload["packet"][0]["value"] < payload["packet"][1]["value"]:
                    payload["value"] = 1
                else:
                    payload["value"] = 0
            if payload["type"] == 7:
                if payload["packet"][0]["value"] == payload["packet"][1]["value"]:
                    payload["value"] = 1
                else:
                    payload["value"] = 0
            payload["endpos"] = offset_new
            return payload


def part1(content):
    decode = {'0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }
    packet = ''.join([decode[x] for x in content[0]])
    #print(packet)
    decoded = decode_packet(packet,0)
    #print(version_list)
    return sum(version_list)

def part2(content):
    decode = {'0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }
    packet = ''.join([decode[x] for x in content[0]])
    #print(packet)
    decoded = decode_packet(packet,0)
    
    return decoded["value"]


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(Fore.CYAN + Back.RED)
        print("Good job idiot, here is a medal: \U0001F3C5")
        raise(e)
