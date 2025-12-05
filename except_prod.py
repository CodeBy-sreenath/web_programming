def productExceptSelf(nums):
    n = len(nums)
    result = [1] * n

    # Left product pass
    left = 1
    for i in range(n):
        result[i] = left
        left *= nums[i]
    
    # Right product pass
    right = 1
    for i in range(n-1, -1, -1):
        result[i] *= right
        right *= nums[i]

    return result

# Example
print(productExceptSelf([1,2,3,4]))
