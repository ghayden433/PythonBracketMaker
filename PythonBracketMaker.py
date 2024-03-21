""""
Author: Hayden Gillen

About: a march madness brakcet predictor based on seed records 1985-2023, does 1/4 of bracket at a time
       from https://www.ncaa.com/news/basketball-men/article/2024-03-07/records-every-seed-march-madness-1985-2023

Version 1
"""
import random

#win percentage by seed = index + 1, expressed as wins / total games
winLossPCT = [500 / 628,  #1 seed
              354 / 501,  #2
              281 / 429,  #3
              235 / 385,  #4
              176 / 328,  #5
              160 / 311,  #6
              136 / 287,  #7
              110 / 261,  #8
              93  / 245,  #9
              93  / 244,  #10
              98  / 250,  #11
              77  / 229,  #12
              38  / 190,  #13
              24  / 176,  #14
              16  / 168,  #15
              2   / 154,] #16

#function because these need to be used 4 times so we can call the function to start with the same numbers
def initRounds():
    #matchups in each round, next round is filled with 0 to prevent index out of range
    global round1
    global round2
    global round3
    global round4

    round1 = [[1, 16],
              [8, 9],
              [5, 12],
              [4, 13],
              [6, 11],
              [3, 14],
              [7, 10],
              [2, 15]]

    round2 = [[0, 0],
              [0, 0],
              [0, 0],
              [0, 0]]

    round3 = [[0, 0],
              [0, 0]]

    round4 = [[0, 0]]
 
    
#initialize the last couple of arrays, we only need to use them once
eliteEight = list()

finalFour = [[0, 0],
             [0, 0]]

champGame = [[0, 0]]




#function that takes 2 seeds and determines a winner based on the stats in winLossPCT returns winner seed number     
def gameWinner(seed1, seed2):  
    #determines the chance that seed 1 wins over seed 2 expressed as a decimal
    #expression is seed1 win% / (seed1 win% + seed2 win%) to express the chance of one team winning out of 100%
    #for ease of use with random() 
    seed1WinCance = winLossPCT[seed1 - 1] / (winLossPCT[seed1 - 1] + winLossPCT[seed2 - 1])
    
    #determine winner by choosing a random number and comparing it to chance of win
    if (random.random() < seed1WinCance):
        return seed1
    else:
        return seed2
    



def doRound(thisRound, nextRound):
    #every match in thisRound add winners to nextRound
    for i in range (len(thisRound)):
        #l and j are pointers to each spot in nextRound 
        l = i / 2
        j = i % 2       

        #add winner to the next round
        nextRound[int(l)][j] = gameWinner(thisRound[i][0], thisRound[i][1])
        
        #denotes winner in the round 
        if (thisRound[i][0] == nextRound[int(l)][j]):
            thisRound[i][0] = "(" + str(nextRound[int(l)][j]) + ")"
        else:
            thisRound[i][1] = "(" + str(nextRound[int(l)][j]) + ")"


#goes 4 times because 4 sections of bracket
for i in range(4):
    #initialize the seed arrays
    initRounds()
    #find winners
    doRound(round1, round2)
    doRound(round2, round3)
    doRound(round3, round4)
    #print one quarter
    print(round1)
    print(round2)
    print(round3)
    print(round4)
    print(" ")
    #set aside the two teams at the top of each division
    eliteEight.extend(round4)

#do the last couple of rounds
doRound(eliteEight, finalFour)
doRound(finalFour, champGame)
#print them
print(eliteEight)
print(finalFour)
print(champGame)
#print winner
print(gameWinner(champGame[0][0], champGame[0][1]))
    
    
    