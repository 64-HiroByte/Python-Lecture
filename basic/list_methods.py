fruits = ['apple', 'peach', 'melon', 'grapes']

hetro_list = ['string', 1, 3.4, True, fruits]


# .append: 新しいオブジェクトを末尾に追加する
print(fruits)
fruits.append('banana')
print(fruits)

# .insert: 指定したindexに指定したオブジェクトを追加する
fruits.insert(3, 'lemon')
print(fruits)

# .remove: マッチした最初のオブジェクトを除く
fruits.remove('peach')
print(fruits)

# .sort: 昇順に並び替える
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)

# len(): リストの要素数を取得する
print(len(fruits))
print(len('hello world'))
