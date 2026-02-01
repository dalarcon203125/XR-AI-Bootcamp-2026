
#operator = input ('Enter operator: ')

while True:
    num1 = int(input('Enter a number: '))
    if num1 is int:
        print('Enter another number: ')    
        continue
    else:
        print('Enter only numbers')

    while True:
        num2 = int(input(''))
        if num2 is int:
            print('Enter an operator: ')
            continue
    else:
        print('Enter only numbers o valid operators')


#if operator == '*':
 #   result = num1 * num2
#elif operator == '+':
#    result = num1 + num2
#elif operator == '-':
#    result = num1 - num2
#elif operator == '/':
#    result = num1 / num2
#else:
#    print('Please enter only -, +, / or *')

#print(result)

