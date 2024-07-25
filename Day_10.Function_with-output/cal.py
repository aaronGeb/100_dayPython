#!/usr/bin/python3
from ast import literal_eval


def addition(*args):
    result = sum(args)
    return result


def multiplication(*args):
    result = 1
    for num in args:
        result *= num
    return result


def subtraction(*args):
    result = 0
    for num in args:
        result -= num
    return result


def division(a, b):
    if b == 0:
        raise Exception('Denominator can not be zero')
    return round(a/b, 2)


def main():
    print("Pick an operation? '+','-','*','/'")
    operations = {'+': addition, '-': subtraction,
                  '*': multiplication, '/': division}
    print('Choose an mathematical operation Operation below.')
    for symbol in operations:
        print(symbol)
    num1 = literal_eval(input('Enter the first number\n'))
    flag = False
    while not flag:
        num2 = literal_eval(input('Enter the next number\n'))
        operation_symbol = input('Enter the operation symbol\n')
        calculation_result = operations[operation_symbol]
        result = calculation_result(num1, num2)
        print(f'{num1}  {operation_symbol}  {num2}  = {result}')
        next_operation = input(
            'You like to continue operations? y on n\n').lower()
        if next_operation == 'y':
            num1 = result
        elif next_operation == 'n':
            flag = True
            main()
    print('Tanks see you later!!!')


main()
