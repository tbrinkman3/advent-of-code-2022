import os

from utils import *

def find_low(p1, p2):
  if(p1<p2):
    return 'p1'
  elif(p2<p1):
    return 'p2'
  else:
    return '*'

def find_high(p1,p2):
  if(p1>p2):
    return 'p1'
  elif(p2>p1):
    return 'p2'
  else:
    return '*'

def has_range_contained(p1,p2):
  low = find_low(p1[0],p2[0])
  high = find_high(p1[1],p2[1])

  return True if (low == high or (high=="*" or low == "*")) else False

def has_range_overlap(p1,p2):
  hasRangeContained = has_range_contained(p1,p2)

  if(not hasRangeContained):
    low = find_low(p1[0],p2[0])
    high = find_high(p1[1],p2[1])

    lowPairHighValue = p1[1] if low =='p1' else p2[1]
    highPairLowValue = p1[0] if high == 'p1' else p2[0]

    if(lowPairHighValue >= highPairLowValue):
      return True
    else:
      return False

  return True

def cleanup_pairings(input, compareFunc):
  count = 0
  for pair in input:
    pairs = pair.split(',')
    p1 = list(map(int, pairs[0].split('-')))
    p2 = list(map(int, pairs[1].split('-')))

    hasRangeOverlapOrContained = compareFunc(p1,p2)

    if(hasRangeOverlapOrContained):
      count+=1
  return count

def solve_part_1():
  with open('inputs/4') as f:
    input = data_to_array(f)
    return cleanup_pairings(input, has_range_contained)

def solve_part_2():
  with open('inputs/4') as f:
    input = data_to_array(f)
    return cleanup_pairings(input, has_range_overlap)

print('Part 1')
print(solve_part_1())
print('Part 2')
print(solve_part_2())

benchmark(solve_part_1, 100)
benchmark(solve_part_2, 100)
