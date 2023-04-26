# in演算子（あるオブジェクトが指定したオブジェクトに含まれているかをTrueかFalseで返す）
fruits = ['apple', 'peach', 'grapes', 'banana']
print('apple' in fruits)
print('lemon' in fruits)
print('lemon' not in fruits)
print('h' in 'hello')

# challenge
text = 'あなたの好きなフルーツを入力してください: '

favorite_fruit = input(text)

if favorite_fruit in fruits:
    fruits.remove(favorite_fruit)
    print(f'{favorite_fruit}が好きなのですね！ どうぞお召し上がりください')
else:
    fruits.append(favorite_fruit)
    print(f'あいにく{favorite_fruit}の在庫がありませんので、すぐに仕入れてきます')
print(f'現在の在庫リスト； {fruits}')
