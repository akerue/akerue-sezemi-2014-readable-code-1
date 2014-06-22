#_*_coding:utf-8_*_

import codecs
import sys
import os
import re


# python recipe.py [raw_data] [recipe_id]
# 引数1: レシピデータのファイルパス
# 引数2: 表示するレシピデータのID
argv = sys.argv
argc = len(argv)

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

if __name__ == "__main__":
    if argc >= 2:
        dirpath = argv[1]

        # ディレクトリ内のファイルのリストを作成
        files = []
        for file in os.listdir(dirpath):
            filepath = os.path.join(dirpath, file)
            if os.path.isfile(filepath):
                files.append(file)

        # ユーザリストを作成
        users = []
        pattrn_filename = re.compile(r'^\.*')  # 拡張子除去
        # ユーザ名のルール
        # 小文字のアルファベット、数字、ハイフン、アンダーバー
        # 10文字以内
        pattrn_username = re.compile(r'^[a-z0-9_-]{0,10}')
        for file in files:
            filename = pattrn_filename(file)[0]
            if pattrn_username.search(filename) and len(filename) <= 10:
                users.append(filename)

        # 日本語対応のため，codecs使用
        with codecs.open(filename, "r", encoding="utf-8") as f:
            # ファイルから改行区切りのレシピを取得
            recipes = [line.rstrip() for line in f.readlines()]
    else:
        print "引数が不正です。"
        quit()

    # 重複レシピ削除
    recipes = list(set(recipes))

    recipes_dic = attach_id(recipes)

    if argc == 3:
        recipe_id = int(argv[2])
        if recipe_id in recipes_dic:
            print "%d: %s" % (recipe_id, recipes_dic[recipe_id])
        else:
            print "IDが不正です。"
    else:
        print_dic(recipes_dic)




