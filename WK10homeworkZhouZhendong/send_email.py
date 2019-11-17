import smtplib
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr

sender = '785989657@qq.com'
sender_pwd = 'MyPasswordCode'
receiver = 'zhang.zhizhen@qq.com'
cc_receiver = '201711010185@mail.bnu.edu.cn'

subject = '周振东-201711010185'
main_text = '''
尊敬的张老师：
    您好！
    这是我在学习计算机网络编程的电子邮件部分时整理的相关名词解释，请您查收！
                                                                                                        周振东
                                                                                        2019年11月15日
'''

message = MIMEMultipart()
message['From'] = formataddr(["周振东", sender])
message['To'] = formataddr(["张老师", receiver])
message['Cc'] = formataddr(["周振东的师大邮箱", cc_receiver])
message['Subject'] = Header(subject, 'utf-8')
message.attach(MIMEText(main_text, 'plain', 'utf-8'))

att = MIMEApplication(open("周振东-名词解释.pdf", 'rb').read())
att.add_header('Content-Disposition', 'attachment', filename="周振东-名词解释.pdf")
message.attach(att)

try:
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.login(sender, sender_pwd)
    s.sendmail(sender, [receiver, cc_receiver], message.as_string())
    print("发送成功")
except s.SMTPException as e:
    print("发送失败")
finally:
    s.quit()