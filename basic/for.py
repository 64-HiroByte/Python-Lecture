# forループ
fruits = ['apple', 'peach', 'grapes', 'banana']

for fruit in fruits:
    print(f'I love {fruit}!!')

for char in 'hello world':
    print(f'char: {char}')

# challenge1
favorite = input('好きなフルーツは？')
for fruit in fruits:
    if fruit == favorite:
        print(f'I love {fruit}!!')
    else:
        print(f'I don\'t like {fruit}.')

# challenge2
like_list = []
hate_list = []
for fruit in fruits:
    answer = input(f'{fruit}は好きですか？ (y/n)')
    if answer == 'y':
        like_list.append(fruit)
    else:
        hate_list.append(fruit)
print(f'好きなフルーツ: {like_list}')
print(f'嫌いなフルーツ: {hate_list}')
