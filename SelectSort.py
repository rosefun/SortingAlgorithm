import numpy as np
import time

class SelectSort():
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]
    def sort(self,arr):
        for i in range(len(arr)):
            min_idx = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            self.swap(arr, min_idx, i)
        return arr 

def get_arr(num=200):
    np.random.seed(1)
    arr = np.random.randint(0,num,(num,))
    return arr 
    
if __name__ == "__main__":
    # 选择排序
    arr = get_arr()
    start = time.time()
    selectSort = SelectSort()
    arr = selectSort.sort(arr)
    end = time.time()
    print('选择排序use {:.4f}'.format(end-start))
    print(arr)
