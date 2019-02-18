#insert_sort.py
def getNum():
    nums = []
    inumstr = input()
    while inumstr!=' ':
        nums.append(eval(inumstr))
        inumstr = input()
    return nums

def insert(nums):
    length = len(nums)
    if length <= 0:
        return None
    for i in range(1,length):
        for j in range(i,0,-1):
            if nums[j-1] > nums[j]:
                p = nums[j-1]
                nums[j - 1] = nums[j]
                nums[j] = p
                #nums[j-1],nums[j] = nums[j],nums[j-1]
            else:
                break
    return nums
def main():
    a =getNum()
    b = insert(a)
    for i in b:
        print(i)

main()



