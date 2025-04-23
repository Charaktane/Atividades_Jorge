print("Questão 1. Escreva um programa para encontrar a soma S = 3 + 6 + 9 + .... + 333.")
S = 0
for x in range(3,334,3):
    S = S + x
    print(S)

    
print("╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")

print("2. Escreva um programa que leia 10 notas e informe a média dos alunos.")
notas = []
for n in range(10): #Vai perguntar 10 vezes
    nota = float(input(f"Digite a nota {n+1}: ")) #O f quer dizer que é para seguir uma fuction
    notas.append(nota) #junte os valores das notas

media = sum(notas) / len(notas) #pegue o total e divide
print("Média das notas:", media) 

print("╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")

print("Questão 3. Escreva um programa que leia um número de 1 a 10, e mostre a tabuada (+, -, *, /) de 0 - 9, desse número.")
numero = int(input("Digite um número de 1 a 10: "))
if 1 <= numero <= 10:
    for p in range(10):
        print(f"{numero} + {p} = {numero + p}") #ele vai apresentar qual é a operação e após isso, vai executar
        print(f"{numero} - {p} = {numero - p}") #ele vai apresentar qual é a operação e após isso, vai executar
        print(f"{numero} * {p} = {numero * p}") #ele vai apresentar qual é a operação e após isso, vai executar
    if p != 0:
        print(f"{numero} / {p} = {numero / p:.2f}") #vai mostrar a divisão com duas casas decimais
    else:
         print(f"{numero} / {p} = indefinido (divisão por zero)")
         print("-" * 20)
else:
   print("Número fora do intervalo permitido.")

print("╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")

print("Questão 4. As notas de um aluno estão armazenadas em uma lista. Calcular a média dessas notas. ")
notAAS = [3.4, 6.6, 8, 9, 10, 9.5, 8.8, 4.3]
medIa = sum(notAAS) / len(notAAS)
print(medIa)
