#coding:utf-8
import time

def quicksort(array):
    if len(array)<2:
        return array
    else:
        midpivot = array[0]
        lte_midpivot = [i for i in array[1:] if i < midpivot]
        gt_midpivot = [i for i in array[1:] if i >= midpivot]
        final_list = quicksort(lte_midpivot) + [midpivot] + quicksort(gt_midpivot)
        return final_list

print(quicksort([3,1,2,1,4,6,5]))

"""
1.先从数列中取出一个数作为基准数。
2.分区过程，将比这个数大的数全放到它的右边，小于或等于它的数全放到它的左边。
3.再对左右区间重复第二步，直到各区间只有一个数。
"""