from datetime import datetime
from peewee import (
    SqliteDatabase, Model,FloatField
)

#conexao banco de dadospi
db = SqliteDatabase('dados_esp.db')

#classe responsavel pela conexao db
class BaseData(Model):
    class Meta:
        database = db


class Informacoes(BaseData):
    dados = FloatField()
   



BaseData.create_table()
db.create_tables([Informacoes])


#Forma de popular banco
# dados = Informacoes.create(dados=151.0)
# dados2 = Informacoes.create(dados=155.0)
