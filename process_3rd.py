import xlwings as xw
import time
import datetime

Setting_3rd_Root:str = None
Temp_Root:str = None
Config_Filepath = r'D:\harrisonworkspace\做账\第三方数据汇总\第三方数据处理模板\第三方数据处理模板.xlsx'
StoreNameMapping = {}

class SourceFile:

    #名称
    SourceName:str = None

    #文件子目录
    SourceSubFolder:str = None

    #文件名列表
    SourceFileNameList = []

    #表名称
    SourceSheetName:str = None

    #表格首行行号
    StartingLineNO:int = 1

    #表格尾行留白
    EndingLineCnt:int = 0

    #门店所在列
    StoreColumn:str = 'E'

    #交易时间所在列
    TimeColumn:str = 'A'

    TimeFormat:str = ''

    #交易金额所在列
    MoneyColumn:str = 'G'

    #手续费所在列
    CommissionColumn:str = ''


SourceList = {}

#开始处理过程
config_app = xw.App(visible=True, add_book=False)

config_app.display_alerts=False

wb = config_app.books.open(Config_Filepath)

sht = wb.sheets['数据源表格']

print("打开配置文件%s "%Config_Filepath)

#在前10行的B列 寻找第三方表格根目录 和 Temp Root 配置项
for i in range(1, 11):
    rs = "B" + str(i)
    if sht.range(rs).value == '第三方表格根目录':
        Setting_3rd_Root = sht.range("C"+str(i)).value
    if sht.range(rs).value == '临时汇总文件位置':
        Temp_Root = sht.range("C"+str(i)).value

print("第三方表格根目录：" + Setting_3rd_Root)
print("临时存储目录: " + Temp_Root)

#开始按照序号寻找每个配置项
Source_Starting_Line = 7
for i in range(6,20):
    rs = rs = "B" + str(i)
    if sht.range(rs).value == '数据表序号':
        Source_Starting_Line = i+1

print("从第[%d]行开始读取第三方配置数据"%Source_Starting_Line)

rown = Source_Starting_Line

while sht.range('B' + str(rown)).value != None:
    cell_value = sht.range('B' + str(rown)).value
    cell_value2 = sht.range('C' + str(rown)).value
    print("第%d行:配置项序号：%d, 配置项: %s"%(rown,cell_value,cell_value2))

    sf = None

    if cell_value in SourceList:
        sf = SourceList[cell_value]
    else:
        sf = SourceFile()

    if cell_value2.strip() == '名称':
        sf.SourceName = sht.range('D' + str(rown)).value
        print(sf.SourceName)
    elif cell_value2.strip() == '文件子目录':
        sf.SourceSubFolder = sht.range('D' + str(rown)).value
        print(sf.SourceSubFolder)
    elif cell_value2.strip() == '文件名':
        sf.SourceFileNameList = sht.range('D' + str(rown)).value.split('\n')
        print(sf.SourceFileNameList)
    elif cell_value2.strip() == '表名称':
        sf.SourceSheetName = sht.range('D' + str(rown)).value
        print(sf.SourceSheetName)
    elif cell_value2.strip() == '门店所在列':
        sf.StoreColumn = sht.range('D' + str(rown)).value
        print(sf.StoreColumn)
    elif cell_value2.strip() == '交易时间所在列':
        sf.TimeColumn = sht.range('D' + str(rown)).value
        print(sf.TimeColumn)
    elif cell_value2.strip() == '交易金额所在列':
        sf.MoneyColumn = sht.range('D' + str(rown)).value
        print(sf.MoneyColumn)
    elif cell_value2.strip() == '手续费所在列':
        sf.CommissionColumn = sht.range('D' + str(rown)).value
        print(sf.CommissionColumn)
    elif cell_value2.strip() == '交易时间格式':
        sf.TimeFormat = sht.range('D' + str(rown)).value

    SourceList[cell_value] = sf
    rown += 1


#开始读取店名 mapping
sht2 = wb.sheets['【工具】门店名称转换']
rown = 3
while sht2.range('B' + str(rown)).value != None:
    StoreNameMapping[sht2.range('B' + str(rown)).value] = sht2.range('C' + str(rown)).value
    rown += 1

config_app.quit()

Temp_App = xw.App(visible=True, add_book=False)
Temp_App.display_alerts=False

Temp_wb = Temp_App.books.add()

#开始循环遍历第三方源 SourceList
for sf in SourceList.values():
    tmp_sht = Temp_wb.sheets.add(name=sf.SourceName)
    source_app = xw.App(visible=True, add_book=False)
    source_app.display_alerts = False
    tmp_sht.range('A1').value = r'交易日期'
    tmp_sht.range('B1').value = r'门店名称'
    tmp_sht.range('C1').value = r'交易金额'
    tmp_sht.range('D1').value = r'手续费'
    dst_cur_row=2

    print("开始处理第三方[%s]"%sf.SourceName)

    for fn in sf.SourceFileNameList:
        ff = None
        if sf.SourceSubFolder:
            ff = Setting_3rd_Root + '\\' + sf.SourceSubFolder + '\\' + fn
        else:
            ff = Setting_3rd_Root + '\\' + fn

        print("开始处理文件：%s"%ff)
        src_wb = source_app.books.open(ff)
        src_sht: xw.main.Sheet = None

        if sf.SourceSheetName:
            for ss in src_wb.sheets:
                if sf.SourceSheetName in ss.name:
                    src_sht = ss
                    break
        else:
            src_sht = src_wb.sheets[0]

        src_row = 2
        src_col = sf.TimeColumn
        while src_sht.range(src_col+str(src_row)).value != None:
            dt = src_sht.range(src_col + str(src_row)).value
            tt_string = None
            if isinstance(dt, datetime.datetime):
                tt_string = dt.strftime("%Y-%m-%d")
            else:
                sdate = time.strptime(dt,sf.TimeFormat)
                tt_string = time.strftime("%Y-%m-%d", sdate)

            tmp_sht.range('A' + str(dst_cur_row)+':C' + str(dst_cur_row)).value = \
                [tt_string,
                 StoreNameMapping[src_sht.range(sf.StoreColumn + str(src_row)).value],
                 src_sht.range(sf.MoneyColumn + str(src_row)).value]
            if sf.CommissionColumn:
                tmp_sht.range('D'+str(dst_cur_row)).value = src_sht.range(sf.CommissionColumn+str(src_row)).value
            src_row += 1
            dst_cur_row += 1
    source_app.quit()


Temp_wb.save(Temp_Root + r'\第三方汇总临时文件.xlsx')
Temp_App.quit()