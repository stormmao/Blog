def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])                               #这里如果list很大，栈的空间就会很大，因为max()函数一直在运行，只到list被切分成长度为2
    return list[0] if list[0] > sub_max else sub_max
print(max([11,2,3,4,5,6,7,8,9]))