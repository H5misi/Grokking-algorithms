
print()



# Binary search

lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

item = 8

def binarySearch(lis, item, firstIndex, lastIndex):
    
    while firstIndex <= lastIndex:
        mid = (firstIndex + lastIndex) // 2
        guess = lis[mid]
        if guess == item:
            return mid
        if guess < item:
            firstIndex = mid + 1
        if guess > item:
            lastIndex = mid - 1
    return None


firstIndex = 0
lastIndex = len(lis) - 1
print(binarySearch(lis, item, firstIndex, lastIndex))



