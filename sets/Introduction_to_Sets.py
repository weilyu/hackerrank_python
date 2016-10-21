# https://www.hackerrank.com/challenges/py-introduction-to-sets


n = input()
line = input().split()
nums = set()
for s in line:
    curr = int(s)
    nums.add(curr)
print(sum(nums) / len(nums))
