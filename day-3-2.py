import os

from utils import *

letterValues = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

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

def sumPriorityOfItemTypesInRucksacks(rucksacks):
  sum = 0
  for rs in rucksacks:
    sum += getPriorityValueOfItemType(rs)
  return sum

def sumPriorityByBadgeType(r1, r2, r3):


def sumPriorityOfBadgeType(rucksacks):
  pointer = 0



with open('3/input') as f:
  arrInput = dataToArray(f)

  sumPriorityOfItemTypesInRucksacks(arrInput)