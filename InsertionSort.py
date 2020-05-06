import numpy as np
import time

class InsertionSort():
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]
    def sort(self,arr):
        for i in range(len(arr)):
            for j in range(i, 0, -1):
                if arr[j] < arr[j-1]:
                    self.swap(arr, j, j-1)
                else:
                    break
        return arr 

def get_arr(num=200):
    np.random.seed(1)
    arr = np.random.randint(0,num,(num,))
    return arr 
    
if __name__ == "__main__":
    # 插入排序
    arr = get_arr()
    start = time.time()
    insertionSort = InsertionSort()
    arr = insertionSort.sort(arr)
    end = time.time()
    print('插入排序use {:.4f}'.format(end-start))
    print(arr)
