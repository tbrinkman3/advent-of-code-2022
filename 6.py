import os
from utils import *
import re

DAY = 6



def process_packet_v3(input, window_size):
  for i, _ in enumerate(input):
    if len(set(input[i - window_size : i])) == window_size:
      return i


def process_packet_v2(input, window_size):
  def create_dict(input):
    store = dict()
    for i in input:
      if i in store:
        store[i] += 1
      else:
        store[i] = 1
    return store

  def has_dupes(dict):
    for letter in dict:
      if dict[letter] > 1:
        return True
    return False

  def update_dict(dict,p1,p2):
    dict[p1] -= 1
    if dict[p1] == 0:
      del dict[p1]
    if p2 in dict:
      dict[p2] += 1
    else:
      dict[p2] = 1
    return dict

  p1 = 0
  p2 = window_size
  dict = create_dict(input[p1:p2])
  has_a_dupe = has_dupes(dict)
  while has_a_dupe:
    dict = update_dict(dict,input[p1],input[p2])
    has_a_dupe = has_dupes(dict)
    p1 += 1
    p2 += 1
    #has_a_dupe = False
  return p2

def process_packet(input, window_size):
  def has_repeat(input):
    return len(input) != len(''.join(sorted(set(input), key=input.index)))

  p1 = 0
  p2 = window_size
  found_start = False
  while(not found_start):
    window = input[p1:p2]
    if(has_repeat(window)):
      p1 += 1
      p2 += 1
    else:
      found_start = True

  return p2

def solve_part_1():
  with open('inputs/6') as f:
    input = f.read()
    return process_packet_v3(input, 4)

def solve_part_2():
  with open('inputs/6') as f:
    input = f.read()
    return process_packet_v3(input, 14)

print('Part 1 -> ', solve_part_1())
print('Part 2 -> ', solve_part_2())
benchmark(solve_part_1, 100, DAY)
benchmark(solve_part_2, 100, DAY)