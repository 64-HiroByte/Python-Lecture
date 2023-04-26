# challenge
age = int(input('何歳ですか？'))
casino_age = 18
game_dict = {
    '1': 'ルーレット',
    '2': 'ブラックジャック',
    '3': 'ポーカー'
}


if age >= casino_age:
    print('どうぞ お入りください')
    while True:
        print('プレイするゲームを選択してください')
        for num, game_name in game_dict.items():
            print(f'{num}: {game_name}')
        game = input(': ')

        if game in game_dict.keys():
            print(f'あなたは{game_dict[game]}を選びました')
            break
        else:
            first_key = list(game_dict.keys())[0]
            last_key = list(game_dict.keys())[-1]
            select_error_text = f'{first_key}〜{last_key}の中から選択してください\n'
            print(game_dict.get(game, select_error_text))
            continue
else:
    print(f'{casino_age}歳未満の方はカジノへ入場できません')
