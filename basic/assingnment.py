# 変数へ代入： assignment

hello = 'Hello'
world = 'World!!'

print(hello + world)
"""
一度つけた変数名を変更するときには、
変数を右クリックして”リファクタリング ＞ 名前の変更”
をやると対象の変数名を一度に変更できるので便利
"""

# format
print('*'*30, ' .format ', '*'*30)

'hello {}'.format('world')
print('{} {}'.format(hello, world))

name = 'john'
print('Hey, {}!! How are you doing?'.format(name))

balance = 100
print('balance: {}'.format(balance))

# fstring <-- 内部的には.formatより処理が早いが、Python 3.6以降で使用可能
print('*'*30, ' fstring ', '*'*30)
print(f'{hello} {world}')
print(f'Hey, {name}!! How are you doing?')
print(f'balance: {balance}')
