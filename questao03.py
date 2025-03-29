valor = float(input("Insira o valor total da mercadoria comprada"))


if valor > 500:
    valor_total = valor + valor*0.5
    print(f"O valor com impostos é {valor_total}")
else:
    print("O valor não sofrerá impostos")
