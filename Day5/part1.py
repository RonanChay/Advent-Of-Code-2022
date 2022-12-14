def parseMoveInput(line):
    arr = line.split(" ")
    amount = int(arr[1])
    start = int(arr[3])
    end = int(arr[5])

    inputs = [amount, start, end]
    return inputs

def moveCrates(stacks, amount, start, end):
    for i in range(amount):
        stacks[end].append(stacks[start].pop())

def rearrangeCrates():
    filename = "input.txt"
    filePtr = open(filename)

    numStacks = len(filePtr.readline()) // 4
    stacks = [[] for i in range(numStacks)]
    filePtr.seek(0)

    isSetupComplete = False
    for line in filePtr:
        if not isSetupComplete and len(line) > 1:
            for i in range(0, numStacks, 1):
                position = (i * 4) + 1
                if line[position] != " ":
                    stacks[i].append(line[position])

        if len(line) == 1:
            for i in range(numStacks):
                stacks[i].pop()
                stacks[i].reverse()
            isSetupComplete = True
            continue
        
        if isSetupComplete:
            inputs = parseMoveInput(line)
            moveCrates(stacks, inputs[0], inputs[1] - 1, inputs[2] - 1)
    
    top = ""
    for stack in stacks:
        top += stack.pop()
    
    print(top)
            
rearrangeCrates()