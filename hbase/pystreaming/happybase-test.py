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
print(row[b't1:tt1'])  # prints 'value1'

# for key, data in table.rows([b'row-key-1', b'row-key-2']):
#     print(key, data)  # prints row key and data for each row
#
# for key, data in table.scan(row_prefix=b'row'):
#     print(key, data)  # prints 'value1' and 'value2'
