import os
from utils import *
import re

def parse_input(input):
  content = input.readlines()

  split = content.index('\n')
  base = split -2
  base_size = int((len(content[base]) / 4))
  stacks = [[] for i in range(base_size)]
  while base > -1:
    i = 1
    for x in range(len(stacks)):
        if(len(content[base][i].strip()) > 0):
          stacks[x].append(content[base][i])
        i+=4
    base -= 1

  def scrub(i):
    return list(map(int,re.sub("\D+", ',', i.strip())[1:].split(',')))

  instr = list(map(scrub,content[split + 1:]))
  #add one to beginner to use indexes from input
  stacks.insert(0, [])
  return stacks, instr

def find_top_row(stacks):
  string = ''
  #remove filler list
  stacks.pop(0)
  for s in stacks:
    string += s.pop()

  return string

def move_boxes(input, crane):
  stacks, instr = parse_input(input)
  for i in instr:
    from_stack = stacks[i[1]]
    to_stack = stacks[i[2]]

    sub_stack = from_stack[len(from_stack) - i[0]:]
    rev_sub_stack = sub_stack[::-1]

    stacks[i[1]] = from_stack[:len(from_stack) - i[0]]
    if(crane == '9000'):
      stacks[i[2]] = to_stack + rev_sub_stack
    else:
      stacks[i[2]] = to_stack + sub_stack

  top_row = find_top_row(stacks)
  return top_row

def solve_part_1():
    with open('inputs/5') as f:
      move_boxes(f, '9000')

def solve_part_2():
    with open('inputs/5') as f:
      move_boxes(f, '9001')

print('Part 1')
print(solve_part_1())
print('Part 2')
print(solve_part_2())

benchmark(solve_part_1, 100)
benchmark(solve_part_2, 100)