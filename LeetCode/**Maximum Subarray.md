- Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.
### Example:
> Input: [-2,1,-3,4,-1,2,1,-5,4],
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.
    
### Follow up:
     - If you have figured out the O(n) solution, try coding another solution 
     using the divide and conquer approach, which is more subtle.
- 发现使用以前的穷举算法不行，提交不了。时间复杂度太高了，没有想出解决的好办法勒，参考了别人的代码~
```
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxnum = nums[0]
        sumn = 0
        for i in range(1,len(nums)):
            if nums[i-1] >0:
                nums[i] += nums[i-1]
        return max(nums)
```
- 本来使用另外一种方法实现不了的，无法识别[-2]的输入，而且怎么都无法解决这个问题，后来发现条件判断语句交换一下位置就好了，阿西吧。
```
def maxSequence1(arr):
    max,curr = 0,0
    for x in arr:
        curr+=x
        if curr<0:curr=0
        if curr>max:max=curr
    return max
print(maxSequence1([-2]))
结果为：0

def maxSequence1(arr):
    max,curr = -float('inf'),0
    for x in arr:
        curr+=x
        if curr > max: max = curr
        if curr<0:curr=0
    return max
print(maxSequence1([-2]))
结果为：-2
```
