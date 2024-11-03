def removeDuplicates(nums):
        seen = {}
        j = 0
        for i, n in enumerate(nums):
            if n not in seen:
                seen[n] = i
                nums[j] = n
                j+=1
            if n in seen:
                pass
        return len(seen), nums


def removeDuplicates1(nums):
    j=1
    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
            nums[j] = nums[i]
            j+=1
    return j, nums



mynums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(mynums))
print(removeDuplicates(mynums))
mynums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates1(mynums))
