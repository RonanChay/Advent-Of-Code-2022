def isStartMarker(marker):
    splitMarker = set()
    for i in range(14):
        splitMarker.add(marker[i])
    if len(set(splitMarker)) == 14:
        return True
    else:
        return False

def findLengthToMarker():
    filename = "input.txt"
    filePtr = open(filename)

    stream = filePtr.readline()

    pos = 0
    while not isStartMarker(stream[pos:(pos + 14)]):
        pos += 1
    
    length = pos + 14

    print(length)



findLengthToMarker()