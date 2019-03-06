# 求数组中元素之和等于给定值的下标
- Given an array of integers, return indices of the two numbers such that they add up to a specific target.

  You may assume that each input would have exactly one solution, and you may not use the same element twice.
```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```
## 铁头娃做法
最容易想到的实现方法，但是时间复杂度比较高，为 O(n*n)
```
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if nums[i] + nums[j] == target:
                    return i,j
                else:
                    return None
```
