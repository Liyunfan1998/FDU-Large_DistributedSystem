# -*- coding:utf-8 -*-
import sys

sys.path.append('/usr/local/lib/python2.7/site-packages')
import happybase


# DO THIS IN SHELL!!!
# hbase-daemon.sh   start   thrift -c compact protocol  -p   9090
def get_tables_name(host, port):
    conn = happybase.Connection(host=host, port=port, protocol='compact', transport='framed')
    return conn.tables()


# get_tables_name(host='localhost',port=9090)
connection = happybase.Connection(host='localhost', port=9090, transport='framed', protocol='compact')
# families = {
#     'id': dict(),
#     'pjname': dict(),
#     'year': dict(),
#     'date': dict(),
#     'time': dict(),
#     'filesize': dict(),
#     'filename': dict(),
# }
# connection.create_table('hw5_fn', families)

table = connection.table('hw5_fn')
# 按文件名和项目编号可快速查询到文件信息 hpbt2.txt
query_str2 = "SingleColumnValueFilter ('filename', 'filename_full', =, " \
             "'substring:\xe6\xa5\xbc\xe6\xa2\xaf\xe8\xaf\xa6\xe5\x9b\xbe5_t3.dwg')" \
             " AND SingleColumnValueFilter ('id', 'id_pre', =, 'substring:18')"

for k, v in table.scan(filter=query_str2, sorted_columns=True):
    print(k, v)

"""
# 按项目编号分组输出 id.txt
ids = []
all = []
for k, v in table.scan(sorted_columns=False, columns=['id']):
    ids.append(v['id:id_pre'])

for id in ids:
    tmp = []
    query_str1 = "SingleColumnValueFilter ('id', 'id_pre', =, 'substring:" + id + "')"
    for k, v in table.scan(filter=query_str1, sorted_columns=True):
        tmp.append(dict(v))
    all.append(tmp)
    # for ki, vi in v.items():
    #     tmp.append(vi)
    #     print(vi)
    # print(table.rows([id], columns=None, timestamp=None, include_timestamp=False))

print(all)
"""

"""
# 按图纸年份分组输出 yr.txt
yrs = []
all = []
for k, v in table.scan(sorted_columns=False, columns=['year']):
    yrs.append(v['year:date_year'])

for y in yrs:
    tmp = []
    query_str1 = "SingleColumnValueFilter ('year', 'date_year', =, 'substring:" + y + "')"
    for k, v in table.scan(filter=query_str1, sorted_columns=True):
        tmp.append(dict(v))
    all.append(tmp)
print(all)
"""
