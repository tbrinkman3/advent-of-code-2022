import os

from utils import *

def getHighestAmoutofCalories():

  with open('1/input') as f:

    elfsWithCalories = dataToArray(f)
    totalCaloriesByElf = []
    total = 0

    for item in elfsWithCalories:
      if(len(item.strip()) == 0):
        totalCaloriesByElf.append(total)
        total = 0
      else:
        total += int(item)

    sortedCalories = sorted(totalCaloriesByElf, reverse=True)
    #Part 1 solution
    #return sortedCalories[0]
    #Part 2 Solution
    return sum(sortedCalories[:3])

solution = getHighestAmoutofCalories()

print(solution)



