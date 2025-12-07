def three_sums(nums):
    nums.sort()
    resut=[]
    for i in range(len(nums)-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        left,right=i+1,len(nums)-1
        while left<right:
            total=nums[i]+nums[left]+nums[right]
            if total==0:
                resut.append([nums[i],nums[left],nums[right]])
                left+=1
                right-=1
                while left<right and nums[left]==nums[left-1]:
                    left+=1
                while left<right and nums[right]==nums[right-1]:
                    right-=1
            elif total>0:
                right-=1
            else:
                left+=1
    return resut
print(three_sums([-4,1,-1,-1,0,2]))                            
                    