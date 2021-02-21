import xlwt

# 循环5次
for i in range(5):
    des_file = 'E:/python/learning-python/files/info' + str(i) + '.xls'
    workbook = xlwt.Workbook(encoding='utf-8')
    xlsheet = workbook.add_sheet('写入结果')
    # 第一个0表示第0行，第二个0表示第0列
    xlsheet.write(0,0,'结果' + str(i))
    xlsheet.write(0,1,'data' + str(i))

    workbook.save(des_file)