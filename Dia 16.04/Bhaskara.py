# Fórmula de Bhaskara do zero

# Entrada dos coeficientes
a = float(input("digite o valor de a: "))
b = float(input("digite o valor de b: "))
c = float(input("digite o valor de c: "))

if a == 0:
    print("isso não é uma equação do 2º grau")
else:
    # Calcula o delta
    delta = b*b - 4 * a * c
    print(f"delta = {delta}")

    # Verifica o valor de delta
    if delta < 0:
        print("não possui raízes reais.")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"A equação possui uma raiz real: x = {x}")
    else:
        raiz_delta = delta ** 0.5
        x1 = (-b + raiz_delta) / (2 * a)
        x2 = (-b - raiz_delta) / (2 * a)
        print(f"A equação possui duas raízes reais:")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
