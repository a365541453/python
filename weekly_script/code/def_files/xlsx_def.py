import time
import xlrd
import os
import re

def between_seven_event(sheet, began_time, end_time):
    began_time_stamp = began_time.timestamp()
    end_time_stamp = end_time.timestamp()

    event_dict = {}
    for x in range(0, sheet.nrows):
        time_numerical = sheet.cell_value(x, 0)
        cell_time = xlrd.xldate.xldate_as_datetime(time_numerical, 0).timestamp()
        # 返回的是date.datetime类型的时间戳
        if (began_time_stamp < cell_time) and (cell_time < end_time_stamp):
            key = time.localtime(cell_time)  # 这一个工单的时间戳转换为标准时间
            key_time = '%s年%s月%s日' % (key.tm_year, key.tm_mon, key.tm_mday)  # 工单的时间
            event_value = [sheet.cell_value(x, 1), sheet.cell_value(x, 3)]  # 工单的工作内容
            event_dict[key_time] = event_value  # 将工单时间和内容写进字典
    return event_dict


def find_filename(target_path, target_filename):
    path = os.walk(target_path)  # 寻找目标路径下的所有文件及文件夹
    for folder in path:
        if folder[0] == target_path:  # 寻找到桌面这个文件夹,为tuple类型
            for x in range(0, len(folder)):
                if (str(type(folder[x])) == "<class 'list'>") and (len(folder[x]) > 1):  #将桌面文件的list筛选出来
                    for name in folder[x]:
                        if re.match('^(%s)'%target_filename, name):
                            filename = name
                            filename_path = target_path + filename
                            return filename_path



