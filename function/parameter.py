def func(first, second, third):
    print(f'first: {first}, second: {second}, third: {third}')


# argument
func('1', '2', '3')

func('1', third='3', second='2')


def func2(first, second, third='3'):
    print(f'first: {first}, second: {second}, third: {third}')


func2('1', '2')
func2('1', '2', '33')
