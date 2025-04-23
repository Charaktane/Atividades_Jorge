#1.Dada a lista L = [ 5, 7, 2 , 9 , 4, 1, 3 ], escreva um programa que imprima as seguintes informações:
L = [5, 7, 2, 9, 4, 1, 3]
#A) tamanho da lista
print("Tamanho da lista:", len(L))
#B) Maior valor da lista:
print("Maior valor da lista:", max(L))
#C) Menor valor da lista:
print("Menor valor da lista:", min(L))
#D) Somar todos os elementos da lista.
print("Soma de todos os elementos da lista:", sum(L))
#E) Em ordem crescente
print("Lista em ordem crescente:", sorted(L))
#F) Ordem decrescente 
print("Lista em ordem decrescente:", sorted(L, reverse=True))

# 2. Gere uma lista contendo os múltiplos de 3 entre 1 e 50

multiplos_de_3 = [x for x in range(3, 51, 3) 
#Ele vai criar uma sequência com o range(3,51,3)  = valores de 3 até 51 com intervalo de 3
                  
print("Múltiplos de 3 entre 1 e 50:", multiplos_de_3)
