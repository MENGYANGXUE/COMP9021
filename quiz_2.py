# COMP9021 19T3 - Rachid Hamadi
# Quiz 2 *** Due Thursday Week 3


import sys
from random import seed, randrange
from pprint import pprint

try:
    arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
mapping = {}
for i in range(1, upper_bound):
    r = randrange(-upper_bound // 8, upper_bound)
    if r > 0:
        mapping[i] = r
print('\nThe generated mapping is:')
print('  ', mapping)
# sorted() can take as argument a list, a dictionary, a set...
keys = sorted(mapping.keys())
print('\nThe keys are, from smallest to largest: ')
print('  ', keys)

cycles = []
reversed_dict_per_length = {}

# INSERT YOUR CODE HERE
bi=[]
Duo=[]
visited=[]
for i in mapping:#判断一元环
    if i not in visited:
        value = mapping[i]
        if i == mapping[i]:
            bi.append(i)
            cycles.append(bi)
            visited.append(i)

        else:#判断多元环
            Duo = [i, mapping[i]]

            while value in list(mapping.keys()):  # 判断非环
                newkeys = value
                value = mapping[newkeys]
                if mapping[newkeys] == Duo[0]:#判断没尾巴
                    cycles.append(Duo)
                    visited.extend(Duo)
                    break
                elif mapping[newkeys] != Duo[0] and mapping[newkeys] in Duo:#判断有尾巴
                    break
                Duo.append(mapping[newkeys])

allval = mapping.values()
setval = set(allval)
ed = {}
ex = {}
biglen = 0
vvalue = list(mapping.values())
for v in vvalue:
    if vvalue.count(v) > biglen:
        biglen = vvalue.count(v)
print(biglen)
for e in setval:
    ek = []
    for k,v in mapping.items():
        if e == v:
            ek.append(k)
    ed.update({e:sorted(ek)})

print(ed)
for ar in range(1, biglen + 1):
    for w,q in ed.items():
        if ar == len(q):
            ex[w] = q
    if ex != {}:
        reversed_dict_per_length[ar] = ex
    ex = {}



print('\nProperly ordered, the cycles given by the mapping are: ')
print('  ', cycles)
print('\nThe (triply ordered) reversed dictionary per lengths is: ')
pprint(reversed_dict_per_length)


