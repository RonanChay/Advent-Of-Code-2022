def calculateRoundScore(opponent, resultChar):
    '''
        1 - Rock
        2 - Paper
        3 - Scissors
    '''
    opponentMove = ord(opponent) - ord("A") + 1
    result = ord(resultChar) - ord("X") + 1

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