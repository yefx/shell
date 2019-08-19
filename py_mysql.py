# coding:utf8
import sys
import xlwt
#import MySQLdb
import pymysql as MySQLdb
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

def get_conn_mysql():
        conn = MySQLdb.connect(host='xx.xx.xx', port=3306, user='username', passwd='userpd', db='db-name', charset='utf8')
        return conn
def query_data(cur, sql, args):
        cur.execute(sql, args)
        return cur.fetchall()

# out_path 保存的路径， sql： 需要执行的语句
def read_mysql_to_excel(file_path, sql):
    conn = get_conn_mysql()
    cursor = conn.cursor()
    count = cursor.execute(sql)
    if count != 0:
        #        print(count)
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
        workbook.save(file_path)
def send_mail(to,host,file_path):
    sender = 'yefuxiong@139.com'
    user = 'yefuxiong@139.com'
    password = 'yfx960216'
    subject = '导出数据'
    content = '您所需要的数据导出，请见附件。'
    with open(file_path, 'rb') as f:
        txt = MIMEText(f.read(), 'plain', 'gbk')
        txt['Content-Type'] = 'application/octet-stream'
        txt['Content-Disposition'] = "attachment;filename=%s" %(file_path)
    email = MIMEMultipart()
    email.attach(MIMEText(content, 'plain', 'utf-8'))
    email.attach(txt)
    email['Subject'] = subject
    email['From'] = sender
    email['To'] = ",".join(to)
    msg = email.as_string()
#    print('Logging with server...')
    smtpObj = smtplib.SMTP_SSL(host,465)
    smtpObj.ehlo()
    smtpObj.login(user, password)
#    print('Login successful.')
    smtpObj.sendmail(sender, to, msg)
    smtpObj.quit()
    print('Email has been sent')
if __name__ == '__main__':
    sql = "SELECT * from user"
    file_path = './TestCase.xls'
    read_mysql_to_excel(file_path, sql)
    to = ['yefuxiong@vip.qq.com','yefuxiong@live.com']
    host = 'smtp.139.com'
    send_mail(to,host,file_path)
