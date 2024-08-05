cod = (input("Digite o codigo do primeiro produto: "))
nome = (input("Digite nome do primeiro produto: "))
quant = int(input("Digite a quantidade do primeiro produto: "))
preco =  float(input("Digite preço do  primeiro produto: "))

print("Codigo do produto: ",cod,)
print("Nome do produto: ",nome,)
print("Quantidade do produto: ",quant,)
print("Preço do produto: ",preco,)




cod2 = (input("Digite o codigo do segundo produto: "))
nome2 = (input("Digite nome do segundo produto: "))
quant2 = int(input("Digite a quantidade do segundo produto: "))
preco2 =  float(input("Digite preço do segundo produto: "))

print("Codigo do produto: ",cod2,)
print("Nome do produto: ",nome2,)
print("Quantidade do produto: ",quant2,)
print("Preço do produto: ",preco2,)

total = ((quant * preco) + (quant2 * preco2) )


print ("Valor total:" ,total)


