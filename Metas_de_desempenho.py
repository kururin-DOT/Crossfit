def registrar_metas(meta):
    arquivo_metas = open("metas_de_desempenho.txt", "a", encoding = "utf8")
    arquivo_metas.write(meta + "\n")
    arquivo_metas.close()
    return print("Meta registrada")

def acompanhar_metas(treino):
    try:
        arquivo_metas = open("metas_de_desempenho.txt", "r", encoding = "utf8")
        lista_metas = arquivo_metas.readlines()

        for i in range(len(lista_metas)):
            if str(treino) in lista_metas[i]:
                del lista_metas[i]
                arquivo_metas.close()

                arquivo_metas = open("metas_de_desempenho.txt", "w", encoding = "utf8")
                arquivo_metas.writelines(lista_metas)
                arquivo_metas.close()

                return print("Meta Alcançada!")
    except FileNotFoundError:
        print("\nErro: o arquivo metas_de_desempenho.txt não existe\n")

try:    
    quant_metas = int(input("Quantas metas deseja registrar? "))

    for i in range(quant_metas):
        meta = input("Digite a meta que deseja registrar: ").capitalize()
        registrar_metas(meta)
except ValueError:
    print("Erro: é preciso digitar um valor inteiro")

while True:
    treino_que_fiz = input("Fizesse o que hoje? ").capitalize()

    if treino_que_fiz == "Nada":
        break

    acompanhar_metas(treino_que_fiz)