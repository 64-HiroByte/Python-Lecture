# mutable: 変更可能なオブジェクト　list, dict, set
fruits = ['apple', 'peach', 'banana']
print(f'fruitsのIDは{id(fruits)}')
fruits.append('lemon')
print(f'fruitsのIDは{id(fruits)}')

# immutable: 変更不可能なオブジェクト　int, float, str, bool, tuple
fruit = 'apple'
print(f'fruitのIDは{id(fruit)}')
fruit += ', lemon'
print(fruit)
print(f'fruitのIDは{id(fruit)}')

# この方法は非効率（文字列はイミュータブルなオブジェクトなので実はメモリを無駄遣いしている）
text = ''
for i in range(1, 11):
    if i == 1:
        text += str(i)
    else:
        text += '-' + str(i)
print(text)

# 効率的な方法（ミュータブルオブジェクトのリストを使用）
text_list = [str(i) for i in range(1, 11)]
text = '-'.join(text_list)
print(text)
