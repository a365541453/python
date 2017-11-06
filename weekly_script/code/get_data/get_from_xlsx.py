import xlrd
from def_files.xlsx_def import *
import datetime




##############################从工作记录中获取工单#############################
xlsx_weekly = xlrd.open_workbook('C:\\Users\\Administrator\Desktop\\工作记录.xlsx')

end_time = datetime.datetime.now() + datetime.timedelta(days=-1)#结束的那一天
began_time = end_time + datetime.timedelta(days=-7)#开始的那一天

event = {}
for sheet in xlsx_weekly.sheets():#遍历xlsx中每一个sheet
	a = between_seven_event(sheet,began_time,end_time)
	#返回的是一周之内的工单dict
	event.update(a)



#########################从RVTool中获取存储信息###################################
target_path = 'C:\\Users\\Administrator\\Desktop\\'
target_filename = 'RVTools_export_all'

filename = find_filename(target_path,target_filename)

################################################################################
#xlsx_weekly = xlrd.open_workbook('C:\\Users\\Administrator\Desktop\\工作记录.xlsx')
#
#end_time = datetime.datetime.now() + datetime.timedelta(days=-1)#结束的那一天
#began_time = end_time + datetime.timedelta(days=-7)#开始的那一天
#
#event_time = {}
#for sheet in xlsx_weekly.sheets():#遍历xlsx中每一个sheet
#	a = between_seven_event(sheet,began_time,end_time)
#	#返回的是一周之内的工单dict
#	event_time.update(a)





############################################################
#excel = win32.gencache.EnsureDispatch('Excel.Application')# 因为RVTool导出来的xls格式
#filename = excel.Workbooks.Open(fname)                    # 需要转换成xlsx格式在进行操作
#filename.SaveAS(fname+"x", FileFormat = 51)               #
#filename.Close()                                          #
#excel.Application.Quit()                                  #
############################################################

xlsx_datastore = xlrd.open_workbook(filename)
datastore_sheet = xlsx_datastore.sheet_by_name('tabvDatastore')

datastore_tol = []
number = 1
for row_id in range(1,datastore_sheet.nrows):
	datastore_row = {}
	row = datastore_sheet.row(row_id)
	datastore_row['sn'] = str(number) #序号
	datastore_row['datastore_name'] = row[0].value #存储名
	if re.match(r'(datastore|LocalDisk)',row[0].value):#判断是什么存储
		type = '本地存储'
	else:
		type = '共享存储'
	datastore_row['datastore_type'] = type #存储类型
	datastore_row['problem_description'] = str(row[5].value/1024)+'GB'  #存储总量，单位GB
	if row[9].value < 20:   #判断空闲率是否低于20%
		state = '异常'
	else:
		state = '正常'
	datastore_row['problem_state'] = state #存储状态
	if (row[9].value > 20):  #判断是正常还是需要扩容处理
		result = '无需处理'
	else:
		result = '需要扩容/等待处理'

	if type == '本地存储':
		result = '本地存储无需处理'
	datastore_row['problem_result'] = result
	datastore_row['free'] = str(row[9].value)
	datastore_tol.append(datastore_row)
	number = number + 1
