import requests
import os

from dotenv import load_dotenv

load_dotenv()

def data_to_array(f):
  data = []
  for line in f:
    data.append(line.strip())
  return data

def get_puzzle_input(day):

  url=f"https://adventofcode.com/2022/day/{day}/input"

  headers = {
  'Cookie':f'session={os.getenv("AOC-SESSION")}'
  }

  response = requests.request("GET", url, headers=headers)

  return response.text


