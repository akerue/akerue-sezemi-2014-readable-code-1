# CookPad リーダブルコード勉強会用のリポジトリ

みんなでリーダブルコードを書けるように勉強しようの会

##開発言語

Python (2.7.5)

## プログラム仕様

# recipe.py

以下のように実行することでプログラムを実行できます
> python recipe.py [ディレクトリ] [ユーザ名] [レシピID]

レシピ全てを表示する例
> python recipe.py recipe-data/ kou

レシピIDを指定する例
> python recipe.py recipe-data/ kou 1

Python 2.Xのプログラムです．"python -V"と実行してversionが3.Xの場合は実行できないことがあります ．

# レシピデータ

**レシピファイルのファイル名をユーザ名として扱う**

|ファイル名|ユーザ名|
|:---------|:-------|
|kou.txt|kou|

レシピには改行区切りで複数のレシピを登録することが可能
また、スペース区切りでcookpadのURLを指定できます。

レシピデータ例:
```
オムライス http://cookpad.com/recipe/2653946
```
