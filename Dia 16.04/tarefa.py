print('------------------------------------------------------------------------------------------')
print('1. pegue valores de x e y com z = (x^2 + v^2) / (x-y)^2')

x = int(input('Dê um valor para x: '))
y = int(input('Dê um valor para y: '))
z = (x*x + y*y) / ( x-y )**2

print('O resultado da equação  z = (x^2 + y^2) / (x-y)^2 é ', z)

print('------------------------------------------------------------------------------------------')
print('2. receba um salario float e retorne um novo valor com +35%')

salario = float(input('Digite seu salário : '))
novoS = salario + (salario * 35)/100
print('O salário com reajuste de 35% é ', novoS)

print('------------------------------------------------------------------------------------------')
print('3.leia 2 notas de aluno, calcule a media e diga se ta reprovado ou aprovado com media minimo 6')

notaUm = float(input('Digite sua primeira nota : '))
notaDois = float(input('Digite sua segunda nota :'))
media = (notaUm + notaDois) / 2
if media < 6 :
    print('Reprovado!')
else :
    print('Aprovado!')    
print('----------------------------------------------------------------------------------------------------------')
print('4. faça a mesma coisa do 3 ponto só que caso a nota seja entre 4 e 6.. result em exame, caso -4 reprovado')
notauM = float(input('Digite sua primeira nota : '))
notadOis = float(input('Digite sua segunda nota :'))
mediA = (notauM + notadOis) / 2
if (mediA > 6) :
    print('Aprovado')
elif (mediA <= 6) and (mediA >= 4) :
    print('Em exame')    
else :
    print('Reprovado')
