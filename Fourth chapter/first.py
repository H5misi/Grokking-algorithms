

import re
from time import sleep


print()









lis = [10, 1, 5, 7, 2, 6, 4, 9, 3, 8]

def quickSort(lis):
    if len(lis) < 2:
        return lis
    else:
        pivot = lis[0]
        less = [i for i in lis[1:] if i <= pivot]
        greater = [i for i in lis[1:] if i > pivot]
        print(pivot, less, greater)
        return quickSort(less) + [pivot] + quickSort(greater)
        

    

print(quickSort(lis))

