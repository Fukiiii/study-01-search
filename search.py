### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース

source = ["ねずこ", "たんじろう", "きょうじゅろう", "ぎゆう", "げんや", "かなお", "ぜんいつ"]

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")

    ### ここに検索ロジックを書く
    print(word in source)
    if(word in source):
      print("当たり！{}のグッズをお渡しします！".format(word))
    else:
      print("残念！{}はハズレです！".format(word))



if __name__ == "__main__":
    search()