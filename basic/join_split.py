# join
text = ' '.join(['Hi', 'My', 'name', 'is', 'John'])
print(text)
text2 = '-'.join(['Hi', 'My', 'name', 'is', 'John'])
print(text2)

# split
print('Hi My name is John'.split(' '))

# splitの使用例（ファイル名から拡張子を除く）
filename = 'sample.py'
print(filename.split('.')[0])
