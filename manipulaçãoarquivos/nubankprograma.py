import pandas as pd
import csv

def quantidadecolunaslinhas(recebe):
    print(recebe.shape)

def nomelinhas(recebe):
    print(recebe.columns.values)


def calculafatura(total):
    recebe = 0
    for linhas in total:
        if (linhas > 0):
            recebe += linhas

    return recebe


def imprimitotal(recebe):
    print('numero total %.2f' % recebe)

le = pd.read_csv(r"C:\Users\Lenovo i5\Downloads\nubank-janeiro.csv")
print(le)
total = le["amount"]
total = calculafatura(total)
imprimitotal(total)