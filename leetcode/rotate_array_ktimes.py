def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    ''' #1 brute force implementation O(n^2) '''
    # for _ in range(k):
    #     temp = nums[0]
    #     for i, n in enumerate(nums):
    #         i_nxt = (i + 1) % len(nums)
    #         temp_nxt = nums[i_nxt]
    #         nums[i_nxt] = temp
    #         temp = temp_nxt
    ''' #2 Pythonic way of things using array slicing '''
    # n = len(nums)
    # if (k + n) % n != 0:
    #     k = k % n
    #     nums[:] = nums[-k:] + nums[:-k]
    ''' #3 Using cyclic replacements '''
    # n = len(nums)
    # k = k % n
    # count = 0
    # start = 0
    #
    # if (k+n) % n != 0:
    #     while count < n:
    #         condition = True
    #         current = start
    #         prev = nums[start]
    #         while condition:
    #             next = (current + k) % n
    #             temp = nums[next]
    #             nums[next] = prev
    #             prev = temp
    #             current = next
    #             count += 1
    #             condition = (start != current)
    #         start += 1
    ''' #4 Using reverse '''
    n = len(nums)
    k %= n
    reverse(nums, 0, n-1)
    reverse(nums, 0, k-1)
    reverse(nums, k, n-1)

def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1




def main():
    rotate([1,2,3,4],3)


if __name__ == '__main__':
    main()