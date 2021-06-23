#!/usr/bin/env python
# coding: utf-8

# In[1]:


def isEven(number):
    if(number%2 == 1):
        return 1;
    else:
        return -1;


# In[2]:


import math
def check(number,index, puzzle):
    y = math.floor(index/9)
    x = index%9
    for i in range(0,9):
        if(puzzle[i*9+x] == number and (i*9+x) != index):
            return False 
            
        if(puzzle[9*y+i] == number and (9*y+i) != index):
            return False
        
    x = math.floor(x/3)*3
    y = math.floor(y/3)*3
    for n in range(0,3):
        for m in range(0,3):
            if(puzzle[9*(y+m)+(x+n)] == number and (9*(y+m)+(x+n)) != index):
                return False
            
    return True


# In[3]:


exPuzzle = [8,7,0,6,0,0,0,4,5,
            0,5,0,3,0,7,0,0,0,
            3,0,9,1,0,0,7,2,0,
            1,0,0,5,0,0,0,7,9,
            0,0,0,0,0,3,1,0,2,
            7,6,0,0,2,0,5,0,0,
            0,8,0,0,0,0,2,0,4,
            9,0,5,2,3,0,0,8,7,
            4,2,7,0,5,0,0,1,0]
if(len(exPuzzle)!=81):
  print("Invalid Puzzle")
  


# In[4]:


def find(index,puzzle):
    checksum = 0
    correctNum = 0;
    for i in range(1,10):
        if(check(i,index,puzzle) == True):
            checksum += 1
            correctNum = i
    if(checksum == 1):
        return correctNum
    elif (checksum < 1):
        print("There is a mistake!")
        return -1
    else:
        return 0          


# In[5]:


def testPuzzle(puzzle):
    for x in range(9):
        for y in range(9):
            if(puzzle[x+9*y] == 0 or not check(puzzle[x+9*y],x+9*y,puzzle)):
                return False
    return True
                
                


# In[6]:


def printPuz(puzzle):
    for i in range(9):
        if(i%3 == 0 and i != 0):
            print("---------------------------------")
        print(str(puzzle[(i*9):(i*9+3)]) + " | " + str(puzzle[(i*9+3):(i*9+6)]) + " | " + str(puzzle[(i*9+6):(i*9+9)]))
        
def Solve(puzzle):
    while(not testPuzzle(puzzle)):
        for i in range(81):
            if(puzzle[i]==0):
                puzzle[i] = find(i,puzzle)
                #if(puzzle[i] != 0):
                    #print("found a " + str(puzzle[i]) + " at (" + str(i%9) + "," + str(math.floor(i/9)) + ")")     
    return puzzle              


# In[8]:


printPuz(Solve(exPuzzle))

