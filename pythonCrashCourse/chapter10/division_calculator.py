print("Give me two numbers, and I'll divide them")
print("Type 'q' to quit\n")

while True:
    first_number = input("First_number:")
    if first_number == 'q':
        break
    second_number = input("Second_number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('You can not divide by zero')
    else:   
        print(first_number, "/", second_number, "=", answer)