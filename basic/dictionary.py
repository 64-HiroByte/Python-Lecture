# dictionary: キーと値の組み合わせを複数保持するデータ型
fruits_colors = {'apple': 'red', 'lemon': 'yellow', 'grapes': 'purple'}
print(fruits_colors['apple'])
fruits_colors['peach'] = 'pink'
print(fruits_colors)
dict_sample = {1: 'one', 'two': 2, 'three': [1, 2, 3], 'four': {'inner': 'dict'}}
print(dict_sample)
print(dict_sample['four']['inner'])

# 辞書型は本来、順番を保持しないとされてきたが、Python3.7から順番を保持するようになった！
colors = {}
colors[1] = 'blue'
colors[0] = 'red'
colors[2] = 'green'
print(colors)

# .keys()と .values()
for fruit in fruits_colors.keys():
    print(fruit)
for fruit in fruits_colors.values():
    print(fruit)
for x in fruits_colors:
    print(x)

# .items()
for fruit, color in fruits_colors.items():
    print(f'{fruit} is {color}')
