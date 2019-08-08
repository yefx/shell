# coding:utf8
import sys
import xlwt
#import MySQLdb
import pymysql as MySQLdb
import datetime

def get_conn_mysql():
    conn = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='root', db='test', charset='utf8')
    return conn
def query_data(cur, sql, args):
    cur.execute(sql, args)
    return cur.fetchall()

# out_path 保存的路径， sql： 需要执行的语句
def read_mysql_to_excel(out_path, sql):
    conn = get_conn_mysql()
    cursor = conn.cursor()
    count = cursor.execute(sql)
    if count != 0:
        print(count)
        cursor.scroll(0, mode='absolute')
        results = cursor.fetchall()
        fields = cursor.description
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('building', cell_overwrite_ok=True)

        for field in range(0, len(fields)):
            sheet.write(0, field, fields[field][0])

        row = 1
        col = 0
        for row in range(1, len(results)+1):
            for col in range(0, len(fields)):
                if results[row-1][col] != None:
                    sheet.write(row, col, u'%s'%results[row-1][col])
                else:
                    val = ''
                    sheet.write(row, col, u'%s'%val)
        workbook.save(out_path)
if __name__ == '__main__':
    # 执行的sql语句
    sql = 'select * from sys_user'
    read_mysql_to_excel('1.xls', sql)
