import numpy as np
import time

class QuickSort():
    def select_base(self,arr,low,high):
        # 取三个数的中位数
        mid = (low + high) // 2
        if (arr[low] - arr[mid])*(arr[low] - arr[high]) < 0:
            return low
        if (arr[mid] - arr[low])*(arr[mid] - arr[high]) < 0:
            return mid
        return high

    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]
        
    def qsort(self,arr, low, high):
        left, right = low, high
        if left < right:
            while left < right:
                pivot = self.select_base(arr, low, high)
                # 基准放在最左边low
                self.swap(arr, low, pivot)
                # 从右到左遍历，选择比基准小的元素
                while left < right and arr[right] >= arr[low]:
                    right -= 1
                # 从左到右遍历，选择比基准大的元素
                while left < right and arr[left] <= arr[low]:
                    left += 1
                self.swap(arr, left, right)
            # 最终 left = right，该位置元素不大于基准
            self.swap(arr, low, right)
            self.qsort(arr, low, right-1)
            self.qsort(arr,right+1, high)
            
    def sort(self,arr):
        self.qsort(arr,0,len(arr)-1)
        return arr

def get_arr(num=200):
    np.random.seed(1)
    arr = np.random.randint(0,num,(num,))
    return arr 
    
if __name__ == "__main__":
    # 快排
    arr = get_arr()
    start = time.time()
    quickSort = QuickSort()
    arr = quickSort.sort(arr)
    end = time.time()
    print('快排use {:.4f}'.format(end-start))
    print(arr)
