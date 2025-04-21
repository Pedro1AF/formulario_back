import random

def gerar_codigo_verificacao():
    return str(random.randint(10000, 99999)).zfill(5)