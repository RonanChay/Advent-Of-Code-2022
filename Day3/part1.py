# bubble sort
def sortItems(compartment):
    for i in range(len(compartment)):
        for j in range(i, len(compartment), 1):
            if (ord(compartment[i]) > ord(compartment[j])):
                compartment[i], compartment[j] = compartment[j], compartment[i]

# binary search
def searchItem(item, compartment, left, right):
    if left > right:
        return False
    
    middle = (left + right) // 2

    if ord(item) > ord(compartment[middle]):
        return searchItem(item, compartment, middle + 1, right)
    elif ord(item) < ord(compartment[middle]):
        return searchItem(item, compartment, left, middle - 1)
    
    return True
    
def findSharedItem(rucksack):
    N = len(rucksack)
    leftCompartment = rucksack[0:N//2]
    rightCompartment = rucksack[N//2: N]
    sortItems(rightCompartment)

    for item in leftCompartment:
        index = searchItem(item, rightCompartment, 0, len(rightCompartment) - 1)
        if index:
            return item

    print("ERROR - No item found")
    print("rucksack: ", rucksack)
    print("left: ", leftCompartment)
    print("right: ", rightCompartment)
    return "-"

def calculatePriorityTotal():
    filename = "input.txt"
    filePtr = open(filename)

    priorityTotal = 0
    for rucksack in filePtr:
        duplicateItem = findSharedItem(list(rucksack[0:len(rucksack) - 1]))
        if duplicateItem == duplicateItem.capitalize():
            priorityTotal += ord(duplicateItem) - ord("A") + 27
        else:
            priorityTotal += ord(duplicateItem) - ord("a") + 1

    print(priorityTotal)

calculatePriorityTotal()