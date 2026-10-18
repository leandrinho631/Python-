def dobro(numero):
    numero*=2
    return numero

x2 = dobro(10)

print(x2)


def boas_vindas(nome):
    print(f"Seja bem vindo senhor {nome} contamos com você")

boas_vindas("Carlos")


def somar(a, b):
    resultado = a + b
    return resultado

soma = somar(10, 7)
print(soma)


def verificar_idade(idade):
    if idade >= 18:
        print("Adulto")
    else:
        print("Adolescente")

verificar_idade(20)

def incrementacao(numero):
    numero+=1
    print(numero)


incrementacao(5)

def tabuada(numero):
    for i in range(10):
        print(f"{numero} x {i} = {numero*i}")

tabuada(3)

def impar_par(numero):
    if numero % 2 == 0:
        print("É par")
    else:
        print("É impar")

impar_par(8)

def contagem(contador):
    while contador >= 0:
        print(contador)
        contador-=1

contagem(10)


def calcular_media(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    return media
    

media_alunos = calcular_media(8,1,1)

if media_alunos >= 6:
    print(f"passou sua nota foi {media_alunos:.2f} ")
else:
    print(f"Reprovado sua nota foi {media_alunos:.2f}")


def calculadora(num1, num2, operacao):
    if operacao == "+":
        print(f"a soma deu {num1 + num2}")
    elif operacao == "-":
        print(f"A subtração deu {num1 - num2}")
    elif operacao == "*":
        print(f"A multiplicação deu {num1 * num2}")
    elif operacao == "/":
        if num2 !=0:
            print(f"A divisão deu {num1 / num2}")
        else:
            print("Não tem como dividir por 0")

    else:
        print("Operação inválida")  

calculadora(10,5,"+")
calculadora(10,5,"-")
calculadora(10,5,"*")
calculadora(10,5,"/")


def sistema_caixa(dinheiro, total):
    if dinheiro > total:
        dinheiro-=total
        print(f"Seu troco foi de {dinheiro} reais")
    elif total > dinheiro:
        total-=dinheiro
        print(f"Está faltando {total} reais para concluir sua compra")
    else:
        print("Obrigado pela compra")


sistema_caixa(50, 50)