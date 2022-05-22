# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 20:15:02 2020

@author: MVU
"""

import sys
import string
import random

def prefix_read(filename, k, out=dict()):
    fin = open(filename, encoding="UTF-8")
    is_header = 1
    last_prefix = tuple(' ' * k)
    for line in fin:
        if "*** END" in line:
            break
        if is_header == 0:
            last_prefix = process_line(last_prefix, line, out)        
        if "*** START" in line:
            is_header = 0
    return out

def process_line(last_prefix, line, D):

    specials = '’‘”“'
    punct = '"#$%&\'()*+-/<=>@[\\]^_`{|}~'
    numbers = "1234567890"

    line = line.replace('-', ' ')
    words = line.split()

    if words != []:
        for word in words:
            word = word.strip(string.whitespace + specials + punct + numbers)
            word = word.lower()
            d = dict()
            Suffix = D.get(last_prefix, d)   
            D[last_prefix] = Suffix
            Suffix[word] = Suffix.get(word,0) + 1
            last_prefix = last_prefix[1:] + (word,)

    return last_prefix

 
def random_suffix(prefix, D):
    S = D.get(prefix, 0)
    if S != 0:
        return random_word(S)
    else:
        return ''

def cumsum(t):
    s = t[:]
    sm = 0
    for i in range(len(t)):
        sm += t[i][0]
        s[i] = (sm, t[i][1])
    return s

def bisect_index(t, ran_nr):
    le = len(t)
    if le == 0:
        return 0
    elif (t[0][0] == ran_nr):
        return 0
    elif (t[-1][0] <= ran_nr):
        return le-1 
    elif (t[(le // 2)][0] > ran_nr):
        return bisect_index(t[:(le // 2)], ran_nr)
    else:
        return bisect_index(t[(le // 2):], ran_nr) + (le // 2)

def random_word(D):
    t = []
    for key, freq in D.items():
        t.append((freq,key))
    Cs = cumsum(t)
    max_ind = Cs[-1][0]
    ind = bisect_index(Cs, random.randint(0,max_ind))
    return Cs[ind][1]



def random_story(D, k, preflen):

    out = []
    t = list(D.items())

    for i in range(k):

        i = random.randint(0,len(t)-1)
        prefix = t[i][0]
        cprefix = (prefix[0].capitalize(),) + prefix[1:]
        out.extend(cprefix)
        try:
            lastchar = prefix[-1][-1]
        except:
            print(lastchar)

        while lastchar != '.' and lastchar != '!' and lastchar != '?':
            suffix = random_suffix(prefix, D)
            out.append(suffix)
            prefix = prefix[1:] + (suffix,)
            try:
                lastchar = prefix[-1][-1]
            except:
                print(lastchar)
        
    return ' '.join(out)

if len(sys.argv) >= 3:
    arg1 = int(sys.argv[1])
    arg2 = int(sys.argv[2])
elif len(sys.argv) == 2:
    arg1 = int(sys.argv[1])    
    arg2 = 2
else:
    print("\n"
          "*******************************************\n"
          " Markov model generating classic literature\n"
          "*******************************************\n"
          "\n"
          " Shell command syntax:\n"
          "\n"
          " > python markov.py [number of sentences] [markov prefix length]\n"
          "\n"
          " Recommended test parameter values:\n"
          "\n"
          " > python markov.py 5 5\n"
          "\n"
          " Full description of function available in README.md"
          "\n")
    exit(0)


D = prefix_read('Dickens.txt', arg2)
D = prefix_read('Shakespeare.txt', arg2, D)
D = prefix_read('Hemingway.txt', arg2, D)
print("\n{}: {} unique prefixes in Markov library.\n".format("Dickens, Hemingway, and Shakespeare", len(D)))

print(random_story(D,arg1,arg2))
print("\n")



