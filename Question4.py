from itertools import permutations
def permutation(str):
    permlist=permutations(str)
    for permval in list(permlist):
        print(''.join(permval))

str='123'
permutation(str)