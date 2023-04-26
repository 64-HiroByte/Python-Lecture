# 論理演算子(logical operators)
# and, or, not
a = 1
b = 1
c = 10
d = 100
print(a == b and c > d)
print(a == b or c > d)
print(not a == b)
print('*' * 80)

# challenge1:年齢が10歳以上かつ身長が110cm以上なら乗れるアトラクション
age = 11
height = 120
print(age >= 10 and height >= 110)

# challenge2:修士号保持もしくは5年以上実務経験があればVisaの取得が可能
master = True
experience = 3
print(master or experience >= 5)
