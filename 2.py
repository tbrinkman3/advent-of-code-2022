import os

from utils import *

rounds = ["A Y", "B X", "C Z"]
#x -lose
#y - draw
#z - win
rps = [[3, 6, 0], [0, 3, 6], [6,0,3]]

foeMoves = ["A", "B", "C"]
youMoves = ["X", "Y", "Z"]

moveValues = [1,2,3]

roundScores = [0,3,6]


def play(foe, you):
  result = rps[foe][you]
  return result

def get_round_score(round):
  split = round.split()
  foe = foeMoves.index(split[0])
  you = youMoves.index(split[1])

  roundValue = play(foe,you)
  moveValue = moveValues[you]

  return roundValue + moveValue

def get_round_score_with_full_instruction(round):
  split = round.split()
  foe = foeMoves.index(split[0])
  neededOutcomeScore = roundScores[youMoves.index(split[1])]
  yourMoveScore = moveValues[rps[foe].index(neededOutcomeScore)]

  return neededOutcomeScore + yourMoveScore

def play_rounds(rounds):
  score = 0
  for round in rounds:
    score += get_round_score(round)

  print(score)

with open('2/input') as f:
  rounds = data_to_array(f)
  play_rounds(rounds)

