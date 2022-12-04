import os

from utils import *


letterValues = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def split_rucksack(rs):
  #odd number
  size = len(rs)
  half = size / 2
  comp1 = rs[slice(0,int(half))]
  comp2 = rs[slice(int(half), size)]
  return [comp1, comp2]

def find_shared_item_type(splitRs):
  comp1 = splitRs[0]
  comp2 = splitRs[1]
  # assumes only 1
  return set(comp1).intersection(comp2).pop()

def get_priority_value_of_item_type(rs):
  splitRs = split_rucksack(rs)
  sharedItemType = find_shared_item_type(splitRs)

  return letterValues.find(sharedItemType)

def sum_priority_by_badge_type(r1, r2, r3):
  badge = (set(r1).intersection(r2)).intersection(r3).pop()
  return letterValues.find(badge)

def sum_priority_of_item_types_in_rucksacks(rucksacks):
  sum = 0
  for rs in rucksacks:
    sum += get_priority_value_of_item_type(rs)
  return sum

def sum_priority_of_badge_type_in_rucksacks(rucksacks):
  p = 0
  sum = 0

  while p < len(rucksacks):
    r1 = rucksacks[p]
    r2 = rucksacks[p+1]
    r3 = rucksacks[p+2]
    sum += sum_priority_by_badge_type(r1, r2, r3)
    p+=3
  return sum

# with open('3/input') as f:
#   arrInput = data_to_array(f)

#   print(sum_priority_of_badge_type_in_rucksacks(arrInput))
#   print(sum_priority_of_item_types_in_rucksacks(arrInput))

def solve():
  data = get_puzzle_input(3)
  arrInput = data.split()

  print(sum_priority_of_badge_type_in_rucksacks(arrInput))
  print(sum_priority_of_item_types_in_rucksacks(arrInput))




solve()
