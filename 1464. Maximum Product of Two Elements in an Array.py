# Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).

nums = [3,4,5,2]

i = 0
j = 0

maxNum= max(nums)
index = nums.index(maxNum)
i = nums[index]
nums.pop(index)

maxNum= max(nums)
index = nums.index(maxNum)
j = nums[index]

(i-1)*(j-1)
