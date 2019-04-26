#!/usr/local/bin/python2
# vim: set fileencoding=utf-8
import sys
import random
import io
reload(sys)
sys.setdefaultencoding('utf8')

def read_from_input(file):
    for line in file:
        yield line.split(' ')


def main(f=None):
    # filenames = (sys.stdin).split('\t')
    # with open('/Users/liyunfan/Desktop/分布式系统/HWs/hbase/pyMR_HB/user_out.txt', 'wb+') as f:
    #     f.write(filenames + "\n")
    # print (filenames)
    # if 'N1' in filenames[0]:
    #     N1 = read_from_input(filenames[0])
    #     D1 = read_from_input(filenames[1])
    # elif 'D1' in filenames[0]:
    #     N1 = read_from_input(filenames[1])
    #     D1 = read_from_input(filenames[0])
    # filenamer = '/Users/liyunfan/Desktop/分布式系统/HWs/hbase/N1.txt'
    # fr = io.open(filenamer, 'r+', encoding='GB2312')
    # stdinr = fr.readlines()
    data = read_from_input(sys.stdin)
    # data = read_from_input(stdinr)
    for lineArr in data:
        while '' in lineArr:
            lineArr.remove('')
        # f.write(str(len(lineArr)) + "\t")
        if len(lineArr) == 2:
            words = lineArr
            id = words[0]
            pjname = words[1]
            print('%s%s%s%s' % (id, '\t', 'N#', pjname))
            # str_tmp = id + '\t' + 'N#' + pjname
            # f.write(str_tmp)
        elif len(lineArr) == 5:
            words = lineArr
            date = words[0]
            time = words[1]
            filesize = words[2]
            id = words[3][0:2]
            subid = words[3][2:]
            filename = words[4]
            print('%s%s%s%s%s%s%s%s%s%s%s' %
                  (id, '\t', 'D#', ' ', date, ' ', time, ' ', filesize, ' ', filename))
            # str_tmp = id + '\t' + 'D#' + ' ' + date + ' ' + time + ' ' + filesize + ' ' + filename
            # f.write(str_tmp)
    # f.close()


if __name__ == '__main__':
    # filename = '/Users/liyunfan/Desktop/分布式系统/HWs/hbase/pyMR_HB/user_out.txt' + str(random.randint(1, 10))
    # f = open(filename, 'wb+')
    f = ''
    main(f=f)
