from random import randint
import numpy as np

def matrix():
    biglistnum  = int(input("length of bigger list? "))
    smallerlistnum = int(input("length of smaller list? "))
    numtoadd = int(input("value to be added to initial bigger list? "))
    biggerlist = []
    smallerlist = []
    while len(smallerlist) < smallerlistnum:
        randomnum = randint(0, 10)
        smallerlist.append(randomnum)
        biggerlist.append(smallerlist)
        

    while True:
        new = [k + numtoadd for k in biggerlist[-1]]
        for n,i in enumerate(new):
            if i>=10:
                new[n] = i-10
            else:
                new[n] = new[n]
        biggerlist.append(new )
        asw = np.array(biggerlist)
        print(asw)
        if len(biggerlist) == biglistnum:
            break

        
        
matrix()
