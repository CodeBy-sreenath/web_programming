from collections import Counter
import heapq
def max_freq_element(nums,k):
    frq=Counter(nums)
    heap=[]
    for num,count in frq.items():
        heapq.heappush(heap,(count,num))
        if len(heap)>k:
            heapq.heappop(heap)
    return [num for count,num in heap] 
print(max_freq_element([1,2,3,3,3,4,4],2))       