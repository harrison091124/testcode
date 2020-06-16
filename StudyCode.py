def majority_vote(ll):
    if ll:
        ss = list(set(ll))
        lll = [len([i for i in ll if s == i]) for s in ss]
        if max(lll) <= len(ll) / 2:
            return None
        else:
            return ss[lll.index(max(lll))]
    else:
        return None

import numpy as np
def tallest_skyscraper(lst):
    l = np.array(lst, np.int8).T
    return max([sum(i) for i in l])

def tallest_skyscraper2(A):
    return sum(1 in R for R in A)

import math
def id_mtrx(n):
    s = int(math.copysign(1,n))
    n = abs(n)
    return [[int(i == r) for i in range(n)][::s] for r in range(n)]


def block(lst):
    return sum((len(lst) - 1 - i) * lst[i].count(2) for i in range(len(lst)))

print(block([
  [1, 1, 1, 1, 1],
  [1, 1, 2, 1, 1],
  [1, 1, 1, 1, 2],
  [1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1]
]))

def only_5_and_3(num):
    if num <= 0:
        return False
    elif only_5_and_3(num-5) or (num % 3 == 0 and only_5_and_3(num/3)):
        return True
    elif num == 3 or num == 5:
        return True
    else:
        return False


if __name__ == '__main__':
    #print(id_mtrx(4))
    print(only_5_and_3(14))
    print(only_5_and_3(25))
    print(only_5_and_3(7))
