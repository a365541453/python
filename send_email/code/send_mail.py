import sys
from def_file.mail_def import login_server
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
from email.mime.application import MIMEApplication

sys.path.append(r'F:\github\python\weekly_script\code')
from word import weekly_filename

#weekly_filename = 'C:\\Users\\Administrator\\Desktop\\周报20171120.docx'

server_ip = 'smtp.qq.com'
username = 'XXXXX'
password = 'XXXXX'
from_addr ='XXXX@qXX.XX'
to_addr = 'XXXX@qXX.XX'
#to_addr = '365541453@qq.com'

target_path = 'C:\\Users\\Administrator\\Desktop\\'
target_file = '周报2'

filename = weekly_filename

file = open(filename,'rb').read()

msg = MIMEMultipart()
msg['From'] = formataddr(['XXX',from_addr])
msg['To']  = formataddr(['XXX',to_addr])
msg['Subject'] = '周报'  #邮件的主题

enclosure = MIMEApplication(file)
enclosure.add_header('Content-Disposition','attchment',filename=('gbk','','周报.docx'))
msg.attach(enclosure)

body = MIMEText('这周的周报','plain','utf-8')
msg.attach(body)

server = login_server(server_ip,username,password)

server.sendmail(from_addr,to_addr,msg.as_string())

server.quit()

server.close()

