import smtplib
import os
import re


def login_server(server_ip, username, password):
	server = smtplib.SMTP_SSL()
	server.set_debuglevel(1)
	server.connect(server_ip)
	server.login(username, password)
	return server


def find_filename(target_path, target_filename):
	path = os.walk(target_path)  # 寻找目标路径下的所有文件及文件夹
	for folder in path:
		if folder[0] == target_path:  # 寻找到桌面这个文件夹,为tuple类型
			for x in range(0, len(folder)):
				if (str(type(folder[x])) == "<class 'list'>") and (len(folder[x]) > 1):  # 将桌面文件的list筛选出来
					for name in folder[x]:
						if re.match('^(%s)' % target_filename, name):
							filename = name
							filename_path = target_path + filename
							return filename_path
