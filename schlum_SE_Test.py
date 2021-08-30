import itertools

def odd_even_list(n):
    odd = list(itertools.permutations(list(range(1, n+1, 2))))
    even = list(itertools.permutations(list(range(2, n+1, 2))))
    odd = [list(i) for i in odd]
    even = [list(i) for i in even]
    return odd, even

def merge(list1, list2):
    if len(list1) < len(list2):
        return -1
    result = [None]*(len(list1)+len(list2))
    result[::2] = list1
    result[1::2] = list2
    return result



def alternating_parity_permutations(n):
    odd, even = odd_even_list(n)
    list1 = list(itertools.product(odd,even))
    list2 = list(itertools.product(even,odd))
    output = []
    for l1, l2 in list1:
        res = merge(l1, l2)
        if res == -1:
            continue
        output.append(res)
    for l1, l2 in list2:
        res = merge(l1, l2)
        if res == -1:
            continue
        output.append(res)
    return output

perms = alternating_parity_permutations(2)
print(perms)