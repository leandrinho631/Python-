def notas(lista_notas):
    os_melhores = []
    
    for i in lista_notas:
        if i >= 7:
            os_melhores.append(i)
        
    return os_melhores

os_melhores = notas([0,10,9,8,0,3,4,5,6,7,8,9,7.6,8.9])

print(os_melhores)




    

