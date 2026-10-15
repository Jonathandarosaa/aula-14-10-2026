print("--- CALCULADORA DE MÉDIA (GRAVAÇÃO) ---")
with open("notas.txt", "r") as arquivo:
    name = arquivo.readline().strip()
    no1 = float(arquivo.readline().strip())
    no2 = float(arquivo.readline().strip())
    no3 = float(arquivo.readline().strip())
media = round((no1+no2+no3)/3, 1)
if media >= 7:
    with open("Aprovado.txt", "w") as aprovado:
        aprovado.write(f"{name}\n")
        aprovado.write(f"{media}\n")
elif media >= 5:
    with open("exame.txt", "w") as exame:
        exame.write(f"{name}\n")
        exame.write(f"{media}\n")
else:
    with open("reprovados.txt", "w") as reprovado:
        reprovado.write(f"{name}\n")
        reprovado.write(f"{media}\n")
print(media)