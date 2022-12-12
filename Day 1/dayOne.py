#!/usr/bin/env python

'''
print("\033[31m")
print("red message")
print("\033[0m")
print("default message")
'''

import sys


def heapify(heap, N, root):
    maximum = root
    left = 2 * root + 1
    right = 2 * root + 2

    if left < N and heap[left] > heap[maximum]:
        maximum = left
    
    if right < N and heap[right] > heap[maximum]:
        maximum = right

    if maximum != root:
        temp = heap[root]
        heap[root] = heap[maximum]
        heap[maximum] = temp

        heapify(heap, N, maximum)

def heapSort(heap):
    N = len(heap)
    for i in range((N // 2) - 1, -1, -1):
        heapify(heap, N, i)

    for i in range(N - 1, 0, -1):
        temp = heap[i]
        heap[i] = heap[0]
        heap[0] = temp

        heapify(heap, i, 0)

def maxCalorieCounter():
    filename = "input.txt"
    try:
        inputPtr = open(filename, encoding="utf-8-sig")
    except:
      print("Unable to open {}".format(filename))
      sys.exit()

    totalCalories = []
    calorieSum = 0
    for calorie in inputPtr:
        if (calorie != "\n"):
            calorieSum += int(calorie)
        else:
            totalCalories.append(calorieSum)
            calorieSum = 0

    heapSort(totalCalories)

    N = len(totalCalories)
    largestCalories = totalCalories[N - 1]
    largestCalories += totalCalories[N - 2]
    largestCalories += totalCalories[N - 3]

    print(largestCalories)

def main():
    maxCalorieCounter()

main()