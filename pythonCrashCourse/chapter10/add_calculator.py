print('please input two numbers to add')
print('inpt q for quit')



while True:
    try:
        first_number = input('first number: ')
        if first_number == 'q':
            break
        second_number = input('second number: ')
        if second_number == 'q':
            break
        sum = int(first_number) + int(second_number)
    except ValueError: 
        print('please input two numbers')
    else:
        print(first_number, '+', second_number, '=', sum)