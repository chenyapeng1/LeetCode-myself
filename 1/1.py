# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

# 示例:

# 给定 nums = [2, 7, 11, 15], target = 9

# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]


# 第一个是常规解法，也是最先想到的想法，原理就是利用两层循环去解决问题，问题就是耗时过长，力扣耗时3784ms
def twoSum_one(nums,target):
    n = len(nums)
    for i in range(n):
        for j in range(i,n):
            if nums[i]+nums[j] == target:
                return [nums[i],nums[j]]

print(twoSum_one([1,2,3,4,5],9))

# 第二个是上一种方法的改进，只需要一次循环，另一个值使用target-nums[i]来代替的，只需要查询nums中是否有那个值，就可以得出结果，力扣耗时1192ms
def twoSum_two(nums,target):
    n = len(nums)
    for i in range(n):
        a = target-nums[i]
        if a in nums:
            j = nums.index(a)
            if j == i:
                continue
            else:
                return [i,j]
        else:
            continue

print(twoSum_two([1,2,3,4,5],5))

# 惊为天人，这种解法的力扣耗时只有60ms，第一次见的话会有点蒙，只有亲自上手算一下才知道它的妙处。先创建一个空字典，然后依次把target-nums[i]的值存入字典，存入一个就跟nums[i+1]去比较，字典中的key为target-nums[i]，value为i，也就是nums[i]在nums列表中的索引位置。当字典中有nums[i+1]时，也就是target-nums[y]=nums[i+1]，所以是return [b[nums[i]],i]
def twoSum_three(nums,target):
    n = len(nums)
    b={}
    for i in range(n):
        a = target-nums[i]
        if nums[i] in b:
            return [b[nums[i]],i]
        else:
            b[a]=i

print(twoSum_three([1,2,3,4,5],7))