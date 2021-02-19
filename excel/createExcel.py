import xlwt

for i in range(5):
    des_file = '/Users/zhan/codes/learning-python/files/info' + str(i) + '.xlsx'
    workbook = xlwt.Workbook(encoding='utf-8')
    xlsheet = workbook.add_sheet('写入结果')
    xlsheet.write(0,0,'结果' + str(i))
    xlsheet.write(0,1,'data' + str(i))

    workbook.save(des_file)