import os

def bigSorting(unsorted):
    n = len(unsorted)
    if n == 1:
      return unsorted

    leftSort = bigSorting(unsorted[0:n//2])
    rightSort = bigSorting(unsorted[n//2:])
    print('lr',leftSort, rightSort)
    sortedList = mergingLists(leftSort, rightSort, n)
    print('sl',sortedList)
    return sortedList
  
def mergingLists(left, right, n):
    i = j = 0
    result = []
    for _ in range(0,n):
        if len(left[i]) < len(right[j]):
            result.append(left[i])
            i += 1
            if i == len(left):
                break
        elif len(left[i]) > len(right[j]):
            result.append(right[j])
            j += 1
            if j == len(right):
                break
        else:
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
                if i == len(left):
                    break
            elif left[i] > right[j]:
                result.append(right[j])
                j += 1
                if j == len(right):
                    break

    for x in range(i,len(left)):
      result.append(left[x])
    for y in range(j,len(right)):
      result.append(right[y])
    
    return result

if __name__ == '__main__':
    fptr = open('./big-o.txt', 'w')
    unsorted = []
    try:
      fin = open('./big.txt', 'r')
      for line in fin:
        unsorted_item = line.strip()
        unsorted.append(unsorted_item)
    
      blen = len(unsorted)
    finally:
      fin.close()
        

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()