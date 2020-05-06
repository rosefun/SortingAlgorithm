import numpy as np
import time
class BubbleSort():
    def sort(self,arr):
        for i in range(len(arr)-1, 0, -1):
            for j in range(i):
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
        return arr 
        
def get_arr(num=200):
    np.random.seed(1)
    arr = np.random.randint(0,num,(num,))
    return arr 
    
if __name__ == "__main__":
    # 冒泡法
    arr = get_arr()
    start = time.time()
    bubbleSort = BubbleSort()
    arr = bubbleSort.sort(arr)
    end = time.time()
    print('冒泡法use {:.4f}'.format(end-start))
    print('排序后arr',arr)
