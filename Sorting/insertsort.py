# coding=u8
"""
插入排序适合数组中本来就很多是有顺序的

"""

def insertsort(array):
    _len = len(array)
    for i in range(1,_len):
        for j in range(i):
            print (i,j)
            if array[i] < array[j]:

                array[i],array[j]=array[j],array[i]
                array.insert(j, array[i]) # 首先碰到第一个比自己大的数字，赶紧刹车，停在那，所以选择insert
                array.pop(i+1) # 因为前面的insert操作，所以后面位数+1，这个位置的数已经insert到前面去了，所以pop弹出

    return array

def insertsort2(array):
    _len = len(array)
    for i in range(1, _len):
        for j in range(i):
            print (i, j)
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]  # 其实就是交换位置 可参考 https://www.youtube.com/watch?v=ROalU379l3U

    return array

print(insertsort([1,5,2,6,9,3]))