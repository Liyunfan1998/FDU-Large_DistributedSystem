#!/usr/bin/env python
# vim: set fileencoding=utf-8
import sys
from itertools import groupby
from operator import itemgetter
import random


def read_from_mapper(file, separator):
    for line in file:
        yield line.strip().split(separator, 2)

def main(separator = '\t',f=None):
    data = read_from_mapper(sys.stdin, separator)
    for line in data:
        f.write(str(line))
    f.close()
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            print ("%s%s%d" % (current_word, separator, total_count))
        except ValueError:
            pass

if __name__ == '__main__':
    filename = '/Users/liyunfan/Desktop/分布式系统/HWs/hbase/pystreaming/user_red.txt' + str(random.randint(1, 10))
    f = open(filename, 'wb+')
    main(f=f)
