
def LinearSearch(list , target):
    for i in range (len(list)):
        if(list[i] == target):
            print(f"The number {target} found on index no {i}")
    return -1

list =[23,4,5,6,7,7,88]
target = 23
LinearSearch(list , target)





