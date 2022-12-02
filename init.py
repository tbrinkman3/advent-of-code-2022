import os

cwd = os.getcwd() + "/"


for x in range(25):
  path = os.path.join(cwd, x.__str__())
  os.mkdir(path)
  print("Made directory", path)

pring("done")
