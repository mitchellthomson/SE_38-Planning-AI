import time

BoardSpot = {1 : "-",2 : "-",3 : "-",4 : "-",5 : "-",6 : "-",7 : "-",8 : "-",9 : "-",}
Player = 0
TurnCount = 0
startTime = time.time()
TurnTimes = []

def drawBoard(BoardSpot):
    boardDisplay = (f"|{BoardSpot[1]}||{BoardSpot[2]}||{BoardSpot[3]}|\n|{BoardSpot[4]}||{BoardSpot[5]}||{BoardSpot[6]}|\n|{BoardSpot[7]}||{BoardSpot[8]}||{BoardSpot[9]}|")
    print(boardDisplay)
    
def gameStart():
    drawBoard(BoardSpot)
    playerPiece = 'x'
    cpuTurn(playerPiece)
    

def checkWin():
    global Player
    print("\n")
    drawBoard(BoardSpot)
    #horizontal
    if((BoardSpot[1] == 'x' and BoardSpot[2] == 'x' and BoardSpot[3] == 'x') 
    or (BoardSpot[4] == 'x' and BoardSpot[5] == 'x' and BoardSpot[6] == 'x') 
    or (BoardSpot[7] == 'x' and BoardSpot[8] == 'x' and BoardSpot[9] == 'x')):
        endGame('x')
    elif((BoardSpot[1] == 'o' and BoardSpot[2] == 'o' and BoardSpot[3] == 'o') 
    or (BoardSpot[4] == 'o' and BoardSpot[5] == 'o' and BoardSpot[6] == 'o') 
    or (BoardSpot[7] == 'o' and BoardSpot[8] == 'o' and BoardSpot[9] == 'o')):
        endGame('o')
        
        #vertical
    elif((BoardSpot[1] == 'x' and BoardSpot[4] == 'x' and BoardSpot[7] == 'x') 
    or (BoardSpot[2] == 'x' and BoardSpot[5] == 'x' and BoardSpot[8] == 'x') 
    or (BoardSpot[3] == 'x' and BoardSpot[6] == 'x' and BoardSpot[9] == 'x')):
        endGame('x')
        
    elif((BoardSpot[1] == 'o' and BoardSpot[4] == 'o' and BoardSpot[7] == 'o') 
    or (BoardSpot[2] == 'o' and BoardSpot[5] == 'o' and BoardSpot[8] == 'o') 
    or (BoardSpot[3] == 'o' and BoardSpot[6] == 'o' and BoardSpot[9] == 'o')):
        endGame('o')
        
        #diagnol
    elif((BoardSpot[1] == 'x' and BoardSpot[5] == 'x' and BoardSpot[9] == 'x') 
    or (BoardSpot[3] == 'x' and BoardSpot[5] == 'x' and BoardSpot[7] == 'x')):
        endGame('x')
        
    elif((BoardSpot[1] == 'o' and BoardSpot[5] == 'o' and BoardSpot[9] == 'o') 
    or (BoardSpot[3] == 'o' and BoardSpot[5] == 'o' and BoardSpot[7] == 'o')):
        endGame('o')
    
    elif(TurnCount == 9):
        endGame("Tie")
    else:
        if(Player == 0):
            Player = 1
            playerPiece = 'o'
            cpuTurn(playerPiece)
        else:
            Player = 0
            playerPiece = 'x'
            cpuTurn(playerPiece)
        
def endGame(win):
    averageTime = 0
    print("Winner is ", win)
    endTime = time.time()
    totalTime = endTime - startTime
    i = 0
    while i <len(TurnTimes):
        averageTime+= TurnTimes[i]
        i+=1
    averageTime = averageTime/len(TurnTimes)
    print("Total game: ", totalTime)
    print("Average Turn = ",averageTime)
    
def cpuMakesMove(bestMove, playerPiece):
    global TurnCount
    BoardSpot[bestMove] = playerPiece
    TurnCount+=1
    checkWin()
    
def cpuTurn(playerPiece):
    turnTimeStart = time.time()
    bestScore = -8000
    bestMove = 0
    i = 1
    while(i<=len(BoardSpot)):
        if(BoardSpot[i] == "-"):
            BoardSpot[i] = playerPiece
            score = miniMax(BoardSpot,0,False, playerPiece)
            BoardSpot[i] = "-"
            
            if(score > bestScore):
                bestScore = score
                bestMove = i
            
        i+=1
    turnTime = time.time() - turnTimeStart
    print(turnTime)
    TurnTimes.append(turnTime)
    cpuMakesMove(bestMove,playerPiece)

def miniMax(BoardSpot, depth, isMaximizing, playerPiece):
    winCheck = cpuCheckWin()
    
    if(playerPiece == 'x'):
        opponentPiece = 'o'
        if(winCheck == 'x'):
            return 100
        elif(winCheck == 'o'):
            return -100
        elif(winCheck == 'tie'):
            return 0
        
    if(playerPiece == 'o'):
        opponentPiece = 'x'
        if(winCheck == 'x'):
            return -100
        elif(winCheck == 'o'):
            return 100
        elif(winCheck == 'tie'):
            return 0
        
    if(isMaximizing):
        bestScore = -1000
        
        i = 1
        while(i<=len(BoardSpot)):
            if(BoardSpot[i] == "-"):
                BoardSpot[i] = playerPiece
                score = miniMax(BoardSpot,depth+1,False,playerPiece)
                BoardSpot[i] = "-"
                
                if(score > bestScore):
                    bestScore = score
            i+=1
        return bestScore
    
    else:
        bestScore = 800
        i = 1
        while(i<=len(BoardSpot)):
            if(BoardSpot[i] == "-"):
                BoardSpot[i] = opponentPiece
                score = miniMax(BoardSpot,depth+1,True,playerPiece)
                BoardSpot[i] = "-"
                
                if(score < bestScore):
                    bestScore = score
            i+=1
        return bestScore
    
def cpuCheckWin():
    #horizontal
    if((BoardSpot[1] == 'x' and BoardSpot[2] == 'x' and BoardSpot[3] == 'x') 
    or (BoardSpot[4] == 'x' and BoardSpot[5] == 'x' and BoardSpot[6] == 'x') 
    or (BoardSpot[7] == 'x' and BoardSpot[8] == 'x' and BoardSpot[9] == 'x')):
        return('x')
    elif((BoardSpot[1] == 'o' and BoardSpot[2] == 'o' and BoardSpot[3] == 'o') 
    or (BoardSpot[4] == 'o' and BoardSpot[5] == 'o' and BoardSpot[6] == 'o') 
    or (BoardSpot[7] == 'o' and BoardSpot[8] == 'o' and BoardSpot[9] == 'o')):
        return('o')
        
        #vertical
    elif((BoardSpot[1] == 'x' and BoardSpot[4] == 'x' and BoardSpot[7] == 'x') 
    or (BoardSpot[2] == 'x' and BoardSpot[5] == 'x' and BoardSpot[8] == 'x') 
    or (BoardSpot[3] == 'x' and BoardSpot[6] == 'x' and BoardSpot[9] == 'x')):
        return('x')
        
    elif((BoardSpot[1] == 'o' and BoardSpot[4] == 'o' and BoardSpot[7] == 'o') 
    or (BoardSpot[2] == 'o' and BoardSpot[5] == 'o' and BoardSpot[8] == 'o') 
    or (BoardSpot[3] == 'o' and BoardSpot[6] == 'o' and BoardSpot[9] == 'o')):
        return('o')
        
        #diagnol
    elif((BoardSpot[1] == 'x' and BoardSpot[5] == 'x' and BoardSpot[9] == 'x') 
    or (BoardSpot[3] == 'x' and BoardSpot[5] == 'x' and BoardSpot[7] == 'x')):
        return('x')
        
    elif((BoardSpot[1] == 'o' and BoardSpot[5] == 'o' and BoardSpot[9] == 'o') 
    or (BoardSpot[3] == 'o' and BoardSpot[5] == 'o' and BoardSpot[7] == 'o')):
        return('o')
    
    if(BoardSpot[1] != '-' and BoardSpot[2] != '-'  and BoardSpot[3] != '-'
    and BoardSpot[4] != '-'  and BoardSpot[5] != '-'  and BoardSpot[6] != '-' 
    and BoardSpot[7] != '-'  and BoardSpot[8] != '-'  and BoardSpot[9]!= '-'):
        return('tie')

gameStart()