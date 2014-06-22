#_*_coding:utf-8_*_

import codecs

with codecs.open("./data/recipe-data.txt", "r", encoding="utf-8") as f:
    # 改行区切りのレシピを取得
    recipes = f.readlines()

# 改行で区切られたレシピを順番に表示
for recipe in recipes:
    # 空行が表示されるのを防ぐ
    print recipe.rstrip()
