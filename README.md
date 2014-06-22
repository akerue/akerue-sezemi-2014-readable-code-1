# CookPad リーダブルコード勉強会用のリポジトリ

みんなでリーダブルコードを書けるように勉強しようの会

##開発言語

Python (2.7.5)

## プログラム仕様

# recipe.py

以下のように実行することでプログラムを実行できます

レシピ全てを表示する場合
> python recipe.py data/recipe-data.txt

レシピIDを指定する場合
> python recipe.py data/recipe-data.txt 1

Python 2.Xのプログラムです．"python -V"と実行してversionが3.Xの場合は実行できないことがあります ．

レシピはdataディレクトリ内にある"recipe-data.txt"から入力される.
レシピには改行区切りで複数のレシピを登録することが可能
また、スペース区切りでcookpadのURLを指定できます。

例:
```
オムライス http://cookpad.com/recipe/2653946
```