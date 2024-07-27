import csv

caminho_do_arquivo: str = 'exemplo.csv'
lista_dados: list = []
with open(caminho_do_arquivo) as csv_file:
    csv_reader: csv.DictReader = csv.DictReader(csv_file)

    for linha in csv_reader:
        lista_dados.append(linha)

    print(lista_dados)



