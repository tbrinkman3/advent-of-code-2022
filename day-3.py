import os

from utils import *


letterValues = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

arrInput = input.split()

print(len(arrInput))

def splitRucksack(rs):
  #odd number
  size = len(rs)
  half = size / 2
  comp1 = rs[slice(0,int(half))]
  comp2 = rs[slice(int(half), size)]
  return [comp1, comp2]

def findSharedItemType(splitRs):
  comp1 = splitRs[0]
  comp2 = splitRs[1]
  # assumes only 1
  return set(comp1).intersection(comp2).pop()

def getPriorityValueOfItemType(rs):
  splitRs = splitRucksack(rs)
  sharedItemType = findSharedItemType(splitRs)

  return letterValues.find(sharedItemType)

def sumPriorityByBadgeType(r1, r2, r3):
  badge = (set(r1).intersection(r2)).intersection(r3).pop()
  return letterValues.find(badge)

def sumPriorityOfItemTypesInRucksacks(rucksacks):
  sum = 0
  for rs in rucksacks:
    sum += getPriorityValueOfItemType(rs)
  return sum

def sumPriorityOfBadgeTypeInRucksacks(rucksacks):
  p = 0
  sum = 0

  while p < len(rucksacks):
    r1 = rucksacks[p]
    r2 = rucksacks[p+1]
    r3 = rucksacks[p+2]
    sum += sumPriorityByBadgeType(r1, r2, r3)
    p+=3
  return sum

with open('3/input') as f:
  arrInput = dataToArray(f)

  print(sumPriorityOfItemTypesInRucksacks(arrInput))
  print(sumPriorityOfBadgeTypeInRucksacks(arrInput))