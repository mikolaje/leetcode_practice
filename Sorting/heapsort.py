# coding=u8
"""
http://bubkoo.com/2014/01/14/sort-algorithm/heap-sort/
堆有序，左儿子不一定要大于右儿子。但父节点肯定大于左右子节点。
"""


def heapsort(arr):
    def max_heapify(arr, index, heap_size):
        """
        # 最大堆调整（MAX‐HEAPIFY）的作用是保持最大堆的性质。 将堆的末端子节点作调整，使得子节点永远小于父节点
        # 意思就是要让index这元素去到它该去的位置
        《算法》P200
        由上至下的对有序化（下沉）
        如果我们把堆想象成一个严密的黑色会组织，每个子节点都表示一个下属（父节点则表示它的直接上级），name这些操作就可以得到很有趣的解释。
        max_hepify这个方法就相当于一个领导，如果占着老大的位置，但如果自己下属有比自己厉害的就要退位让贤。自己去到该去的层次

        注意的是：这方法是有惰性的。调用一次该方法仍然不行。如果该index的左右子树都小于自己的话，它就不会递归了。所以建立最大堆要从最后一个节点的父节点开始
        这个方法只是让index尽量下沉下去。如果是堆有序的话，那么执行该方法后index位置就是该位置最大的值
        """

        while True:
            imax = index
            ileft = 2 * index + 1
            iright = 2 * index + 2

            if ileft < heap_size and arr[index] < arr[ileft]:
                imax = ileft

            if iright < heap_size and arr[imax] < arr[iright]:
                imax = iright

            if imax != index:
                arr[imax], arr[index] = arr[index], arr[imax]
                index = imax
            else:
                break

    def build_maxheap(arr):
        """
        # 将堆所有数据重新排序，使其成为最大堆

        创建最大堆（Build-Max-Heap）的作用是将一个数组改造成一个最大堆，接受数组和堆大小两个参数，Build-Max-Heap 将自下而上的调用 Max-Heapify 来改造数组，建立最大堆。
        因为 Max-Heapify 能够保证下标 i 的结点之后结点都满足最大堆的性质，所以自下而上的调用 Max-Heapify 能够在改造过程中保持这一性质。
        如果最大堆的数量元素是 n，那么 Build-Max-Heap 从 Parent(n) 开始，往上依次调用 Max-Heapify。
        """

        iparent = len(arr) // 2 - 1   # 最后一个节点的父节点
        for i in range(iparent, -1, -1):
            max_heapify(arr, i, len(arr))

    def sort(arr):
        build_maxheap(arr)  # build后左子树 还是可能大于 右子树的.所以这并不是一个有序数组
        print(arr)
        for i in range(len(arr)-1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]

            max_heapify(arr, 0, i)  # 这里这个i 相当于比当前的length - 1；第i个元素为当前最大的元素，就被固定死了。不再访问它
        return arr

    return sort(arr)



if __name__ == '__main__':

    print(heapsort([5,4,7,3,8,2,11,15,17,16,13,10,9,12,1]))