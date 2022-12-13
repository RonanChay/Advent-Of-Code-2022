def hasOverlap(group):
    pairs = group.split(",")
    boundsP1 = pairs[0].split("-")
    boundsP2 = pairs[1].split("-")

    diff1 = int(boundsP2[1]) - int(boundsP1[0])
    diff2 = int(boundsP1[1]) - int(boundsP2[0])

    if diff1 < 0 or diff2 < 0:
        return False
    else:
        return True

def findTotalOverlaps():
    filename = "input.txt"
    filePtr = open(filename)

    totalOverlaps = 0
    for group in filePtr:
        if (hasOverlap(group)):
            totalOverlaps += 1
    
    print(totalOverlaps)

findTotalOverlaps()