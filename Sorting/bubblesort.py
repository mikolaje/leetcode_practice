#coding=u8

def bubblesort(array):
    _len = len(array)

    for i in range(_len):
        for j in range(_len - i - 1):
            print(i,j)
            if array[j] > array[j+1]:
                array[j+1],array[j] = array[j],array[j+1]

    return array

print(bubblesort([4,1,2,3]))
