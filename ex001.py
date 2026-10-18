try:
    numero1 = int(input("digite um múmero"))
    numero2 = int(input("digite um múmero"))
    print(f"{numero1 / numero2}")
except ValueError:
    print("Digite um número")
except ZeroDivisionError:
    print("Não é possivel ser dividido por 0")