#!/usr/bin/env python
 
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

class SendMail(object):
    
    # mail_host = "smtp.xxx.com"
    # sender = "123@qq.com"
    # mail_pass = "xxxx" 
    # subject = 'Ezblock Message'
    def __init__(self, mail_host, sender, mail_pass): 
        self.mail_host = mail_host      # 邮箱的服务器名字
        self.sender = sender            # 发送者邮箱
        self.mail_pass = mail_pass      # 发送者邮箱的生成授码权（口令）（打开SMTP服务）

    def send(self, receivers, msg, subject):
        # receivers： 收件人邮箱
        # msg: 邮件内容
        # subject： 邮件主题
        print("sender:", self.sender)
        message = MIMEText(msg, 'plain', 'utf-8')               # 创建消息对象， utf-8：表示支持多种语言
        message['From']=formataddr([self.sender, self.sender])  # sender name
        try:
            message['To']=formataddr([receivers,receivers]) 
            message['Subject']= subject   # Email subject
        
            smtpObj = smtplib.SMTP()            # 开始SMTP服务
            smtpObj.connect(self.mail_host, 25) # 连接远程smtp服务器，25为服务器端口号
            smtpObj.login(self.sender, self.mail_pass)  # 登陆
            smtpObj.sendmail(self.sender, receivers, message.as_string()) # 发送邮件信息
            print("Email sent successfully")
        except smtplib.SMTPException:
            print("Error: Email sending failed")


def test():
    send11 = SendMail("smtp.qq.com", "1171587873@qq.com", "nfsjbvkolswkhddg")
    send11.send('826437286@qq.com', "who send email?", "Ezblock Message")

if __name__ == "__main__":
    test()
