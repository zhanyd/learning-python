filename = 'guest.txt'
with open(filename, 'a', encoding="utf-8") as file:
    while True:
        print('please input your name...q to quit')
        name = input()
        if(name == 'q'):
            break
        file.write(name + '\n')