### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース

import csv

source = ["ねずこ", "たんじろう", "きょうじゅろう", "ぎゆう", "げんや", "かなお", "ぜんいつ"]

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")

    ### ここに検索ロジックを書く
    print(word in source)
    if(word in source):
      print("当たり！{}のグッズをお渡しします！".format(word))
    else:
      print("残念！{}はハズレです。でも次回以降にグッズを用意しておきます！".format(word))
      source.append(word)

    with open("source.csv", "w", encoding="Shift_jis") as f: # 文字コードをShift_JISに指定
      writer = csv.writer(f) # writerオブジェクトの作成 改行記号で行を区切る
      writer.writerows(source) # csvファイルに書き込み

if __name__ == "__main__":
    search()
