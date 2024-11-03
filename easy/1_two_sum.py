def two_sum(arr, target):
    seen = {}
    for i,n in enumerate(arr):
        if target-n in seen:
            return [arr.index(target - n), i]
        elif n not in seen:
            seen[n] = i

array = [1,2,8,3]
target_num = 5

print(two_sum(array,target_num))
