import datetime
import os
import db_config
from dotenv import load_dotenv
from playhouse.db_url import connect
from peewee import Model, IntegerField, TimestampField, _StringField

# .envの読み込み
load_dotenv()

# データベースへの接続設定
# db = SqliteDatabase('peewee_db.sqlite')  # SQLite固定の場合
db = connect(os.environ.get("DATABASE"))  # 環境変数に合わせて変更する場合
# db = connect(os.environ.get('DATABASE') or 'sqlite:///peewee_db.sqlite')  # 環境変数が無い場合にデフォルト値として値を設定することも可能
# 接続NGの場合はメッセージを表示
if not db.connect():
    print("接続NG")
    exit()


class information(Model):
    """Message Model"""

    db_id = db_config.id
    name_jp = _StringField()
    nickname_jp = _StringField()
    birthplace_jp = _StringField()
    job = _StringField()
    hobby_jp = _StringField()
    food_jp = _StringField()
    book_jp = _StringField()
    myword_jp = _StringField()
    color_jp = _StringField()
    music_jp = _StringField()
    # pub_date = TimestampField(default=datetime.datetime.now())

    class Meta:
        database = db
        table_name = "MoreInformation"


db.create_tables([information])
