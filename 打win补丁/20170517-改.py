# -*- coding:utf-8 -*-

import telnetlib
import time
import re
import xlrd


def get_os_systeminfo(host_ip,host_username,host_passwd):
	host_telnet = telnetlib.Telnet(host_ip,23)
	host_telnet.set_debuglevel(2)  

	time.sleep(5)

	host_telnet.read_until(b'login',10)
	host_telnet.write(host_username + b'\r')
	host_telnet.read_until(b'password',10)
	host_telnet.write(host_passwd + b'\r')

	host_telnet.read_until(b'>')
	host_telnet.write(b'systeminfo\r\n')

	time.sleep(80)   #一定要60s，不然返回信息不全
	systeminfo = host_telnet.read_very_eager()

	host_telnet.close()

	systeminfo = systeminfo.split(b'\r\n')

	while b'' in systeminfo:
		systeminfo.remove(b'')
	os_n = 'OS 名称'.encode('gbk')
	os_x = '系统类型'.encode('gbk')

	for row in systeminfo:
		
		os_name = re.findall(b'^%s.*'%os_n,row)
		if os_name != []:
			system_name = os_name[0].decode('gbk')

		os_type = re.findall(b'^%s.*'%os_x,row)
		if os_type != []:
			system_type = os_type[0].decode('gbk')
	return system_name,system_type

def get_os_version_type(os_info_version,os_info_type):
	if os_info_version.find('2003') != -1:
		os_version = '2003'
	elif os_info_version.find('2008') != -1:
		os_version = '2008'	
	elif os_info_version.find('R2') != -1:
		os_version = '2008R2'
	elif os_info_version.find('r2') != -1:
		os_version = '2008R2'
	
	if os_info_type.find('64') != -1:
		os_type = '64'
	elif os_info_type.find('86') != -1:
		os_type = '32'
	elif os_info_type.find('32') != -1:
		os_type = '32'

	if (os_version == '2003') and (os_type == '32'):
		patch_pwd = 'Win2003'
		patch_file = 'windowsserver2003-kb4012598-x86-custom-chs.exe'
	elif (os_version == '2003') and (os_type == '64'):
		patch_pwd = 'Win2003'
		patch_file = 'windowsserver2003-kb4012598-x64-custom-chs.exe'
	elif (os_version == '2008') and (os_type == '32'):
		patch_pwd = 'Win2008'
		patch_file = 'windows6.0-kb4012598-x86.msu'
	elif (os_version == '2008') and (os_type == '64'):
		patch_pwd = 'Win2008'
		patch_file = 'windows6.0-kb4012598-x64.msu'
	elif (os_version == '2008R2') and (os_type == '64'):
		patch_pwd = 'Win7'
		patch_file = 'windows6.1-kb4012212-x64.msu'

	return patch_pwd,patch_file

def download_run_patch(host_ip,host_username,host_passwd,patch_pwd,patch_file):

	host_telnet = telnetlib.Telnet(host_ip,23)
	host_telnet.set_debuglevel(2)  

	time.sleep(5)

	host_telnet.read_until(b'login',10)
	host_telnet.write(host_username + b'\r')
	host_telnet.read_until(b'password',10)
	host_telnet.write(host_passwd + b'\r')

	host_telnet.read_until(b'>')
	host_telnet.write(b'ftp\r')

	host_telnet.read_until(b'>')
	host_telnet.write(b'open 10.41.0.109\r')

	host_telnet.read_until(b'220')
	host_telnet.write(b'administrator\r')

	host_telnet.read_until(b'assword')
	host_telnet.write(b'qazWSX123\r')

	host_telnet.read_until(b'>')
	host_telnet.write(b'prompt\r')

	host_telnet.read_until(b'>',10)
	host_telnet.write(b'lcd c:\\\r')
	
	host_telnet.read_until(b'>',10)
	host_telnet.write(b'cd %s\r'%patch_pwd)

	host_telnet.read_until(b'>',10)
	host_telnet.write(b'mget %s\r'%patch_file)
	
	host_telnet.read_until(b'>',10)
	host_telnet.write(b'bye\r')	

	host_telnet.read_until(b'>',10)
	host_telnet.write(b'c:\\' + patch_file +b' /u \r' )
	host_telnet.read_all()

	host_telnet.close()

workbook = xlrd.open_workbook('.//host_info.xlsx')
sheet = workbook.sheet_by_index(0)

for row in range(1,sheet.nrows):
	host_ip = sheet.cell_value(row,5)
	host_username = sheet.cell_value(row,6).encode('gbk')
	host_passwd = sheet.cell_value(row,7).encode('gbk')

	os_info = get_os_systeminfo(host_ip,host_username,host_passwd)
	os_info_version = os_info[0]
	os_info_type = os_info[1]

	patch_pwd = get_os_version_type(os_info_version,os_info_type)[0].encode('gbk')
	patch_file = get_os_version_type(os_info_version,os_info_type)[1].encode('gbk')

	download_run_patch(host_ip,host_username,host_passwd,patch_pwd,patch_file)


















