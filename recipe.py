#_*_coding:utf-8_*_

import codecs

def attach_id(array):
    """
    引数で指定した配列の要素に1から昇順にIDを付与した辞書を返す
    """
    ret_dic = dict()
    for i in range(len(array)):
        ret_dic[i + 1] = array[i]
    return ret_dic

def print_dic(dic):
    """
    引数で指定した辞書のキーとバリューを順に表示

    ライブラリにpprintというものがあるが、
    これで出力するとユニコード表示になるため関数を作成
    """
    for k, v in dic.items():
        print "%d: %s" % (k, v)

# 日本語対応のため，codecs使用
with codecs.open("./data/recipe-data.txt", "r", encoding="utf-8") as f:
    # ファイルから改行区切りのレシピを取得
    recipes = [line.rstrip() for line in f.readlines()]

# 重複レシピ削除
recipes = list(set(recipes))

recipes_dic = attach_id(recipes)
print_dic(recipes_dic)




