#!/usr/local/bin/python3

def uniqueChar(charArray):
  charSet = set()
  for char in charArray:
    charSet.add(char)
  
  return len(charArray) == len(charSet)

def isUnique(str_):
  charSet = [False] * 128
  for s in str_:
    val = ord(s)
    if charSet[val]:
      return False
    charSet[val] = True 
  
  return True  

# Function testing
print(isUnique('ajbfj'))
print(uniqueChar('ab'))