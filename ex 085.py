num = [[],[]]
valores = 0
for c in range(1,8):
    valores = int(input(f"Digite o {c}°valor:"))
    if valores % 2 == 0:
        num[0].append(valores)
    else:
        num[1].append(valores)
print("***" * 10)
num[0].sort()
num[1].sort()
print(f"Os valores pares digitados foram: {num[0]}.")
print(f"Os valores impares digitados foram:{num[1]}.")

