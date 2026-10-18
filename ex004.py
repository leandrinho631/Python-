def sistema_bancario(saldo_atual, valor, operacao):
    if operacao == "deposito":
        saldo_atual+=valor
    elif operacao == "saque":
        saldo_atual-=valor
    else:
        print("erro")

    novo_saldo = saldo_atual
    return novo_saldo

novo_saldo = sistema_bancario(1000, 139, "saque")

print(novo_saldo)
