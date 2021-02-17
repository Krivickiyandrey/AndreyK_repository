import math
print('1. Сумма, разность, произведение действительных чисел a и b')
print('2. Получить формулу (|Х|-|Y|)/(1+|XY|)')
print('3. Задать длинну ребра куба и вычислить его объем и площадь боковой поверхности')
print('4. Задать два просстых числа и вычислить среднее арифметическое и геаметрическое.')
print('5. Найти плозадь и гипотенузу прямоугольного треугольника по заданным катетам')
print('Выберите номеря действия:')
deistvie = input()
if deistvie == '1':
    print('Введите число a')
    a = int(input())
    print('Введите число b')
    b = int(input())
    print('Сумма=', a+b, 'Разность=', a-b, 'Произведение=', a*b)
elif deistvie == '2':
    print('Введите число x')
    x = float(input())
    print('Введите число y')
    y = float(input())
    ModulX = math.sqrt(x**2)
    ModulY = math.sqrt(y**2)
    Formula = (ModulX - ModulY) / (1 + ModulX*ModulY)
    print('Результат вычисления формулы  =', Formula)
elif deistvie == '3':
    print('Задайте длинну ребра куба:')
    dlinna_rebra = float(input())
    print('Объем куба = ', dlinna_rebra**3, 'Площадь боковых поверхностей = ', dlinna_rebra**2 * 6)
elif deistvie == '4':
    print('Задайте 2 простых числа')
    a = int(input())
    b = int(input())
    print('Среднее арифметическое = ', (a+b)/2, 'Среднее геометрическое = ', math.sqrt(a*b))
elif deistvie == '5':
    print('Введите длинны катетов прямоугольника')
    a = float(input())
    b = float(input())
    print('Площадь = ', (a*b)/2, 'Гипотенуза = ', math.sqrt(a**2+b**2))
else:
    None
