# coding:utf8
import sys,os
import xlwt
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

def read_mysql_to_excel(file_path, sql):
    conn = get_conn_mysql()
    cursor = conn.cursor()
    count = cursor.execute(sql)
    if count != 0:
        print('查询结果：%s' %(count))
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
    if os.path.isfile(file_path):
        sender = 'yefuxiong@139.com'
        user = 'yefuxiong@139.com'
        password = 'xxxxxxxxx'
        subject = '导出数据'
        content = '您所需要的数据导出，请见附件。'
        with open(file_path, 'rb') as f:
            txt = MIMEText(f.read(), 'plain', 'gbk')
            txt['Content-Type'] = 'application/octet-stream'
            txt['Content-Disposition'] = "attachment;filename=%s" % (file_path)
        email = MIMEMultipart()
        email.attach(MIMEText(content, 'plain', 'utf-8'))
        email.attach(txt)
        email['Subject'] = subject
        email['From'] = sender
        email['To'] = ",".join(to)
        msg = email.as_string()
        smtpObj = smtplib.SMTP_SSL(host, 465)
        try:
            smtpObj.ehlo()
            smtpObj.login(user, password)
            smtpObj.sendmail(sender, to, msg)
            smtpObj.quit()
            os.remove(file_path)
            print('邮件发送成功\n%s已删除' %(file_path))

        except 
            print('Error:邮件发送失败！！！')

    else:
        print("发送文件不存在！！！")
        print('Error:邮件发送失败！！！')

if __name__ == '__main__':
    sql = 
    """
    这里是sql语句
    """
    file_path = sys.argv[1]
    read_mysql_to_excel(file_path, sql)
    to = ['%s'%(sys.argv[2]),'yefuxiong@vip.qq.com']
    host = 'smtp.139.com'
    send_mail(to,host,file_path)
