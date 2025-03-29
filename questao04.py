dias = int(input("Insira a quantidade de dias rodados: "))
km_rodado = int(input("Insira a quantidade de quilometros rodados: "))


if km_rodado > 100:
  km_extra = km_rodado - 100
  valor_adicional = km_extra*12
  total = dias*90 + valor_adicional
  print(f"O valor a pagar será {total}")
else:
  total1= dias*90
  print(f"O valor a pagar será {total1}")
