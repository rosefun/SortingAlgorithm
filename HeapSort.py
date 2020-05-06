import numpy as np
import time

class HeapSort():
    def siftDown(self, arr, index, length=None):
        '''sift_down'''
        if length is None:
            length = len(arr)
        # 最大堆；子节点总小于父节点, O(n)
        while True:
            left = 2*index + 1
            right = 2*index + 2
            max_idx = left
            if left >= length:
                break
            if right<length and arr[right] > arr[left]:
                max_idx = right
            if arr[index] < arr[max_idx]:
                arr[index], arr[max_idx] = arr[max_idx],arr[index]
                index = max_idx
            else:
                break
    def sort(self,arr):
        # 初始化最大堆 O(n)
        for idx in range(len(arr)//2-1, -1, -1):
            self.siftDown(arr, idx, len(arr))

        # 堆排序，交换最大值和最后一个叶节点, O(nlogn)
        for length in range(len(arr)-1, -1, -1):
            arr[length], arr[0] = arr[0], arr[length]
            self.siftDown(arr, 0, length)
        return arr 

def get_arr(num=200):
    np.random.seed(1)
    arr = np.random.randint(0,num,(num,))
    return arr 
    
if __name__ == "__main__":
    # 堆排序
    arr = get_arr()
    start = time.time()
    heapSort = HeapSort()
    arr = heapSort.sort(arr)
    end = time.time()
    print('堆排序use {:.4f}'.format(end-start))
    print(arr)
