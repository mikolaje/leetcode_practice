# coding=u8

def insertsort(array):
    _len = len(array)
    for i in range(1,_len):
        for j in range(i):
            if array[i] < array[j]:
                array.insert(j, array[i]) # 首先碰到第一个比自己大的数字，赶紧刹车，停在那，所以选择insert
                array.pop(i+1) # 因为前面的insert操作，所以后面位数+1，这个位置的数已经insert到前面去了，所以pop弹出

    return array


print(insertsort([1,5,2,6,9,3]))