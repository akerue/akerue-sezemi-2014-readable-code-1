# Pythonグループ発表

## レビューの流れ

1. グループで各自が選んだベストオブリーダブルコードを発表
2. その中から、上位2つを多数決選択

---

## ベストオブリーダブルコード

---

### 実行結果が明示されたREADME

---

README.md内に実行方法のみではなく，
実行結果も表示

正しいプログラム挙動をユーザが確認しやすい

```
$ python cookpad_assignment.py
input the file_name, you want to use > recipes-data.txt
input the id, you want to show (first == 0) > 
>>> 0 ome-rice
>>> 1 oyako-don
>>> 2 annin-tofu

$ python cookpad_assignment.py
input the file_name, you want to use > recipes-data.txt
input the id, you want to show (first == 0) > 1
>>> 1 oyako-don
```

URL: https://github.com/kajiwara0126/kajiwara0126-sezemi-2014-readable-code-1

きっかけ: プログラムの進捗を確認しようとした時に

どこまでの機能が実装されているかを確認することができた．

---

### AtoBパターン関数名

---

関数がどういう挙動を行うかを短く表記

例: リストの型を入力すると辞書の型が出力される

```
def list2dict(val_list):
    return dict(zip(range(0,len(val_list)), val_list))
```

URL: https://github.com/akerue/YOwatari-sezemi-2014-readable-code-1/blob/master/src/main.py#L12

きっかけ: Linuxの命名慣習に基づいたものになっているので，

プログラマフレンドリな名前になっており，

コードを読んだ際にすんなりと理解できた．
