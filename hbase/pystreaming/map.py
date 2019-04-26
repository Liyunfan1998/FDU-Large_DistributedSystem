#!/usr/bin/python2.7
# vim: set fileencoding=utf-8
import sys
import random

def read_from_input(file):
    for line in file:
        yield line.split(' ')


def main(separator = ' '):
    data = read_from_input(sys.stdin)
    """
    input = sys.stdin
    input = input.split()
    for word in input:
        print ('%s%s%d' % (word, '\t', 1))
    """
    for words in data:
        for word in words:
            # write to the reduce
            print ('%s%s%d' % (word, '\t', 1))
if __name__ == '__main__':
    filename = '/Users/liyunfan/Desktop/分布式系统/HWs/hbase/pystreaming/user_out.txt' + str(random.randint(1,10))
    f = open(filename, 'wb+')
    data = read_from_input(sys.stdin)
    # for lineArr in data:
    #     tmp = list(lineArr)
    #     for w in tmp:
    #         if len(w)==0:
    #             lineArr.remove(w)
    for lineArr in data:
        while '' in lineArr:
            lineArr.remove('')
        f.write(str(len(lineArr))+"\t")
        # for word in words:
        #     f.write(word)
    main()
