
def lis(nums):
  """ 
  """
  nums_len = len(nums)
  res = [1] * nums_len

  for i in range(1, nums_len):
    for j in range(i):
      if nums[j] <= nums[i] and res[j] + 1 > res[i]:
        res[i] = res[j] + 1

      print(i, j, res)

  return max(res)

nums = [10,9,2,5,3,7,101,18]
nums = [-1,3,4,5,2,2,2,2]
nums = [1,3,5,4,7]

print(lis(nums))

# Function to find length of longest increasing subsequence
def LIS(A, i, n, prev): 
    print('index i: ',i)
    # Base case: nothing is remaining
    if i == n:
        return 0

    # case 1: exclude the current element and process the
    # remaining elements
    
    excl = LIS(A, i + 1, n, prev)
    print(f'excl: {excl}')
    print(f'elem @ {i}: {A[i]}')
    # case 2: include the current element if it is greater
    # than previous element in LIS
    incl = 0
    if A[i] > prev:
        incl = 1 + LIS(A, i + 1, n, A[i])
        print(f'incl: {incl}')
    # return maximum of above two choices
    return max(incl, excl)


# Program for Longest Increasing Subsequence
if __name__ == '__main__':
    A = [0, 8, 4, 12, 22]
    A = [50, 3, 10, 7, 40, 80]
    # print("Length of LIS is", LIS(A, 0, len(A), float('-inf')))

