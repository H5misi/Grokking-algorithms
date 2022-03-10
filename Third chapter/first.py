

import re
from time import sleep


print()


lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def binarySearch(lis, num, start, end):
   if start <= end:
    mid = (start + end) // 2
    if lis[mid] == item:
        return mid
    if lis[mid] < item:
        return binarySearch(lis, num, mid + 1, end)
    else:
        return binarySearch(lis, num, start, mid - 1)
    
    


item = 2
start = 0
end = len(lis)
print(binarySearch(lis, item, start, end))




