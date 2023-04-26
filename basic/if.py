# if文

age = -20
age_alcohol = 21
if age >= age_alcohol:
    print('You can drink beer!')
else:
    print('You are too young to drink beer')

age_drive = 18
if age >= age_alcohol:
    print('You can drink beer!')
elif age < age_drive:
    print('You cannot even drive!')
else:
    print("You are not allowed to drink beer but you can drive only if you have a driver's license")

if not 0 < age < 120:
    print('The value is invalid!!')

# Challenge1: もし残高が引き出し額より大きければ引き出せないATM
balance = 10000000
withdraw = 1200000
if balance > withdraw:
    balance -= withdraw
    print(f'Your balance is {balance}')
else:
    print('You don\'t have money')

# Challenge2: Challenge1に加えて、引き出し額の上限が100万を超えると引き出せないATM
withdraw_limit = 1000000
if withdraw > withdraw_limit:
    print(f'withdraw limit is {withdraw_limit}')
elif balance > withdraw:
    balance -= withdraw
    print(f'Your balance is {balance}')
else:
    print('You don\'t have money')