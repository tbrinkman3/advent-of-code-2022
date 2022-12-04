import os

from utils import *

def findLow(p1, p2):
  if(p1<p2):
    return 'p1'
  elif(p2<p1):
    return 'p2'
  else:
    return '*'

def findHigh(p1,p2):
  if(p1>p2):
    return 'p1'
  elif(p2>p1):
    return 'p2'
  else:
    return '*'

def has_range_contained(p1,p2):
  low = findLow(p1[0],p2[0])
  high = findHigh(p1[1],p2[1])

  return True if (low == high or (high=="*" or low == "*")) else False

def cleanup_pairings(input, compareFunc):
  count = 0
  for pair in input:
    pairs = pair.split(',')
    p1 = list(map(int, pairs[0].split('-')))
    p2 = list(map(int, pairs[1].split('-')))

    hasRangeOverlapOrContained = compareFunc(p1,p2)

    if(hasRangeOverlapOrContained):
      count+=1
  print(count)

def has_range_overlap(p1,p2):
  hasRangeContained = has_range_contained(p1,p2)

  if(not hasRangeContained):
    print(p1,p2)
    # get the low
    low = findLow(p1[0],p2[0])
    high = findHigh(p1[1],p2[1])

    lowPairHighValue = p1[1] if low =='p1' else p2[1]
    highPairLowValue = p1[0] if high == 'p1' else p2[0]

    if(lowPairHighValue >= highPairLowValue):
      return True
    else:
      return False

  return True

def solve():
  data = get_puzzle_input(4)
  input = data.split()
  #print(cleanup_pairings(input, has_range_contained))
  print(cleanup_pairings(input, has_range_overlap))

solve()
