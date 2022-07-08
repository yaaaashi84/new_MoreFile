import os
import logging
from playhouse.db_url import connect
from dotenv import load_dotenv
from peewee import Model, IntegerField, CharField

# .envの読み込み
load_dotenv()

logger = logging.getLogger('peewee')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

# データベースへの接続設定
db = connect(os.environ.get('DATABASE'))  # 環境変数に合わせて変更する場合

# 接続NGの場合はメッセージを表示
if not db.connect():
    print("接続NG")
    exit()


class Customer(Model):
    """Customer Model"""
    id = IntegerField(primary_key=True)
    name = CharField()
    age = IntegerField()

    class Meta:
        database = db
        table_name = 'customers'


db.create_tables([Customer])