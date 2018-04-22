# coding=u8
"""
选择排序的交换次数是N
"""

def selectSort(arr):
    len_ = len(arr)
    for i in range(len_):
        min_index = i
        for j in range(i+1,len_):  # 这个循环会找到值比第i个索引所代表值小的索引
            print(i,j)
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i] ,arr[min_index] = arr[min_index], arr[i]  # 互换两个索引位置
    return arr

print (selectSort([1,5,2,6,9,3]))