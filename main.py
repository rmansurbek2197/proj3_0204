# 11
def diff_without_min_max(lst):
    temp = lst.copy()
    temp.remove(max(temp))
    temp.remove(min(temp))
    return max(temp) - min(temp)

# 12
def invert_numbers(lst):
    return [-x if x != 0 else 0 for x in lst]

# 13
def chunk_list(lst, size):
    return [lst[i:i+size] for i in range(0, len(lst), size)]

# 14
def count_elements(lst):
    d = {}
    for x in lst:
        d[x] = d.get(x, 0) + 1
    return d
