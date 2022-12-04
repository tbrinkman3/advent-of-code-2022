def dataToArray(f):
  data = []
  for line in f:
    data.append(line.strip())
  return data