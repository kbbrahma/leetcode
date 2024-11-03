def remove_element(nums,val):
    j=0
    for n in nums:
        if n!=val:
            nums[j] = n
            j+=1
    return j,nums

nums = [3,2,2,3]
val = 3
print(remove_element(nums,val))

nums = [0,1,2,2,3,0,4,2]
val = 2
print(remove_element(nums,val))