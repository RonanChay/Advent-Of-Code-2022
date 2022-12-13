def isFullOverlap(group):
    pairs = group.split(",")
    boundsP1 = pairs[0].split("-")
    boundsP2 = pairs[1].split("-")

    LBdiff = (int(boundsP1[0]) - int(boundsP2[0]))
    UBdiff2 = (int(boundsP1[1]) - int(boundsP2[1]))
    sign = LBdiff * UBdiff2
    if sign <= 0:
        return True
    else:
        return False

def findTotalFullOverlaps():
    filename = "input.txt"
    filePtr = open(filename)

    totalFullOverlaps = 0
    for group in filePtr:
        if (isFullOverlap(group)):
            totalFullOverlaps += 1
    
    print(totalFullOverlaps)

findTotalFullOverlaps()