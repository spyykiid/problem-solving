from collections import Counter

def checkPerm(s1, s2):
  '''Using sort function O(n log n) complexity'''
  return sorted(s1) == sorted(s2)

def checkPerm2(s1, s2):
  '''Using Counter class from collections O(n)'''
  s1c = Counter(s1)
  s2c = Counter(s2)
  print(s1c, s2c)
  return s1c == s2c
  
def checkPerm3(s1, s2):
  '''Using Hashtable nothing but dict in py'''
  s1_ = {}
  for s in s1:
    s1_[s] = s1_.get(s, 0) + 1
  
  s2_ = {}
  for s in s2:
    s2_[s] = s2_.get(s, 0) + 1
  
  return s1 == s2


status = checkPerm('aaba', 'abaa')
status2 = checkPerm2('aaba', 'abaa')

status3 = checkPerm3('aaba', 'aaba')

print(status, status2, status3)

