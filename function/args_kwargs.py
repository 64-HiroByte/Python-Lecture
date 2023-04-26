# *args: 不特定多数の引数を渡すことができる
# print('hello', 'world', 'test')
def get_args(*args):
    # *をつけると一つずつ出力される
    print(*args)
    # *がなければ引数をタプル型で扱う
    print(args)


get_args(1, 2, 3, 4, 5)


def get_average(*args):
    num = len(args)
    if num == 0:
        return 0
    total = sum(args)
    return total / num


average = get_average(1, 2, 3, 4, 5, 6, 7, 8)
print(average)

# **kwargs: *argsの辞書型バージョン
def kwargs_func(**kwargs):
    print(kwargs)


kwargs_func(param1=10, param2=6, param3=100)


def kwargs_func2(**kwargs):
    param1 = kwargs.get('param1', 1)
    param2 = kwargs.get('param2', 2)
    param3 = kwargs.get('param3', 3)

    print(f'param1: {param1}, param2: {param2}, param3: {param3}')


kwargs_func2()
kwargs_func2(param1=10, param2=20)
kwargs_func2(param1=10, param2=20, param3=30, param4=40)

# *と**はunpacking operator（アンパッキング演算子）と呼ばれる
numbers = (1, 2, 3)
print(*numbers)     # *をつけて関数に渡すとアンパックした状態で実行される
print(1, 2, 3)

a = {'a': 1, 'b': 2}
b = {'c': 3, 'd': 4}
c = {**a, **b}      # **も同様にアンパックされて実行される
print(c)
