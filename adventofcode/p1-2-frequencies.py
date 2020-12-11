sum = 0
sumH = {0:True}

def readIO(filepath):
  global sum, sumH
  
  with open(filepath) as f:
    for freq in f:
      sum += int(freq)
      # print(sum)
      # print(sumH)
      if sumH.get(sum, False):
        return sum
      else:
        sumH[sum] = True
  return None


if __name__ == "__main__":
    result = None
    while not result:
      result = readIO('./data/p1-frequencies.txt') 
    print(result)