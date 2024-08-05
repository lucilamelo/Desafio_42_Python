def calcular_area(largura, altura):
    return largura * altura


forma = input("Você quer calcular a área de um quadrado ou retângulo? ").strip().lower()

if forma == "quadrado":
    lado = float(input("Digite o valor do lado do quadrado: "))
    area = calcular_area(lado, lado)
elif forma == "retângulo" or forma == "retangulo":
    largura = float(input("Digite a largura do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))
    area = calcular_area(largura, altura)

print("A área do", forma, "é: ", area)

