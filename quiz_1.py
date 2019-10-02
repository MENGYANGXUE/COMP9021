# COMP9021 19T3 - Rachid Hamadi
# Quiz 1 *** Due Thursday Week 2


import sys
from random import seed, randrange

try:
    arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
mapping = {}
for i in range(1, upper_bound):
    r = randrange(-upper_bound // 2, upper_bound)
    if r > 0:
        mapping[i] = r
print('\nThe generated mapping is:')
print('  ', mapping)

mapping_as_a_list = []
one_to_one_part_of_mapping = {}
nonkeys = []

# INSERT YOUR CODE HERE

u = mapping.keys()
print(u)
p = len(u)
print(p)  ## mapping=len(mapping.keys)


for i in range(1, upper_bound): 
    nonkeys.append(i)
for i in range(1, upper_bound):
    if i in list(mapping.keys()):
        nonkeys.remove(i)


mapping_as_a_list = upper_bound * [None]
for key, value in mapping.items():
    print(key,value) #(2:4 3:8 4:7 5:7)
    mapping_as_a_list[key]=value

u = []  
uu = list(mapping.values())
for m in list(mapping.values()):
    if uu.count(m) == 1: 
        u.append(m) 
        print(u)


k = list(mapping.keys()) 

for v in u: #(4 8) 
    vv = list(mapping.values()).index(v) 
    s = k[vv] #(2 3)
    one_to_one_part_of_mapping[s] = v 





print('EDIT THIS PRINT STATEMENT')
print("The mappings's so-called \"keys\" make up a set whose number of elements is " + str(p) + ".")
print('\nThe list of integers between 1 and', upper_bound - 1, 'that are not keys of the mapping is:')
print('  ', nonkeys)
print('\nRepresented as a list, the mapping is:')
print('  ', mapping_as_a_list)
# Recreating the dictionary, inserting keys from smallest to largest,
# to make sure the dictionary is printed out with keys from smallest to largest.
one_to_one_part_of_mapping = {key: one_to_one_part_of_mapping[key]
                                  for key in sorted(one_to_one_part_of_mapping)
                                  }
print('\nThe one-to-one part of the mapping is:')
print('  ', one_to_one_part_of_mapping)
