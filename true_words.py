import requests
from bs4 import BeautifulSoup

def word_exists(word):
    # ウェブ上の辞書サイトなどから単語を検索するためのURLを構築
    url = f"https://sakura-paris.org/dict/%E5%BA%83%E8%BE%9E%E8%8B%91/prefix/{word}"  # 実際の辞書サイトのURLに置き換えてください

    # サイトからデータを取得
    response = requests.get(url)

    # HTTPステータスコードが200（成功）であれば、ページ内容を解析
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # 検索結果が存在しないことを示す特定のテキストを検索
        not_found_text = "検索結果は見つかりません"
        if not_found_text in soup.get_text():
            return False  # 検索結果が存在しない場合
        else:
            return True   # 単語が存在する場合
    else:
        return False  # HTTPステータスコードが200以外の場合も単語が存在しないとみなします

# ユーザーから単語を入力
user_input = input("単語を入力してください: ")

# 単語の存在を確認
if word_exists(user_input):
    print(f"{user_input} は存在します。")
else:
    print(f"{user_input} は存在しません。")
