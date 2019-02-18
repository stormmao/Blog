def max(list):
    if len(list) == 2:
        if list[0] > list[1]:
            return list[0]
        else:
            return list[1]
    sub_max = max(list[1:])
    if list[0] > sub_max:
        return list[0]
    else:
        return sub_max
print(max([16,21,19,8]))