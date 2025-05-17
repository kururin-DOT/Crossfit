def filtrar(movtreino):
    existe_no_crud = 0
    crud = open("arquivo crud.txt", "r", encoding='utf8')
    linhascrud = crud.readlines()
    crud.close()
    filtrando = open("Filtro.txt", "w", encoding='utf8')

    for i in range(len(linhascrud)):
        if movtreino in linhascrud[i]:
            filtrando.write(linhascrud[i] + "\n")
            existe_no_crud += 1

    filtrando.close()
    
    if existe_no_crud == 0:
        return print("Treino ou movimento não existe no crud.")
    
    else:
        return print("Filtragem concluída")

Wodmov_filt = input("Insira o treino ou movimento que deseja filtrar: ").upper()
filtrar(Wodmov_filt)
