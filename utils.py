import requests
import os
import time
import logging

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

def benchmark(func, num, day):
  logging.basicConfig(filename=f'benchmarks/{day}', encoding='utf-8', level=logging.INFO, format='%(asctime)s -> %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
  totalTime = 0
  for i in range(num):
    totalTime += timeExecution(func)
  average = totalTime / num
  message = f"Average Execution Time of {average * 10**6} microseconds"
  logging.info(message)

def timeExecution(func):
  start = time.perf_counter()
  func()
  return time.perf_counter() - start
