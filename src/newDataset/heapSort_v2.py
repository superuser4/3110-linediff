def HeapSort(alist):
    make_heap(alist)              # create the heap
    end = len(alist) - 1
    while (0 < end):
        alist[end], alist[0] = alist[0], alist[end]
        shiftDown(alist, 0, end - 1)
        end -= 1
        
#this function helps to maintain the heap property
def make_heap(alist):
    start = (len(alist) - 2) // 2     # faster execution
    while start >= 0:
        shiftDown(alist, start, len(alist) - 1)
        start -= 1

def shiftDown(alist, start, end):
    root = start
    while root * 2 + 1 <= end:
        child = root * 2 + 1
        # right child exists and is greater than left child
        if child + 1 <= end and alist[child] < alist[child + 1]:
            child = child + 1
        # if child is greater than root(parent), then swap their positions
        if child <= end and alist[root] < alist[child]:
            alist[root], alist[child] = alist[child], alist[root]
            root = child
        else:
            return

if __name__ == '__main__':
    alist = [12, 2, 4, 5, 2, 3]
    HeapSort(alist)
    print('Sorted Array:',alist)