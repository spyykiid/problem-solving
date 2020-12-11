
def canConstruct(ransomNote: str, magazine: str) -> bool:
  rc = {}
  for r in ransomNote:
    rc[r] = rc.get(r, 0) + 1
  
  mg = {}
  for m in magazine:
    mg[m] = mg.get(m, 0) + 1
  
  for k, v in rc.items():
    if v > mg.get(k, 0):
      return False
  
  return True
  print(mg, rc)

resp =canConstruct('aa', 'aab')
print(resp)