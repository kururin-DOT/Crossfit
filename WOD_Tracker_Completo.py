import random

def entrada_float_positiva(pergunta):
            while True:
                entrada = input(pergunta).replace(",", ".").strip()
                try:
                    valor = float(entrada)
                    if valor >= 0:
                        return valor
                    else:
                        print("Dado inválido. Digite um número positivo.")
                except ValueError:
                    print("Dado inválido. Digite um número.")

def entrada_int_positiva(pergunta):
            while True:
                entrada = input(pergunta).strip()
                try:
                    valor = int(entrada)
                    if valor >= 0:
                        return valor
                    else:
                        print("Dado inválido. Digite um número inteiro positivo.")
                except ValueError:
                    print("Dado inválido. Digite um número inteiro.")

def filtrar(movtreino):
    existe_no_crud = 0
    try:
        crud = open("dia_a_dia.txt", "r", encoding='utf8')
        linhascrud = crud.readlines()
        crud.close()
        filtrando = open("Filtro.txt", "w", encoding='utf8')
        for linha in linhascrud:
            if movtreino in linha:
                filtrando.write(linha)
                existe_no_crud += 1
        filtrando.close()
        if existe_no_crud == 0:
            print("Treino ou movimento não existe no crud.")
        else:
            print("Filtragem concluída")
            exibindo = open("Filtro.txt", "r", encoding='utf-8')
            exibicao = exibindo.readlines()
            for i in range(len(exibicao)):
                print(exibicao[i])
    except FileNotFoundError:
        print("Arquivo 'dia_a_dia.txt' não encontrado.")

def registrar_metas(meta):
    arquivo_metas = open("metas_de_desempenho.txt", "a", encoding="utf8")
    arquivo_metas.write(meta + "\n")
    arquivo_metas.close()
    return print("\nMeta registrada\n")

def ver_metas():
    try:
        arquivo_metas = open("metas_de_desempenho.txt", "r", encoding="utf8")
        ver = arquivo_metas.read()
        arquivo_metas.close()
        return print("\n" + ver)
    except FileNotFoundError:
        print("\nNenhuma meta foi criada")

def acompanhar_metas(treino):
    try:
        arquivo_metas = open("metas_de_desempenho.txt", "r", encoding="utf8")
        lista_metas = arquivo_metas.readlines()
        for i in range(len(lista_metas)):
            if str(treino) == lista_metas[i].strip("\n"):
                lista_metas[i] = f"{treino} - Alcançada!\n"
                arquivo_metas.close()
                arquivo_metas = open("metas_de_desempenho.txt", "w", encoding="utf8")
                arquivo_metas.writelines(lista_metas)
                arquivo_metas.close()
                return print("\nMeta Alcançada!\n")
    except FileNotFoundError:
        print("\nErro: o arquivo metas_de_desempenho.txt não existe\n")

def sugestao_aleatoria():
    try:
        arquivo_treinos = open("dia_a_dia.txt", "r", encoding = "utf8")
        lista_treinos = arquivo_treinos.readlines()
        arquivo_treinos.close()
        while True:
            treino_aleatorio = random.choice(lista_treinos).strip("\n")
            try:
                if ultimo_treino not in treino_aleatorio:
                    return print(f"\nQue tal o próximo treino ser {treino_aleatorio}?\n")
            except NameError:
                return print(f"\nQue tal o próximo treino ser {treino_aleatorio}?\n")
    except FileNotFoundError:
        print("\nNenhum treino adicionado ainda\n")

while True:
    print("\n=== MENU CROSSFIT ===")
    print("1 - Registrar e Manipular treinos do dia (adicionar, substituir, visualizar, remover)")
    print("2 - Proteínas ingeridas")
    print("3 - Sugerir treino aleatório")
    print("4 - Filtrar movimentos/treinos")
    print("5 - Gerenciar metas de desempenho")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        try:
            while True:
                escolha1 = input("Qual será a ação? (visualizar, adicionar, substituir, remover) ").lower()
                if escolha1 == 'adicionar':
                    # treinododia.py
                    file = open("dia_a_dia.txt", "a", encoding="utf-8")
                    exercicio = []
                    lista = []
                    tipo_de_treino = []
                    dia = int(input("Que dia do mês é hoje? "))
                    if dia < 0 or dia > 31:
                        quit()
                    else:
                        ri = str(dia)
                    mes = int(input("Em que mês estamos? "))
                    if mes < 1 or mes > 12:
                        quit()
                    else:
                        yue = str(mes)
                    ano = int(input("Em que ano estamos? "))
                    nian = str(ano)
                    try:
                        quantidade = int(input("Quantos exercícios foram realizados hoje? "))
                        if quantidade < 1:
                            print("Resposta inválida")
                            quit()
                    except ValueError:
                        print("Resposta inválida")
                        quit()
                    for i in range(quantidade):
                        exercicio_input = input("Exercício feito hoje: ")
                        exercicio.append(exercicio_input)
                        acompanhar_metas(exercicio_input)
                        ultimo_treino = exercicio_input
                        duracao = float(input("Duração desse exercício em minutos: "))
                        lista.append(str(duracao))
                        tipagem = input("Insira o tipo de treino: ")
                        tipo_de_treino.append(str(tipagem))
                    for i in range(len(exercicio)):
                        a = exercicio[i]
                        b = lista[i]
                        c = tipo_de_treino[i]
                        file.write( ri + "/" + yue + "/" + nian + ' | Exercício: ' + str(a) + ' | Duração: ' + str(b) + ' | Tipo: ' + str(c) + '\n')
                    file.close()
                elif escolha1 == 'substituir':
                    file = open("dia_a_dia.txt", 'r', encoding="utf-8")
                    lista = file.readlines()
                    file.close()
                    for i in range(len(lista)):
                        print(f"Índice: {i} item: {lista[i]}")
                    sub = int(input("Qual o índice do item será substituído? "))
                    new_day = int(input("Que dia do mês é hoje? "))
                    if new_day < 0 or new_day > 31:
                        quit()
                    else:
                        new_ri = str(new_day)
                    new_month = int(input("Em que mês estamos? "))
                    if new_month < 1 or new_month > 12:
                        quit()
                    else:
                        new_yue = str(new_month)
                    new_year = int(input("Em que ano estamos? "))
                    new_nian = str(new_year)
                    novo = input("Qual será o novo treino? ")
                    acompanhar_metas(novo)
                    duration = float(input("Duração desse exercício em minutos: "))
                    nova_tipagem = input("Insira a sua tipagem: ")
                    lista[sub] = new_ri + "/" + new_yue + "/" + new_nian + ' | Exercício: ' + novo + ' | Duração: ' + str(duration) + ' | Tipo: ' + nova_tipagem + '\n'
                    file = open("dia_a_dia.txt", "w", encoding="utf-8")
                    file.writelines(lista)
                    file.close()
                elif escolha1 == 'visualizar':
                    file = open("dia_a_dia.txt", 'r', encoding="utf-8")
                    print(file.read())
                    file.close()
                elif escolha1 == 'remover':
                    file = open("dia_a_dia.txt", 'r', encoding="utf-8")
                    lista = file.readlines()
                    file.close()
                    for i in range(len(lista)):
                        print(f"Índice: {i} item: {lista[i]}")
                    sub = int(input("Qual o índice do item será removido? "))
                    lista.pop(sub)
                    file = open("dia_a_dia.txt", "w", encoding="utf-8")
                    file.writelines(lista)
                    file.close()
                else:
                    break
        except Exception as e:
            print(f"Erro: {e}")

    elif opcao == "2":
        # proteinas_ingeridas.py
        proteinas = {
            "carne": {"ppg": 0.30},
            "peixe": {"ppg": 0.22},
            "ovo": {"ppu": 13},
            "laticinio": {"ppg": 0.032},
            "grãos": {"ppg": 0.10},
            "legume": {"ppg": 0.06},
            "fruta": {"ppg": 0.01}
        }
        
        proteina_total = 0

        for alimento in ["carne", "peixe", "laticinio", "grãos", "legume", "fruta"]:
            peso = entrada_float_positiva(f"Quantos gramas de {alimento} foram consumidos? ")
            proteina_total += proteinas[alimento]["ppg"] * peso
        qtd_ovos = entrada_int_positiva("Quantos ovos foram consumidos? ")
        proteina_total += proteinas["ovo"]["ppu"] * qtd_ovos

        print(f"\nTotal de proteínas ingeridas: {proteina_total:.2f}g")

    elif opcao == "3":
        # Aleatorio.py
        sugestao_aleatoria()

    elif opcao == "4":
        # Filtragem.py
        Wodmov_filt = input("Insira o treino ou movimento que deseja filtrar: ").lower()
        filtrar(Wodmov_filt)

    elif opcao == "5":
        # Metas_de_desempenho.py
        opcao = input("Quer ver suas metas ou adicionar? ").lower()
        if opcao ==  "ver":
            ver_metas()
        elif opcao == "adicionar":
            try:
                quant_metas = int(input("Quantas metas deseja registrar? "))
                for i in range(quant_metas):
                    meta = input("Digite a meta que deseja registrar: ")
                    registrar_metas(meta)
            except ValueError:
                print("Erro: é preciso digitar um valor inteiro")    

    elif opcao == "0":
        print("Fechando o programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")