

def show(list):
    for i in range(len(list)):
        print(list[i])


def BinarySearch(list, target):
    low = 0
    high = (len(list)-1)
    while (low <= high):
        mid = int((low + high)/2)
        if ((list[mid]) == target):
            return mid
        if ((list[mid]) < target):
            low = mid+1
        else:
            high = mid - 1

    return -1


list = [1, 8, 69, 96, 563, 67789]
target = 96
show(list)
searchIndex = BinarySearch(list, target)
print(f"The number {target} is found on index no {searchIndex}")
