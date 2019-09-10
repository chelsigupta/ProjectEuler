import math
import string


file1 = open("p042_words.txt","r+")

myfile = file1.read()

myfile = myfile.split(",")

words = [x.strip('"') for x in myfile]


def is_triangle(num):

    d = math.sqrt(1+8*num)
    if d < 0:
        return True

    r1 = (-1+d)/2
    r2 = (-1-d)/2

    if r1>0 and math.floor(r1)==r1:
        return True

    if r2>0 and math.floor(r2)==r2:
        return True

    return False


def word_sum(s):

    sum = 0

    for i in range(0,len(s),1):
        t = string.uppercase.index(s[i]) + 1
        sum += t

    return sum


count = 0

for i in range(0,len(words),1):

    k = word_sum(words[i])

    if is_triangle(k):
        count += 1

print count