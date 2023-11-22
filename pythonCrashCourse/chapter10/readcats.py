import os

# 获取当前脚本所在目录
current_dir = os.path.dirname(os.path.realpath(__file__))
print(current_dir)

catsFile = os.path.join(current_dir, 'cats.txt')
print(catsFile)
dagsFile = os.path.join(current_dir, 'dogs.txt')
print(dagsFile)

try:
    with open(catsFile, 'r', encoding="utf-8") as casfile:
        for line in casfile:
            print(line)
except FileNotFoundError:
    print(catsFile + "文件不存在")        

try:
    with open(dagsFile, 'r', encoding="utf-8") as dagsfile:
        for line in dagsfile:
            print(line)    
except FileNotFoundError:
    print(dagsFile + "文件不存在")                 