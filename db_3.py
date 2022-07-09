# ０．sqlite3をインポート。これがないと始まらない
import sqlite3
# １．DB接続。ファイルがなければ作成する
con = sqlite3.connect('peewee_db.sqlite')
# ２．テーブル作成
con.execute("CREATE TABLE MoreLog(コード INTEGER PRIMARY KEY, 商品名 STRING, 値段 REAL)")
# ３．テーブルにデータを追加
con.execute("INSERT INTO MoreLog(コード, 商品名, 値段) values(1, '苺のショートケーキ', 350)")
con.commit()
# ４．データを更新する
con.execute("UPDATE 商品一覧 SET 値段=450 WHERE コード= 1")
con.commit()
# ５．データ参照
cur = con.execute("SELECT * FROM 商品一覧")
for row in cur:
    print(row)
    print(type(row))
cur.close()
# ５の実行結果
# (1, '苺のショートケーキ', 450.0)
# <class 'tuple'>
# ６．データ削除
con.execute("DELETE FROM 商品一覧")
# ７．テーブル削除
con.execute("DROP TABLE 商品一覧")
# ８．DB接続解除
con.close()