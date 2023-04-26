# tuple(タプル): 変更できないリスト、[]ではなく()を使う

date_of_birth = (1974, 10, 1)
print(date_of_birth)
print(date_of_birth[0])

# 次のように変更しようとするとエラーになる
# date_of_birth[0] = 1998

# unpack
year, month, date = date_of_birth
print(year)
print(month)
print(date)
