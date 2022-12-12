def calculateRoundScore(opponent, player):
    '''
        1 - Rock
        2 - Paper
        3 - Scissors
    '''
    opponentMove = ord(opponent) - ord("A") + 1
    playerMove = ord(player) - ord("X") + 1
    roundScore = playerMove

    if opponentMove == playerMove:
        return (roundScore + 3)

    '''
        3 win possibilities:
        (player, opponent)
            (1, 3)        -> rock, scissors
            (2, 1)        -> paper, rock     (player - opponent = 1)
            (3, 2)        -> scissors, paper (player - opponent = 1)
    '''
    comparison = playerMove - opponentMove
    if (playerMove == 1 and opponentMove == 3) or (comparison == 1 and playerMove > opponentMove):
        roundScore += 6

    return roundScore

def findTotalScore():
    filename = "input.txt"
    inputPtr = open(filename)

    totalScore = 0
    for line in inputPtr:
        opponentMove = line[0]
        playerMove = line[2]
        totalScore += calculateRoundScore(opponentMove, playerMove)

    print(totalScore)

# ------------------------------------------------------------------------------------------------------------------
def main():
    findTotalScore()

main()