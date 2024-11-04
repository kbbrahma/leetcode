nums = [2,56,89,235, 461, 990]
target = 100

# nums = [1,3,5,6]
# target = 7
#
# nums = [1,3,5,6]
# target = 6
def binary_search(nums, target):
    start = 0
    end = len(nums)-1
    counter = 0
    while start<= end:
        mid = int((end+start)/2)
        if nums[mid] < target:
            start = mid+1
        elif nums[mid] > target:
            end = mid-1
        else:
            return mid
        counter+=1
    return end+1

print(binary_search(nums,target))