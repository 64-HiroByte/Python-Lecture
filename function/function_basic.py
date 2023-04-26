# 関数（function）

# 華氏から摂氏に変換する
fahrenheit = 72
celsius = (fahrenheit - 32) * 5/9
print(celsius)


# 関数の定義と使用方法
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


fahrenheit = 72
celsius = fahrenheit_to_celsius(fahrenheit)
print(celsius)
