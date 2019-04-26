import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import happybase
# DO THIS IN SHELL!!!
# hbase-daemon.sh   start   thrift -c compact protocol  -p   9090
def get_tables_name(host,port):
    conn = happybase.Connection(host=host,port=port,protocol='compact',transport='framed')
    return conn.tables()

get_tables_name(host='localhost',port=9090)
connection = happybase.Connection(host='localhost',port=9090,transport='framed', protocol='compact')
table = connection.table('S1')
table.put(b'row1', {b't1:tt1': b'value1'})
row = table.row(b'row1')
print(row[b't1:tt1'])

# for key, data in table.rows([b'row-key-1', b'row-key-2']):
#     print(key, data)  # prints row key and data for each row
#
# for key, data in table.scan(row_prefix=b'row'):
#     print(key, data)  # prints 'value1' and 'value2'


hw5_id
date
filename
filesize
pjname
subid
time
year
table.put(id, {b'date': })
table.put(id, {b'pjname:pj_name': n, b'date:date_full': d[0], b'time:time_full': d[1],
               b'filename:filename_full': d[3], b'year:date_year': d[0][0:4],
               b'filesize:filesize_num': d[2]})