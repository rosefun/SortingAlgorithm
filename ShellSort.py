import numpy as np
import time

class ShellSort():
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]
    def sort(self,arr):
        # 希尔排序
        gap = len(arr) // 2
        while gap > 0:
            for i in range(gap, len(arr)):
                j = i
                while (j >= gap) and (arr[j] < arr[j-gap]):
                    self.swap(arr, j, j-gap)
                    j = j-gap
            gap = gap//2
        return arr
    
if __name__ == "__main__":
    # 希尔排序
    arr = get_arr()
    start = time.time()
    shellSort = ShellSort()
    arr = shellSort.sort(arr)
    end = time.time()
    print('希尔排序use {:.4f}'.format(end-start))
    print(arr)
