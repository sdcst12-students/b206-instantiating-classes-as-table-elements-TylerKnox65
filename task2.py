#!python3

# Calculate the mean and standard deviation for each of the following datasets:

import random
set1 = [5, 13, 6, 14, 11, 11, 8, 6, 15, 10, 6, 16, 9, 11, 8, 5, 8, 11, 10, 9, 12, 10, 7, 7, 11, 10, 12, 10, 10, 6, 12, 13, 9, 13, 8, 17, 9, 12, 5, 13, 11, 15, 9, 8, 12, 15, 13, 5, 13, 14, 15, 10, 9, 12, 6, 12, 
14, 13, 11, 11, 11, 13, 17, 8, 11, 9, 15, 6, 5, 11, 7, 12, 6, 12, 13, 14, 11, 9, 16, 13, 18, 14, 9, 6, 8, 13, 11, 12, 17, 12, 11, 12, 18, 5, 11, 11, 14, 11, 10, 9]
set2 = [7, 12, 7, 7, 5, 11, 4, 12, 8, 5, 3, 8, 7, 7, 8, 5, 7, 8, 11, 6, 6, 9, 11, 5, 10, 8, 4, 5, 2, 6, 6, 9, 8, 7, 2, 9, 4, 12, 7, 8, 9, 4, 9, 7, 4, 8, 10, 3, 5, 8, 12, 8, 5, 6, 6, 4, 10, 3, 6, 4, 5, 11, 10, 4, 8, 8, 11, 5, 9, 7, 12, 4, 7, 6, 7, 9, 4, 12, 8, 7, 12, 9, 8, 12, 7, 5, 9, 8, 9, 4, 9, 5, 2, 8, 8, 9, 5, 8, 4, 4]
set3 =[13, 12, 7, 12, 12, 10, 11, 10, 11, 10, 13, 12, 5, 11, 9, 11, 11, 9, 12, 10, 7, 7, 10, 9, 12, 13, 7, 12, 9, 11, 9, 12, 12, 13, 11, 12, 8, 9, 16, 11, 9, 13, 11, 5, 12, 9, 14, 9, 10, 14, 10, 8, 10, 7, 7, 14, 8, 9, 5, 11, 12, 9, 12, 10, 11, 14, 12, 7, 15, 8, 8, 7, 11, 12, 14, 10, 9, 10, 13, 10, 11, 10, 11, 12, 10, 11, 9, 9, 11, 10, 13, 10, 9, 13, 8, 10, 7, 12, 9, 9]

def mean(data):
    temp = 0
    count = 0
    for i in data:
        temp += i
        count += 1
    return (temp/count)

def sd(data):
    deviation = []
    temp = 0
    meanVal = mean(data)
    for i in data:
        deviation.append((i-meanVal)**2)
    for i in deviation:
        temp += i
    temp = (temp / (len(deviation))) ** (1/2)
    

    return temp

assert round(mean(set1),2) == 10.77
assert round(sd(set1),2) == 3.19
assert round(mean(set2),2) == 7.16
assert round(sd(set2),2) == 2.60
assert round(mean(set3),2) == 10.34
assert round(sd(set3),2) == 2.20
