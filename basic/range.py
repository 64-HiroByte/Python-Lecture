# range(start, stop, step)

# for i in range(1, 7):
#     print(i)
# print('-' * 80)
#
# for i in range(7):
#     print(i)
# print('-' * 80)
#
# for i in range(2, 14, 2):
#     print(i)
# print('-' * 80)
#
# for _ in range(4):
#     print('hello')
# print('-' * 80)

# challenge FizzBuzzゲーム
for i in range(1, 51):
    if i % 15 == 0:
        print(i, ': FizzBuzz')
    elif i % 3 == 0:
        print(i, ': Fizz')
    elif i % 5 == 0:
        print(i, ': Buzz')
    else:
        print(i)
