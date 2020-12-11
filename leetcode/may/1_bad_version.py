def isBadVersion(x):
  return (x == 3)

def binary_search(nums):

  l = 1
  r = len(nums)
  
  while l < r:
    mid =  l + (r-l) // 2
    print(mid, nums[mid])

    if isBadVersion(mid):
      print(f'bad version, {mid} : {nums[mid]}')
      r = mid
    else:
      l = mid + 1
  
  return l




nums=[1,2,3,4,5,6]
resp = binary_search(nums)
print(resp)

