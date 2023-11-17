filename = 'G:/codes/python/Python编程：从入门到实践源代码文件/源代码文件/chapter_10/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input('Enter you birthady, in the format yyyy/mm/dd:')
if birthday in pi_string:
    print('Your birthday is in the first million digits of pi!')
else:
    print('Your birthday is not in the first million digits of pi!')
