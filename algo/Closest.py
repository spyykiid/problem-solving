def findClosestElements(numDestinations, alllocations, numDeliveries):
  if len(alllocations) == 0 or numDeliveries == 0:
      return []
  
  alllocations.sort(key=lambda x: abs(x[0]-x[1]))
  k = numDeliveries
  while k < len(alllocations):
    a = alllocations[k-1]
    b = alllocations[k]
    
    if abs(a[0]-a[1]) == abs(b[0]-b[1]):
      k += 1
    else:
      break
    
  newLocations = alllocations[:k].sort()

  return newLocations[:numDeliveries]


numDestinations = 3
alllocations = [[1,-3], [1,2], [3,4]]
numDeliveries = 1

# numDestinations = 6 
# alllocations = [[3,6], [2,4], [5,3], [2,7], [1,8], [7,9]]
# numDeliveries = 3

findClosestElements(numDestinations, alllocations, numDeliveries)