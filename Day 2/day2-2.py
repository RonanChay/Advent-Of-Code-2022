def calculateRoundScore(opponent, resultChar):
    '''
        0 - Rock        -1 - Lose
        1 - Paper        0 - Draw
        2 - Scissors     1 - Win
    '''
    opponentMove = ord(opponent) - ord("A")
    result = ord(resultChar) - ord("X") - 1

    playerMove = (opponentMove + result) % 3

    return (playerMove + 1) + (result + 1) * 3

def findTotalScore():
    filename = "input.txt"
    inputPtr = open(filename)

    totalScore = 0
    for line in inputPtr:
        opponentMove = line[0]
        resultChar = line[2]
        totalScore += calculateRoundScore(opponentMove, resultChar)

    print(totalScore)

# ------------------------------------------------------------------------------------------------------------------
def main():
    findTotalScore()

main()