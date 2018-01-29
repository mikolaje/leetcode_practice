#coding:utf-8
def quicksort(array):
    if len(array)<2:
        return array
    else:
        midpivot = array[0]
        lte_midpivot = [i for i in array[1:] if i <= midpivot]
        print 'lte',lte_midpivot
        gt_midpivot = [i for i in array[1:] if i > midpivot]
        finallylist = quicksort(lte_midpivot)+ [midpivot] + quicksort(gt_midpivot)
        print 'final',finallylist
        return finallylist

print quicksort([4,3,2,1])