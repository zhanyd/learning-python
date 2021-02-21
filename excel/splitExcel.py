import xlrd
import xlwt

# 写入Excel文件
def writeToExcel(username, content):
	dest_file = 'E:/python/learning-python/files/split_' + username + '.xls'
	workbook = xlwt.Workbook(encoding='utf-8')
	xlsheet = workbook.add_sheet('拆分结果')

	# 标题
	table_header = ['日期','姓名','星期','上班考勤','上班考勤类型','上班考勤地点','上班考勤状态','下班考勤','下班考勤类型','下班考勤地点','下班考勤状态']
	# 写入标题
	row = 0
	col = 0
	for cell_header in table_header:
		xlsheet.write(row, col, cell_header)
		col += 1
	row += 1
	# 写入内容
	# print(content)
	for line in content:
		col = 0
		print(line)
		for cell in line:
			print(cell)
			xlsheet.write(row, col, str(cell))
			col += 1
		row += 1
	workbook.save(dest_file)



# 要拆分的excel文件
src_file = 'E:/python/learning-python/files/考勤列表.xlsx'

# 读取excel
book = xlrd.open_workbook(src_file)
print("The number of worksheets is {0}".format(book.nsheets))
print("Worksheet name(s): {0}".format(book.sheet_names()))
sh = book.sheet_by_index(0)
print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))

content = []
# 上一个用户的名字
lastUserName = sh.cell_value(rowx=1, colx=1)
for rx in range(sh.nrows):
	# 跳过第一行标题
	if(rx == 0):
		continue
	# 读取用户的名字
	username = sh.cell_value(rowx=rx, colx=1)
	# 一个用户的数据读取完之后，写入一个新的excel文件中
	if(lastUserName != username):
		# 写入Excel文件
		writeToExcel(lastUserName, content)
		lastUserName = username
		content = []
	# 每一行的数据存在一个数组里
	content.append([sh.cell_value(rowx=rx, colx=0),sh.cell_value(rowx=rx, colx=1),sh.cell_value(rowx=rx, colx=2),sh.cell_value(rowx=rx, colx=3),sh.cell_value(rowx=rx, colx=4),sh.cell_value(rowx=rx, colx=5),sh.cell_value(rowx=rx, colx=6),sh.cell_value(rowx=rx, colx=7),sh.cell_value(rowx=rx, colx=8),sh.cell_value(rowx=rx, colx=9),sh.cell_value(rowx=rx, colx=10)])
	#print(sh.row(rx))




