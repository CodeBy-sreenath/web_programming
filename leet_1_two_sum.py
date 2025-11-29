def two_sums(nums,target):
    seen={}
    for i,num in enumerate(nums):
        complement=target-num
        if complement in seen:
            return [seen[complement],i]
        seen[num]=i
    return []
nums=[2,7,11,5] 
target=9
result=two_sums(nums,target)
print("the array is",nums)
print("the target is",target)
print(result)   