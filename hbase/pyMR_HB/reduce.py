#!/usr/local/bin/python2
# vim: set fileencoding=utf-8
import sys
from itertools import groupby
from operator import itemgetter
import sys
import random
import io

reload(sys)
sys.setdefaultencoding('utf8')

sys.path.append('/usr/local/lib/python2.7/site-packages')
import happybase


# def get_tables_name(host,port):
#     conn = happybase.Connection(host=host,port=port,protocol='compact',transport='framed')
#     return conn.tables()
#
# get_tables_name(host='localhost',port=9090)
# connection = happybase.Connection(host='localhost', port=9090, transport='framed', protocol='compact')
# families = {
#     # 'id': str(),
#     'pjname': dict(),
#     'year': dict(),
#     'date': dict(),
#     'time': dict(),
#     'filesize': dict(),
#     'subid': dict(),
#     'filename': dict(),
# }
# connection.create_table('hw5_id', families)
# sleep(3)
# table = connection.table('hw5_id')


def read_from_mapper(file, separator, f=None):
    for line in file:
        # f.write(line)
        yield line.split('\t')


def main(separator='\t', f=None):
    # filenamer = '/Users/liyunfan/Desktop/分布式系统/HWs/hbase/pyMR_HB/user_out.txt4'
    # fr = open(filenamer, 'r+')
    # stdinr = fr.readlines()
    # fr.close()
    # filenamer = '/Users/liyunfan/Desktop/分布式系统/HWs/hbase/pyMR_HB/user_out.txt10'
    # fr = open(filenamer, 'r+')
    # stdinr += fr.readlines()
    # fr.close()
    # data = []
    # for line in stdinr:
    #     data.append(line.decode('utf-8'))
    # print(line)
    # data = read_from_mapper(sys.stdin, separator, f)

    # connection = happybase.Connection(host='localhost', port=9090, transport='framed', protocol='compact')
    # table = connection.table('hw5_id')

    data = sys.stdin
    # data = read_from_mapper(stdinr, separator, f)
    # print(data)
    # for id, group in groupby(data, itemgetter(0)):
    try:
        # for line in data:
        #     for word in line:
        #         f.write(word)
        #     f.write('\n')
        # f.close()
        dict = {}
        for d in data:
            d = d.strip().split('\t')
            if d[0] not in dict.keys() and len(d) >= 2:
                dict[d[0]] = [d[1]]
            elif len(d) >= 2:
                # print(d[0], dict[d[0]])
                dict[d[0]] = dict[d[0]] + [d[1]]
        # print(dict)
        for id in dict:
            N, D = [], []
            for tb in dict[id]:
                # print(id, tb[2:])
                if tb[0:2] == 'N#':
                    N.append(tb[2:])
                elif tb[0:2] == 'D#':
                    D.append(tb[2:])
            # write to hbase
            # print(id,N)
            if len(N) > 0 and len(D) > 0:
                for d in D:
                    d = d.split(' ')
                    while '' in d:
                        d.remove('')
                    for n in N:
                        print(id, n, d[0], d[0][0:4], d[1], d[2], d[3])
                        # tmpstr = str(id + n + d[0] + d[0][0:4] + d[1] + d[2] + d[3] + '\n')
                        # f.write(tmpstr)

                        table.put(id, {b'pjname:pj_name': n, b'date:date_full': d[0], b'time:time_full': d[1],
                                       b'filename:filename_full': d[3], b'year:date_year': d[0][0:4],
                                       b'filesize:filesize_num': d[2]})

            else:
                print(id, n, '', '', '', '', '')
                # tmpstr = str(id + n + '' + '' + '' + '' + '' + '\n')
                # f.write(tmpstr)

        # f.close()
    except ValueError:
        pass


if __name__ == '__main__':
    # filename = '/Users/liyunfan/Desktop/分布式系统/HWs/hbase/pyMR_HB/user_red.txt' + str(random.randint(1, 10))
    # f = open(filename, 'wb+')
    f = ''
    main(f=f)
