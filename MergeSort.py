import numpy as np
import time

class MergeSort():
    def merge(self, arr, left, mid, right):
        l = left
        r = mid+1
        n_arr = [0 for _ in range(right-left+1)]
        index = 0
        while l <= mid and r<=right:
            if arr[l] > arr[r]:
                n_arr[index] = arr[r]
                r += 1
            else:
                n_arr[index] = arr[l]
                l += 1
            index += 1
        while l <= mid:
            n_arr[index] = arr[l]
            index += 1
            l += 1
        while r <= right:
            n_arr[index] = arr[r]
            index += 1
            r += 1
        # 拷贝排序完成的arr
        for i in range(len(n_arr)):
            arr[left+i] = n_arr[i]
            
    def mSort(self,arr, left, right):
        if left < right:
            mid = (left+right)//2
            self.mSort(arr, left, mid)
            self.mSort(arr, mid+1, right)
            self.merge(arr, left, mid, right)
            
    def sort(self, arr):
        self.mSort(arr, 0, len(arr)-1)
        return arr

def get_arr(num=200):
    np.random.seed(1)
    arr = np.random.randint(0,num,(num,))
    return arr 
    
if __name__ == "__main__":
    # 归并排序
    arr = get_arr()
    start = time.time()
    mergeSort = MergeSort()
    arr = mergeSort.sort(arr)
    end = time.time()
    print('归并排序use {:.4f}'.format(end-start))
    # print(arr)
