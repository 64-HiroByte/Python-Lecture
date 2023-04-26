# input()：ユーザの入力した値（文字列）を取得する

age = input('何歳ですか？')
print('あなたは{}歳です'.format(age))

# challenge1, 2
age = int(input('何歳ですか？'))
casino_age = 18
game_text = """プレイするゲームを選択してください
1： ルーレット
2： ブラックジャック
3：　ポーカー
"""

if age >= casino_age:
    print('どうぞ お入りください')
    game = input(game_text)
    if game == '1':
        print('あなたはルーレットを選びました')
    elif game == '2':
        print('あなたはブラックジャックを選びました')
    elif game == '3':
        print('あなたはポーカーを選びました')
    else:
        print('正しく入力してください')
else:
    print('18歳未満の方はカジノへ入場できません')
