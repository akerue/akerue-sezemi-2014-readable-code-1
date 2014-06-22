#_*_coding:utf-8_*_

import codecs

with codecs.open("./data/recipe-data.txt", "r", encoding="utf-8") as f:
    # 改行区切りのレシピを取得
    recipes = f.readlines()

# 今後レシピの数が増える可能性があるため，イテレートしている
for recipe in recipes:
    # 空行が表示されるのを防ぐ
    print recipe.rstrip()
