import xlrd
import xlwt
from pathlib import Path, PurePath

# 文件所在的目录
src_path = '/Users/zhan/codes/learning-python/files'
# 合并后的文件
dest_file = '/Users/zhan/codes/learning-python/files/merge.xlsx'

# 获取所有文件
path = Path(src_path)
files = [x for x in path.iterdir() if PurePath(x).match('*.xlsx')]

content = []

for file in files:
    username = file.stem
    data = xlrd.open_workbook(file)
    table = data.sheets()[0]
    result1 = table.cell_value(0,0)
    result2 = table.cell_value(0,1)
    temp = f'{username},{result1},{result2}'
    content.append(temp.split(','))
    print('temp = ' + temp)

# 标题
table_header = ['文件名','第一项','第二项']

workbook = xlwt.Workbook(encoding='utf-8')
xlsheet = workbook.add_sheet('统计结果')

# 写入表头
row = 0
col = 0
for cell_header in table_header:
    xlsheet.write(row, col, cell_header)
    col += 1

row += 1

print(content)
for line in content:
    col = 0
    print(line)
    for cell in line:
        xlsheet.write(row, col, cell)
        col += 1
    
    row += 1

workbook.save(dest_file)

