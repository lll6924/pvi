import pandas as pd
import numpy as np
import random

def get_matrix(features):
    with open('data/cps2000-04-08-DKs.dat', 'r') as f:
    #with open('data/votechoice2000-04-08.dat', 'r') as f:
        header = f.readline()
        main = f.readlines()
    random.Random(0).shuffle(main)
    D = len(features) + 1
    counter = 0
    sets = [set() for _ in range(D-1)]
    nums = np.array((51, 4, 5, 4, 2, 5))
    sum = np.zeros(tuple(nums[features-1]))
    pos = np.zeros(tuple(nums[features-1]))
    for line in main:
        all = line.split()
        filtered = False
        for i in range(D-1):
            if all[features[i]] == 'NA':
                filtered = True
        if all[0] == 'NA':
            filtered = True
        if filtered:
            continue
        if not all[10].endswith('2000-cps\"'):
            continue
        counter += 1
        if counter > 40000:
            continue
        indexes = []
        for i in range(D-1):
            sets[i].add(int(all[features[i]]))
            indexes.append(int(all[features[i]])-1)
        #if indexes[0]>0:
        #    indexes[0] -= 1
        sum[*indexes] += 1
        pos[*indexes] += int(all[0])

    #print(sets, counter)
    print(np.sum(sum), 'collected')
    return tuple(nums[features-1]), sum, pos

def get_matrix_valid(features):
    with open('data/cps2000-04-08-DKs.dat', 'r') as f:
    #with open('data/votechoice2000-04-08.dat', 'r') as f:
        header = f.readline()
        main = f.readlines()
    random.Random(0).shuffle(main)
    D = len(features) + 1
    counter = 0
    sets = [set() for _ in range(D-1)]
    nums = np.array((51, 4, 5, 4, 2, 5))
    sum = np.zeros(tuple(nums[features-1]))
    pos = np.zeros(tuple(nums[features-1]))
    for line in main:
        all = line.split()
        filtered = False
        for i in range(D-1):
            if all[features[i]] == 'NA':
                filtered = True
        if all[0] == 'NA':
            filtered = True
        if filtered:
            continue
        if not all[10].endswith('2000-cps\"'):
            continue
        counter += 1
        if counter <= 40000 or counter > 55000:
            continue
        indexes = []
        for i in range(D-1):
            sets[i].add(int(all[features[i]]))
            indexes.append(int(all[features[i]])-1)
        #if indexes[0]>0:
        #    indexes[0] -= 1
        sum[*indexes] += 1
        pos[*indexes] += int(all[0])

    #print(sets, counter)
    print(np.sum(sum), 'collected')
    return tuple(nums[features-1]), sum, pos

def get_matrix_test(features):
    with open('data/cps2000-04-08-DKs.dat', 'r') as f:
    #with open('data/votechoice2000-04-08.dat', 'r') as f:
        header = f.readline()
        main = f.readlines()
    random.Random(0).shuffle(main)
    D = len(features) + 1
    counter = 0
    sets = [set() for _ in range(D-1)]
    nums = np.array((51, 4, 5, 4, 2, 5))
    sum = np.zeros(tuple(nums[features-1]))
    pos = np.zeros(tuple(nums[features-1]))
    for line in main:
        all = line.split()
        filtered = False
        for i in range(D-1):
            if all[features[i]] == 'NA':
                filtered = True
        if all[0] == 'NA':
            filtered = True
        if filtered:
            continue
        if not all[10].endswith('2000-cps\"'):
            continue
        counter += 1
        if counter <= 55000:
            continue
        indexes = []
        for i in range(D-1):
            sets[i].add(int(all[features[i]]))
            indexes.append(int(all[features[i]])-1)
        #if indexes[0]>0:
        #    indexes[0] -= 1
        sum[*indexes] += 1
        pos[*indexes] += int(all[0])

    #print(sets, counter)
    print(np.sum(sum), 'collected')
    return tuple(nums[features-1]), sum, pos

if __name__ == '__main__':
    shape, sum, pos = get_matrix( np.array([1, 2, 3]))
    print(shape, sum, pos)