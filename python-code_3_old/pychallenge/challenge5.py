# coding=utf-8

import pickle

file = open('./data/banner.p', 'rb')
data = pickle.load(file)
file.close()

for x in data:
    for y in x:
        print(y[0] * y[1], end='')
    print('    ' + str(x))

del data