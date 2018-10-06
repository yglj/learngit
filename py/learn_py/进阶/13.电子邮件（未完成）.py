#传统邮件的运输过程
#用邮件软件写好电子邮件 MUA（mail user agent）-邮件用户代理
#发到MTA，传输邮件 mail transfer agent-邮件传输代理（email服务提供商）
#最终到达MDA mail delivery agent -邮件投递代理，存储到文件或数据库（电子邮箱）

#发件人 -> MUA -> MTA -> MTA -> 若干个MTA -> MDA <- MUA <- 收件人
'''
本质上就是：

编写MUA把邮件发到MTA；

编写MUA从MDA上收邮件。

发邮件时，MUA和MTA使用的协议就是SMTP

收邮件时，MUA和MDA使用的协议有两种：POP：Post Office Protocol，目前版本是3，俗称POP3；IMAP：Internet Message Access Protocol，目前版本是4，优点是不但能取邮件，还可以直接操作MDA上存储的邮件，比如从收件箱移到垃圾箱，等等。

'''
from email.mime.text import MIMEText  #email负责构造邮件，smtplib负责发送邮件
import smtplib

msg = MIMEText('this is my first email...','plain','utf-8') #plain表示纯文本
'''
from_addr = input('Email地址：')
passwd = input('密码：')
to_addr = input('输入收件人地址：')
smtp_server = input('输入smtp服务器地址：')
'''

server = smtplib.SMTP(smtp_server,25) #SMTP协议默认端口25
server.set_debuglevel(1)
server.login(from_addr,passwd) #登录STMP服务器
server.sendmail(from_addr,[to_addr],msg.as_string())
#[] 一次可以传给多人，as_string()把mime对象变为字符串
server.quit()
