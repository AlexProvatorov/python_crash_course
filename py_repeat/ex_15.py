# put your python code here
nums = input().split()
for i, num in enumerate(nums):
    if float(num) < 0:
        nums[i] = -1.0
print(nums)