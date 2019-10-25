#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)
data3 = ['a', 'b', 'A', 'B']

# Реализация задания 2
print(str(list(Unique(data1)))[1:-1])
print(str(list(Unique(data2)))[1:-1])
print(str(list(Unique(data3)))[1:-1])
print(str(list(Unique(data3, ignore_case=True)))[1:-1])
