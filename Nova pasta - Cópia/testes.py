from main import *
from pytest import *
def teste_1(origem,destino,tempo,plano,com,sem):
    valores = {"Origem": origem, "destino": destino, "tempo": tempo, "plano": plano,"com fale mais":com, "sem fale mais":sem}
    a=calcular(origem,destino,tempo,plano)
    assert valores==a


teste_1("11","16",20,30,0.00,38.00)
teste_1("11","17",80,60,37.40,136.00)
teste_1("18","11",200,120,167.2,380.00)
teste_1("18","17",100,30,'-','-')
teste_1("18","17",100,30,300,300)
