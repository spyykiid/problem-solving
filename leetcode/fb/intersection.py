def intersection(nums1, nums2):    
    list1 = sorted(nums1)
    list2 = sorted(nums2)
    l = 0
    r = 0 
    intersections = []
    

    while list1[l] and list2[r]:
        
        left = list1[l]
        right = list2[r]
        print(left, right)
        if left == right:
            intersections.append(right)
            while left == list1[r]: r+=1
            while right == list2[l]: l+=1
            continue
        
        if right > left:
            while left == list1[r]: 
                print(left, list1[r], r)
                r+=1
            
        else:
            while right == list2[l]: 
                print(right, l)
                l+=1
        print('end',l, r)
        
    # print(list1, list2)
    return intersections

if __name__ == "__main__":
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    intersection(nums1, nums2)
