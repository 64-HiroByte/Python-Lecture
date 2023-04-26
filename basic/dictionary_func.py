fruits_color = {'apple': 'red', 'lemon': 'yellow', 'grapes': 'purple'}

# キーが存在しないのでエラーになる書き方
# print(fruits_color['peach'])

# キーの存在をif文で確認（非スマート）
if 'peach' in fruits_color:
    print(fruits_color['peach'])
else:
    print('the key is not found')

# .get():スマートな方法
print(fruits_color.get('peach', 'Nothing'))
# ex
fruit = input('フルーツの名前を指定してください')
print(fruits_color.get(fruit, 'Nothing'))

# .update(): 辞書同士の結合
fruits_color2 = {'peach': 'pink', 'kiwi': 'green'}
fruits_color.update(fruits_color2)
print(fruits_color)
