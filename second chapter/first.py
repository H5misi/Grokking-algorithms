

print()




# Selection sort
lis = [5, 6, 3, 10, 1, 9, 8, 7, 2, 4]

def selectionSort(lis):
    minIndex = 0
    for i in range(1, len(lis)):
        if lis[i] < lis[minIndex]:
            minIndex = i
    
    return minIndex

newLis = []
for i in range(len(lis)):
    min = selectionSort(lis)
    newLis.append(lis.pop(min))

print(newLis)




