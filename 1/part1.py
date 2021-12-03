import csv
import os
print(os.path.dirname(os.path.realpath(__file__)))
with open(os.path.dirname(os.path.realpath(__file__))+'/input.txt', 'r') as f:
    content = [int(line.rstrip()) for line in f]

counter = 0
for i in range(len(content)):
    if i==0:
        buffer = content[i]
        continue
    if content[i] > buffer:
        print(str(content[i]) + " > ")
        counter+=1
    else:
        print(str(content[i]))
    buffer = content[i]

print(str(counter))