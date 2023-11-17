filename = 'g:/codes/python/learning-python/pythonCrashCourse/chapter10/config.txt'

with open(filename, encoding="utf-8") as file_oject:
    for line in file_oject:
        print(line.rstrip())