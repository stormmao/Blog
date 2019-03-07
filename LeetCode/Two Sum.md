# 求数组中元素之和等于给定值的下标
- Given an array of integers, return indices of the two numbers such that they add up to a specific target.

  You may assume that each input would have exactly one solution, and you may not use the same element twice.
```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```
## 铁头娃做法
最容易想到的实现方法，但是时间复杂度比较高，为 O(n*n)，跑的时间领先全球，高达6690ms
```
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j] #后面的代码都注释掉也是可以的
                else:
                    j = j +1    #这里要设置自加，要不然j的值不会往后增加，会使得不满足条件就直接输出else下的值，以前我写的return None，就直接没了
            i = i +1
if __name__ == '__main__':
    sums = [1, 2, 3, 4]
    t = 3
    s = Solution()  # 新建一个类才能调用其中的方法
    q = s.twoSum(sums, t) #特地调试了一下
    print(q)
```
## 优雅的做法
```
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
        hash_table = {}
        for i in range(len(nums)): #时间复杂度为 O(n)
            if nums[i] in hash_table: # *target - nums[i]*就是要找的目标，如果数组中存在，就返回相应的下标，并且调出哈希表，返回对应的另外一个下标
                return [hash_table[nums[i]],i]
            else:
                hash_table[target - nums[i]] = i

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         for i, num in enumerate(nums):
            sub_num = target - num
            if sub_num in nums:
                t_index = nums.index(sub_num)
                if t_index != i:
                     return [i, t_index]
```
