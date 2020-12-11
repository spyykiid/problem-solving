def binary_search(nums, target):
  l = 0
  r = len(nums) -1
  
  while r >= l:
    m = l + (r-l) // 2
    val = nums[m]
    if target == val:
      return m
    
    if target > val:
      l = m + 1
    elif target < val:
      r = m - 1


def binary_search_recursive(nums, l, r, t):
  print(l, r)
  if r >= l: 
    m = l + (r-l) // 2
    val = nums[m]
    print(m, val, t)
    if val == t:
      return m
    
    if t < val:
      return binary_search_recursive(nums, l, m-1, t)
    if t > val:
      return binary_search_recursive(nums, m+1, r, t)
    
if __name__ == "__main__":
  # iterative func call
  print(binary_search([1,5,8,10, 12],1))
  
  # recursive func call
  # nums = [1,5,8,10,12]
  # print(binary_search_recursive(nums, 0, len(nums)-1,-2))