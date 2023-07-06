# OBS: CÓDIGOS EM PARTES SEPARADOS POR COMENTÁRIOS ENTRE (''' '''), CADA CÓDIGO ESTÁ ENUMERADO PARA MELHOR ENTENDIMENTO.

#Boolean -> True or False -> 1 or 2

#                                                         ---Código 1---

'''
boole = 50 > 55 or 20 < 30
string = 'texto, palavras'
print(type(10 + 5 - 20 * 5 / 4))
lista = ['a', 'b', 'c', 1, 2, 3, 4, 5]
print(boole, lista, string)
A = input('Digite seu nome: ')
B = input('Digite sua idade: ')
print(10 == 10 and 10 - 10 == 0 or 100 == 100)
print('Seu nome é: ', A, 'e sua idade é', B)

# Calculos

calc = 10
calc2 = 20
print('soma:', calc + calc2)
print('sub:', calc - calc2)
print('mult:', calc * calc2)
print('div:', calc / calc2)
print('div int:', calc // calc2)
print('exp:', calc ** calc2)
print('rest:', calc % calc2)
'''


#Cadastro de Pessoas

#                                                         ---Código 2---

'''
print('Cadastro de ficha do paciente.')
paciente = input('Nome do paciente:')
idade = (input('Idade:'))
altura = float(input('Altura:'))
peso = float(input('Peso:'))
imc = peso
imc = imc / altura * 2
if imc > 80.5:
  print('Você está acima do seu imc.')
else:
  print('Seu imc está dentro dos padrões.')
print('Ficha do paciente.')
print('Paciente:', paciente)
print('Idade:', idade, 'anos')
print('Seu imc é:', imc)
'''

#                                                         ---Código 3---

'''
receita = float(input('Insira o valor de RBT12:'))

if receita <=180000:
  pd = 0
  al = 4.0

if receita >180000:
  if receita <=360000:
    pd = 5940
    al = 7.3

if receita >360000:
  if receita <=720000:
    pd = 13860
    al = 9.5

if receita >720000:
  if receita <=180000:
    pd = 22500
    al = 10.7

if receita >180000:
  if receita <=3600000:
    pd = 87300
    al = 14.3

if receita >3600000:
  if receita <=4800000:
    pd = 378000
    al = 19.0

al = al/100
ae = receita*al
ae = ae - pd
ae = ae/receita

print(f'O valor da aliquota efetiva a ser pago para um faturamento será de {receita} reais será de {ae*100}%')

'''

#                                                         ---Código 4---

'''
nome = input('Insira seu nome:')
idade = float(input('Insira sua idade:'))

if idade > 18:
  print(f'{nome} é maior de idade')
if idade < 18:
  print(f'{nome} é menor de idade')
if idade >= 19:
  print(f'{nome} tem mais de 18 anos')
if idade <= 17:
  print(f'{nome} É menor de idade')
if idade != 18:
  print(f'{nome} Não tem 18 anos')

# considerado adolescente de 14 a 18 anos
# considerado adulto de 19 a 60 anos

if idade >=19 and idade <=60:
  print(f'{nome} é adulto')
if idade <=14 and idade >=18:
  print(f'{nome} é adolecente')

if idade <19 or idade >60:
  print(f'{nome} não é adulto')
  '''

#                                                         ---Código 5---

# if(se), elif(se não) e else(se não ignore tudo)

'''
num = int(input())

if num % 3 == 0:
  print(f'{num} é multiplo de 3')
if num % 5 == 0:
  print(f'{num} é multiplo de 5')
if num % 5 == 0 and num % 3 == 0:
  print(f'{num} é multiplo de 15')
'''

#                                                         ---Código 6---

'''
num = int(input())
if num % 5 == 0 and num % 3 == 0:
  print(f'{num} é multiplo de 15')
elif num % 5 == 0:
  print(f'{num} é multiplo de 5')
elif num % 3 == 0:
  print(f'{num} é multiplo de 3')
else:
  print('nada a executar')

'''
#                                                         ---Código 7---

'''
nome = input('Insira seu nome: ')
ativar = int(input('Insira 1 para ATIVA e 2 para RESERVA: '))

imc = float(input('Insira o valor do imc: '))
if ativar == 1:
  if imc > 19 and imc < 24:
    print(f'O candidato de nome {nome} foi aprovado para ATIVA')
  else:
    print(f'O candidato {nome} foi reprovado para ATIVA')
    if imc > 17 and imc < 26:
      print(f'O candidato {nome} foi aprovado para reserva')
'''
#                                                         ---Código 8---

'''
# not inverte uma condição

idade = int(input('Digite sua idade: '))
if not idade >18:
  print('é menor do que 18 anos')
else:
  print('é maior do que 18 anos')

'''

#                                                         ---Código 9---

'''
# idade entre 18 á 60 anos é adulto
# idade maior que 60 anos é idoso
# adolecente entre 15 e 18 anos
idade = int(input('Digite sua idade: '))
peso = float(input('Digite seu peso: '))
if idade >18:
  if idade >18 and idade <60 or peso >60.0 and peso <70.0:
    print('ADULTO')
if idade >12 and idade <17 or peso >50.0 and peso <60.0:
  print('ADOLECENTE')
if idade >1 and idade <11 or peso >40.0 and peso <50.0:
  print('CRIANÇA')

'''
#                                                         ---Código 10---

'''
# listas
# while (Enquanto)
lista_de_nomes = []
while True: #Top
  nome = input('Digite um nome: ')
  lista_de_nomes.append(nome)
  print(lista_de_nomes)

'''
#                                                         ---Código 11---

'''
nomes = []
idades = []
pesos = []

Quantidades = int(input('Quantos dados ? '))
while Quantidades>0:
  Quantidades = Quantidades - 1
  nome = input('Nome: ')
  idade = input('Idade: ')
  peso = input('Peso:')
  nomes.append(nome)
  idades.append(idade)
  pesos.append(peso)

print(f'Nomes da lista adicionados:{nomes}', f'Idades das pessoas: {idades}', f'Idades das pessoas: {pesos}')

'''
#                                                         ---Código 12---

'''
lista = [0,1,2,3,4,5,6,7,8,9]
i = -1
while i<9:
  i=i+1
  print(lista[i])

'''
#                                                         ---Código 13---

'''
total = 0
number = 1
#enquanto    #diferente
while number != 0:
    number = int(input("Digite um número (ou 0 para sair): "))
    total += number

print("A soma dos números é:", total)

'''
#                                                         ---Código 14---

'''
# for vs while



a=30
while a>0:
  print(a)
  a=a-10
print('###########################')

for a in range(0,11): #Percorrendo por posição.
  print(a)

lista = ['a','b','c','d']
for i in lista:
  print(i)

'''
#                                                         ---Código 15---

'''
nomes = []
a = int(input())

while a>0:
  nome = input()
  nomes.append(nome)
  a = a-1
for a in range(0, len(nomes)):
  print(nomes[a])

'''
#                                                         ---Código 16---
'''

a = 0

while a < 5:
    print(a)
    a = a + 1


frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print(fruta)
  
# Explicando a estrutura a baixo
# para i no intervalo(começa em 0, vai até 10 e pula os números de 2 em 2.)

for i in range(0,10,2): # percorrendo por posições.
    print(i)

'''
#                                                         ---Código 17---

'''
#Funções

def saudacao(nome):
    print(f'Olá, {nome} Bem-vindo!')

# Chamando a função
saudacao("Maurício Gonçalves")


def soma(a, b):
    return a + b

resultado = soma(3, 4)
print(resultado)  # Imprime 7


def identidade(rg):
  print('Sua numeração é', rg, 'ok!')
identidade(123638069)

def s(a, b, c):
  return a / b * c
result = s(5, 5, 10)
print(f'Seu resultado total deu {result}')

'''
#                                                         ---Código 18---



def media_aluno(n1, n2):
  m = n1 + n2
  m = m / 2
  return m
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
a = media_aluno(nota1, nota2)
print(a)

if a > 7.1:
  print('Você passou de ano! Parabéns.')
elif a == 7.0:
  print('Você está na média!')
else:
  print('Você rodou!')

