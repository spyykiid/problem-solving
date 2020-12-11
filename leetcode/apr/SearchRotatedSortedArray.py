class Solution:
  def search(self, nums, target):
    pivot = self.findPivot(nums, 0, len(nums)-1)
    if pivot == -1:
      return self.binary_search(nums, 0, len(nums)-1, target)

    if nums[pivot] == target:
      return pivot
    
    if target >= nums[0]:
      return self.binary_search(nums, 0, pivot-1, target)
    return self.binary_search(nums, pivot+1, len(nums)-1, target)
  
  def binary_search(self, nums, low, high, target):
    if high < low:
      return -1

    mid = (low+high) // 2
    if target == nums[mid]:
      return mid
    if target > nums[mid]:
      return self.binary_search(nums, mid+1, high, target)
    if target < nums[mid]:
      return self.binary_search(nums, low, mid-1, target)

  def findPivot(self, nums, low, high):
    if high<low:
      return -1
    if high == low:
      return low
    
    mid = (low+high) // 2
    if mid < high and nums[mid] > nums[mid+1]:
      return mid
    if mid > low and nums[mid] < nums[mid-1]:
      return mid-1
    
    print(f'{nums}, {low}: {nums[low]}, {mid}:{nums[mid]}, {high}:{nums[high]}')
    if nums[low] >= nums[mid]:
      return self.findPivot(nums, low, mid-1)
    return self.findPivot(nums, mid+1, high)


def main():
  arr = [3, 4, 5, 6, 1, 2]
  s = Solution()
  # print(s.findPivot(arr,0, len(arr)-1))

  ordered_ = [1,2,3,4,5,6]
  # print(s.binary_search(ordered_, 0, 5))

  nums = [5, 6, 7, 8, 9, 10, 1, 2, 3] 
  print(s.search(nums, 1))

if __name__ == '__main__':
    main()