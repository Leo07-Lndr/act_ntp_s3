total = 0
while True:
    n = input("Número (Escribe el numero 0 para terminar): ")
    if n == "0":
        break
    total += float(n)
print("Total:", total)