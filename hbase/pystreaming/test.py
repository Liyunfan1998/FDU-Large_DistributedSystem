# -*- coding:utf-8 -*-
import io
filename = '/Users/liyunfan/Desktop/分布式系统/HWs/hbase/pyMR_HB/user_out.txt9'
f = io.open(filename, encoding='gb2312')
data=f.readlines()
# filename = '/Users/liyunfan/Desktop/分布式系统/HWs/hbase/pyMR_HB/user_red.txt8'
# f2 = open(filename, 'wb+')
# for id, group in groupby(data, itemgetter(0)):
#     concat = ''
#     for id, tb in group:
#         print(id,tb)
#         if tb[0:2] == 'N#':
#             concat += (tb[2:])
#         elif tb[0:2] == 'D#':
#             concat += (' ' + tb[2:])
#         f2.write(concat+'\n')

dict = {}
for d in data:
    d = d.split('\t')
    # print(d)
    if d[0] not in dict.keys():
        dict[d[0]] = list()
    else:
        print(d[0],dict[d[0]])
        dict[d[0]] = dict[d[0]]+[d[1].strip()]
for id in dict:
    # print(id)
    # N,D = [],[]
    for tb in dict[id]:
        print(tb[0:2])
        if tb[0:2] == 'N#':
            N.append(tb[2:])
        elif tb[0:2] == 'D#':
            D.append(tb[2:])
    # write to hbase
    for n in N:
        n = n.split(' ')
        for d in D:
            # print(len(concat), concat)
            print(id, d, n[0], n[1][0:4], n[1], n[2], n[3], n[4], n[5])



table.put(d[0], {b'pjname:pj_name': d[4], b'date:date_full': d[5], b'time:time_full': d[1],
               b'filename:filename_full': d[3], b'year:date_year': d[0][0:4],
               b'filesize:filesize_num': d[2]})
