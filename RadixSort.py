import numpy as np
import time
import math

class RadixSort():
    def sort(self,arr,radix=10):
        '''基数排序，radix为基数'''
        K = int(math.ceil(math.log(max(arr)+1, radix)))
        for i in range(1,K+1):
            bucket = [[] for _ in range(radix)]
            for val in arr:
                bit = val%(radix**i)//(radix**(i-1))
                bucket[bit].append(val)
            # 合并桶
            del arr
            arr = []
            for bk in bucket:
                arr.extend(bk)
        return arr 

def get_arr(num=200):
    np.random.seed(1)
    arr = np.random.randint(0,num,(num,))
    return arr 
    
if __name__ == "__main__":
    # 基数排序
    arr = get_arr()
    start = time.time()
    radixSort = RadixSort()
    arr = radixSort.sort(arr,radix=10)
    end = time.time()
    print('基数排序use {:.4f}'.format(end-start))
    print(np.array(arr))
