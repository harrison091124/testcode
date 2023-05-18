import os

import xlrd
import xlwt

wbk = xlwt.Workbook(encoding="utf-8")  # 创建 xls 文件,可被复写
data_sheet = wbk.add_sheet("Sheet1")  # 创建一个名为sheet1的sheet

wbk_row = 0

g = os.walk(r'D:\harrisonworkspace\做账\第三方数据汇总\202103数据\3月第三方平台原始数据\银联\3月银联数据2  20210402162707')
init = 0
for path, dir_list, file_list in g:
    for file_name in file_list:
        full_path = os.path.join(path, file_name)
        print("处理: " + full_path)
        xls_file_path = full_path
        xls_fd = xlrd.open_workbook(xls_file_path)
        table = xls_fd.sheets()[0]

        start_idx = 3

        # 对于首个文件，需要将 start_idx 设置为2
        if init == 0:
            init = 1
            start_idx = 2

        for i in range(start_idx, table.nrows - 1):
            current_row = table.row_values(i)
            print(current_row)
            for j in range(len(current_row)):
                data_sheet.write(wbk_row, j, str(current_row[j]))
            wbk_row += 1

wbk.save(r"D:\harrisonworkspace\做账\第三方数据汇总\202103数据\3月第三方平台原始数据\银联2.xls")  # 保存
