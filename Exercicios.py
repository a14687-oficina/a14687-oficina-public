#Exercício FP6: Imprimir números de 1 a 10.
#Escreve um programa em Python que use um ciclo for para imprimir todos os números de 1 a 10.
i = 1
while i < 11:
  print (i)
  i += 1
#Soma de números de 1 a 100.
#Escreve um programa que use um ciclo while para calcular a soma de todos os números de 1 a 100.
numero = 1
soma = 0
while numero <= 100:
  soma += numero
  numero += 1
print (f"A soma de todos os números de 1 a 100 é {soma}")

#Exercício FP8: Contagem de vogais numa string.
#Escreve um programa que peça ao utilizador para introduzir uma frase e utilize um ciclo for para contar quantas vogais (a, e, i, o, u) existem na frase.
frase = input("Insira uma frase: ")
vogal = 0
for letra in frase:
  if letra.lower() in "aeiou":
    vogal += 1
print (f"Esta frase tem {vogal} vogais")

#Exercício FP9: Listar múltiplos de 5.
#Escreve um programa que utilize um ciclo for para listar todos os múltiplos de 5 entre 1 e 50.
for i in range(1, 51):
  if i % 5 == 0:
    print(i)

#Exercício FP10: Verificar se um número é primo.
#Escreve um programa que peça ao utilizador um número inteiro e verifique se ele é primo. Um número primo é divisível apenas por 1 e por ele mesmo. O programa deve utilizar um ciclo for para testar se o número é divisível por algum outro número.
numero = int(input("Escreva um número: "))
if numero < 0:
    print("Número inválido. Escreva apenas valores positivos")
if numero == 0 or numero == 1:
    print(f"insira um número maior.")
else:
    if numero == 2:
        print("2 é primo")
    elif numero % 2 == 0:
        print(f"{numero} não é primo, pois 2 é o único número par primo.")
    else:
        x = 3
        while x < numero:
            if numero % x == 0:
                break
            x = x + 2
        if x == numero:
            print(f"{numero} é primo")
        else:
            print(f"{numero} não é primo, pois é divisível por {x}")

#Exercício FP11: Média de uma lista de números.
#Escreve um programa que crie uma lista de 5 números inteiros, pede ao utilizador para introduzir cada número e, em seguida, calcula e exibe a média desses números.
notas = [] #Criação da lista.
for i in range(0,5): #Ir até 5.
    numeros = int(input("Insira um valor inteiro: ")) #Pedir o valor ao utlizador.
    notas.append(numeros) #Adicionar um elemento á lista
soma = sum (notas) #Devolve o número total de elementos da lista
x = len(notas) #Devolve o número total de elementos da lista
media = (soma / x) #Cálculo da soma.
print (media) #Mostrar a média
print (notas) #Mostrar a lista

#Exercício FP12: Gerar uma lista de números pares.
#Cria um programa que utilize a função range() e um ciclo for para gerar uma lista com todos os números pares entre 1 e 20 e imprima a lista.
pares = [] #Criar a lista
for i in range (1,21): #Apenas mostrar números até 20
  if i % 2 == 0: #Script para verificar se um número é par.
    pares.append(i) #Adicionar itens á lista.
print (pares) #Mostrar apenas os números pares

#Exercício FP13: Inverter uma string.
#Escreve um programa que peça ao utilizador para introduzir uma palavra ou frase e utilize um ciclo para imprimir a string invertida.
texto = str(input("Insira um texto: ")) #Pedir o texto ao utilizador 
textoinv = texto [::-1] #Script para inverter o texto/ https://www.w3schools.com/python/numpy/numpy_array_slicing.asp
print (textoinv) #Printar o texto invertido

#Exercício FP14: Tabuada de multiplicação
#Escreve um programa que gere a tabuada de multiplicação de um número introduzido pelo utilizador. O programa deve utilizar um ciclo for para calcular e exibir a tabuada até 10.
tabuada=int(input("Tabuada do numero: ")) #Pedir o valor ao utilizador 

for count in range(10): #Para apenas dar print até 10
    print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)) ) # %d é como se criasse uma variavél para poder fazer contas e dar print logo em seguida.
#Usando o ciclo for.
num = int(input("Insira o número: "))
for i in range (1,11):
  mult = num * i
  print (f"{num} x {i} = {mult}")
#Usando o ciclo while. 
num = int(input("Insira o número: "))
i = 1
while i < 11:
  mult = num * i
  print (f"{num} x {i} = {mult}")
  i += 1
#Exercício FP15: Fatorial de um número
#Escreve um programa que utilize um ciclo while para calcular o fatorial de um número introduzido pelo utilizador. O fatorial de um número n (n!) é o produto de todos os números inteiros positivos até n.
numero = int(input("Insira um número: ")) #Pedir ao utilizador o valor
resultado = 1
count = 1
while count <= numero: #Enquanto um for menor que o outro fazer a conta
    resultado *= count
    count += 1

print(f"O fatorial de {numero} é {resultado}")
