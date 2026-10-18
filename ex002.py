def lista_notas():
    soma = 0
    notas = [3,10,4,5]
    qtd = len(notas)
    for i in notas:
        soma+=i
    media = soma / qtd
    return media

media = lista_notas()

print(media)




    
    


