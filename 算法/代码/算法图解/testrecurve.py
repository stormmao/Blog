#4.1 请编写前述sum函数的代码。
'''
def sum(num):

    if len(num) <= 1:
        return num[-1]
    else:
        return num[0] + sum(num[1:])
total = sum([1,2,3,4,5,6,9])
print(total)

#4.2 编写一个递归函数来计算列表包含的元素数
def count(list):
    if len(list) == 0:
        return 0
    if len(list) == 1:
        return 1
    else:
        return 1 + count(list[1:])
total = count([1,6,7])
print(total)
'''
#4.3 找出列表中最大的数字

def bigger(v1,v2):
    if v1 >= v2:
        return v1
    else:
        return v2

def max(list):
    if len(list) == 0:
        return None
    if len(list) == 1:
        return list[0]
    elif len(list) == 1:
        return bigger(list[0],list[1])
    else:
        return bigger(list[0],max(list[1:]))#此处少了一个调用函数max导致整数与列表比较大小，
        # 不过报错会报到bigger函数中去，使得不好追踪
biggestnum = max([9,6,5,4,8])
print(biggestnum)

