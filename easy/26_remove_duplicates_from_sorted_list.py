#works with both sorted and un-sorted arrays
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

# works only with sorted array
def removeDuplicates1(nums):
    j=1
    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
            nums[j] = nums[i]
            j+=1
    return j, nums



mynums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(mynums)) # gives correct answer
print(removeDuplicates(mynums)) # gives correct answer after the mynums is updated(unsorted now)
mynums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates1(mynums)) # gives correct answer
print(removeDuplicates1(mynums)) # gives wrong answer as mynums is now updated to [0, 1, 2, 3, 4, 2, 2, 3, 3, 4] instead
