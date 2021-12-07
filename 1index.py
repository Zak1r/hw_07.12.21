#task 2

signs = {
    'add': '+',
    'substract': '-'}
def calc(a, b, action):
    return eval(f'{a} {signs.get(action)} {b}')
print(calc(5, 2, 'add'))
print(calc(5, 2, 'substract'))