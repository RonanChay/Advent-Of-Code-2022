from part1 import searchItem
from part1 import sortItems

def findBadgeItem(rucksack1, rucksack2, rucksack3):
    sortItems(rucksack2)
    sortItems(rucksack3)

    for item in rucksack1:
        if (searchItem(item, rucksack2, 0, len(rucksack2) - 1)) and searchItem(item, rucksack3, 0, len(rucksack3) - 1):
            return item
    
    print("ERROR - No item found")
    print("rucksack1: ", rucksack1)
    print("rucksack2: ", rucksack2)
    print("rucksack3: ", rucksack3)
    return "-"

def findTotalPriority():
    filename = "input.txt"
    filePtr = open(filename)

    group = []
    totalPriority = 0
    for line in filePtr:
        group.append(list(line))
        if len(group) == 3:
            badgeItem = findBadgeItem(group[0], group[1], group[2])
            if badgeItem == badgeItem.capitalize():
                totalPriority += ord(badgeItem) - ord("A") + 27
            else:
                totalPriority += ord(badgeItem) - ord("a") + 1
            group = []

    print(totalPriority)

findTotalPriority()


