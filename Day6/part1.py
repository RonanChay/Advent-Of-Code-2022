def isStartMarker(marker):
    splitMarker = [marker[0], marker[1], marker[2], marker[3]]
    if len(set(splitMarker)) == 4:
        return True
    else:
        return False

def findLengthToMarker():
    filename = "input.txt"
    filePtr = open(filename)

    stream = filePtr.readline()

    pos = 0
    while not isStartMarker(stream[pos:(pos + 4)]):
        pos += 1
    
    length = pos + 4

    print(length)



findLengthToMarker()