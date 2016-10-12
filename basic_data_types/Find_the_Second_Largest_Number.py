# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list

n = int(input())
raw_input = input().split()
nums = list()
for s in raw_input:
    nums.append(int(s))
nums.sort()
largest = nums[n - 1]
i = n - 1
while i >= 0:
    if nums[i] < largest:
        print(nums[i])
        break
    else:
        i -= 1
