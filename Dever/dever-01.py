import csv

def ler_arquivo_csv(nome_arquivo):
    with open(nome_arquivo, mode='r', encoding='utf-8-sig') as arquivo:
        leitor = list(csv.DictReader(arquivo, delimiter=','))
        
        try:
            indice = int(input("Digite um número para selecionar um registro: ")) - 1
            if 0 <= indice < len(leitor):
                linha = leitor[indice]
                
                data_cadastro = linha['dia de cadastro'].strip()
                partes_data = data_cadastro.split('/')
                if len(partes_data) == 3:
                    data_cadastro = f"{partes_data[2]}/{partes_data[1]}/{partes_data[0]}"
                
                print(f"Registro: {indice + 1} Nome: {linha['nome'].strip()}, Data de Nascimento: {linha['data de nascimento'].strip()}, "
                      f"Dia de Cadastro: {data_cadastro}, Hora de Cadastro: {linha['hora de cadastro'].strip()}")
            else:
                print("Número fora do intervalo válido.")
        except ValueError:
            print("Por favor, digite um número válido.")

nome_arquivo = 'dados.csv'
ler_arquivo_csv(nome_arquivo)
