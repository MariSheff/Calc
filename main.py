from calc.operations import calculation
from calc.history import write_history
tpl = ('+', '-', '*', '/', '^')
print('Для завершения работы введите "exit"')
while True:
    s = input(f'Выберите операцию {tpl}:')

    if s == 'exit':
        break

    if s not in tpl:
        print('выберите операцию из списка!')
        continue

    a = float(input('a:'))
    b = float(input('b:'))
    res = calculation(s, a, b)
    write_history(s, a, b, res)
    print(res)
