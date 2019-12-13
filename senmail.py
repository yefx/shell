import smtplib
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header

def send_mail(receiver, fpath, fname):
    host = 'smtp.qq.com'
    password = 'xxxxxxxx'
    sender = 'yefuxiong@vip.qq.com'
    #邮件的正文内容
    mail_content = "你好，<p>这是使用python发送html格式的邮件测试2：</p><p><a href='https://www.baidu.com'>Baidu</a></p>"
    #邮件标题
    mail_title = 'Python邮件自动化'
    msg = MIMEMultipart()
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender
    msg["To"] = Header("测试邮件", 'utf-8')
    msg.attach(MIMEText(mail_content, 'html', 'utf-8'))
    #添加附件
    attachment = MIMEApplication(open(fpath, 'rb').read())
    attachment.add_header('Content-Disposition', 'attachment', filename=fname)
    msg.attach(attachment)

    try:
        smtp = SMTP_SSL(host)
        smtp.set_debuglevel(0)
        smtp.ehlo(host)
        smtp.login(sender,password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("无法发送邮件")

def main():
    receiver = 'yefuxiong@139.com' #收件人
    fpath = './xiaohuangya.xlsx' #文件路径
    fname = 'xiaohuangya.xlsx' #发送时文件重命名
    send_mail(receiver, fpath, fname)
if __name__ == '__main__':
    main()
