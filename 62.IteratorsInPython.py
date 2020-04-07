nums=[7,8,9,5]

print(nums[3])

for i in nums:
    print(i)

it=iter(nums)
print(it.__next__())
print(it.__next__())

print(next(it))


