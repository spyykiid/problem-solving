def mono(nums):
  if len(nums) == 1:
    return True
  
  l = len(nums)

  prev = nums[0]
  i = 1
  while i < l and prev >= nums[i]:
    prev = nums[i]
    i += 1
  if i == l:
    return True

  print('decrease')
  prev = nums[0]
  i = 1
  while i < l and nums[i] <= prev :
    prev = nums[i]
    i += 1
  if i == l:
    return True

  return False
  
def mono_simple(A):
  inc = dec = True

  for i in range(len(A) - 1):
    if A[i] > A[i+1]:
      dec = False
    if A[i] < A[i+1]:
      inc = False

  return inc or dec

if __name__ == "__main__":
  print(mono([2,3,1,1]))