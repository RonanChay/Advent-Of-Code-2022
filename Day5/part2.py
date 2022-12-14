from part1 import parseMoveInput
from part1 import setupStacks

def moveCrates(stacks, amount, start, end):
    tempStack = []
    for i in range(amount):
        tempStack.append(stacks[start].pop())
    
    for i in range(amount):
        stacks[end].append(tempStack.pop())

def rearrangeCrates():
    filename = "input.txt"
    filePtr = open(filename)
    stacks = setupStacks(filePtr)
    
    for line in filePtr:
        inputs = parseMoveInput(line)
        moveCrates(stacks, inputs[0], inputs[1] - 1, inputs[2] - 1)
    
    top = ""
    for stack in stacks:
        top += stack.pop()
    
    print(top)

rearrangeCrates()