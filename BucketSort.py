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

class BucketSort():
    def get_index(self, val, min_a, radix):
        return (val - min_a) // radix
        
    def sort(self,arr, radix=10):
        '''radix,基数代表一个桶最大容纳多少个不同的数；
        当radix=1, 桶排序相当于计数排序.'''
        max_a = max(arr)
        min_a = min(arr)
        bucket_num = (max_a - min_a)//radix + 1
        bucket = [[] for _ in range(bucket_num)]
        # 放入桶中
        for val in arr:
            index = self.get_index(val, min_a,radix)
            bucket[index].append(val)
        index = 0
        insertionSort = InsertionSort()
        for bk in bucket:
            # 桶内进行排序
            bk = insertionSort.sort(bk)
            for val in bk:
                arr[index] = val
                index += 1
        return arr

def get_arr(num=200):
    np.random.seed(1)
    arr = np.random.randint(0,num,(num,))
    return arr 
    
if __name__ == "__main__":
    # 桶排序
    arr = get_arr()
    start = time.time()
    bucketSort = BucketSort()
    arr = bucketSort.sort(arr,radix=10)
    end = time.time()
    print('桶排序use {:.4f}'.format(end-start))
    print(arr)
