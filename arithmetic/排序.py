# 冒泡
def bubble_sort(array):
    for i in range(1, len(array)):
        for j in range(0, len(array) - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


# 插入排序
def insertion_sort(array):
    for i in range(len(array)):
        tmp = array[i]
        pre = i - 1
        while pre >= 0 and tmp < array[pre]:
            array[pre + 1] = array[pre]
            pre -= 1
        array[pre + 1] = tmp
    return array


# 归并排序
def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    return merge(merge_sort(array[:mid]), merge_sort(array[mid:]))


def merge(l1, l2):
    r = []
    while l1 and l2:
        if l1[0] < l2[0]:
            r.append(l1.pop(0))
        else:
            r.append(l2.pop(0))
    r += l1 + l2
    return r


# 快速排序
def quick_sort1(array, i, j):
    if i >= j:
        return
    start = i
    end = j
    mid = array[i]
    while i < j:
        while i < j and mid <= array[j]:
            j -= 1
        array[i] = array[j]
        while i < j and mid >= array[i]:
            i += 1
        array[j] = array[i]
    array[j] = mid
    quick_sort1(array, start, i - 1)
    quick_sort1(array, i + 1, end)
    return array


def quick_sort2(array, l, r):
    if l < r:
        q = partition(array, l, r)
        quick_sort2(array, l, q - 1)
        quick_sort2(array, q + 1, r)


def partition(array, l, r):
    x = array[r]
    i = l - 1
    for j in range(l, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1


def heap_sink(heap, heap_size, parent_index):
    """最大堆-下沉算法"""
    child_index = 2 * parent_index + 1

    # temp保存需要下沉的父节点，用于最后赋值
    temp = heap[parent_index]

    while child_index < heap_size:
        # 如果有右孩子，且右孩子比左孩子大，则定位到右孩子
        if child_index + 1 < heap_size and heap[child_index + 1] > heap[child_index]:
            child_index += 1

        # 如果父节点的值不小于左右孩子节点的值，可直接跳出循环
        if temp >= heap[child_index]:
            break

        heap[parent_index] = heap[child_index]
        parent_index = child_index
        child_index = 2 * parent_index + 1

    heap[parent_index] = temp


def heap_sort(mylist):
    """堆排序"""
    n = len(mylist)

    # 1. 无序列表构建成最大堆
    for i in range((n - 2) // 2, -1, -1):
        heap_sink(mylist, n, i)

    # 2. 循环删除堆顶元素，移到列表尾部，调节堆产生新的堆顶
    for i in range(n - 1, 0, -1):
        mylist[0], mylist[i] = mylist[i], mylist[0]
        heap_sink(mylist, i, 0)


if __name__ == "__main__":
    my_list = [1, 3, 4, 5, 2, 6, 9, 7]
    heap_sort(my_list)
    print(my_list)
