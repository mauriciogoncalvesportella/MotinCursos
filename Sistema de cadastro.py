import pandas as pd

# Função para cadastrar um novo produto
def cadastrar_produto():
    # Solicita os dados do produto ao usuário
    nome = input('Insira o nome do produto: ')
    quantidade = int(input('Insira a quantidade inicial: '))
    valor_unitario = float(input('Insira o valor por unidade: '))
  
    # Cria um dicionário com os dados do produto
    produto = {
        'Nome': nome,
        'Quantidade': quantidade,
        'Valor Unitário': valor_unitario,
        'Valor Total': quantidade * valor_unitario
    }
  
    # Cria um dataframe a partir do dicionário
    dataframe = pd.DataFrame(produto, index=[0])
  
    # Salva o dataframe no arquivo Excel
    dataframe.to_excel('Motim_Mutimercado.xlsx', index=False)
  
    # Imprime mensagem de sucesso
    print('Produto cadastrado com sucesso!')

# Função para procurar um produto pelo nome
def procura_prod():
    # Solicita o nome do produto ao usuário
    nome = input('Insira o nome do produto: ')
  
    # Lê o arquivo Excel e filtra o dataframe pelo nome do produto
    dataframe = pd.read_excel('Motim_Mutimercado.xlsx')
    produto = dataframe.loc[dataframe['Nome'] == nome]
  
    return produto

# Função para vender um produto
def vender(produto):
    # Solicita a quantidade e o valor por unidade da venda ao usuário
    quantidade = int(input('Insira a quantidade que deseja vender: '))
    valor_unitario = float(input('Insira o valor por unidade para a venda: '))
  
    # Calcula o valor total da venda
    valor_total = quantidade * valor_unitario
  
    # Converte o produto para uma lista
    p = produto.values.tolist()
  
    # Imprime as informações do produto
    print("Informações do produto:")
    for i, coluna in enumerate(produto.columns):
        print(f"{coluna}: {p[0][i]}")
      
    # Verifica se há estoque suficiente para a venda
    if quantidade <= p[0][1]:
        # Calcula o valor mínimo para a venda
        valor_minimo = p[0][2] * (1 - p[0][4])
      
        # Verifica se o valor por unidade está acima do mínimo
        if valor_unitario >= valor_minimo:
            # Venda autorizada
            print(f'Venda autorizada pelo valor: {valor_total} reais.')
          
            # Realiza as ações necessárias para registrar a venda
            dataframe = pd.read_excel('Motim_Mutimercado.xlsx')
            dataframe.loc[dataframe['Nome'] == p[0][0], 'Quantidade'] -= quantidade
            dataframe.loc[dataframe['Nome'] == p[0][0], 'Valor Total'] += valor_total
            dataframe.to_excel('Motim_Mutimercado.xlsx', index=False)
        else:
            # Valor de venda abaixo do mínimo permitido
            print('Valor de venda abaixo do mínimo permitido.')
    else:
        # Venda negada devido à falta de estoque
        print(f'Venda negada! Motivo: Falta de estoque. Você possui {p[0][1]} unidades.')

# Função para exibir o estoque
def exibir_estoque():
    # Lê o arquivo Excel e exibe o dataframe completo
    dataframe = pd.read_excel('Motim_Mutimercado.xlsx')
    print(dataframe)

# Menu principal
while True:
    # Exibe o menu
    print('===== Sistema de Controle de Estoque =====')
    print('1. Cadastrar produto')
    print('2. Procurar produto')
    print('3. Vender produto')
    print('4. Exibir estoque')
    print('5. Sair')
  
    # Solicita a opção ao usuário
    opcao = int(input('Escolha uma opção: '))
  
    # Verifica a opção escolhida
    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        produto = procura_prod()
        if not produto.empty:
            print(produto)
        else:
            print('Produto não encontrado.')
    elif opcao == 3:
        produto = procura_prod()
        if not produto.empty:
            vender(produto)
        else:
            print('Produto não encontrado.')
    elif opcao == 4:
        exibir_estoque()
    elif opcao == 5:
        print('Saindo do sistema...')
        break
    else:
        print('Opção inválida. Tente novamente.')
