ultimo_treino = 'agachamento'

import random

def SugerirTreino():
    try:
        file = open('treinos.txt', 'r', encoding = "utf8")
        lista = file.readlines()
        file.close()

        tipagens = []
        exercicios = []

        for linha in lista:
            linha = linha.strip()
            partes = linha.split('tipagem:')
            exercicio = partes[0].strip()
            tipo = partes[1].strip()
            exercicios.append(exercicio)
            tipagens.append(tipo)
    
        exerc_aleatorio = random.choice(exercicios)
        tipo_aleatorio = random.choice(tipagens)

        try:
            if not exercicios or not tipagens:
                    print("Não foi possível extrair um exercício ou uma tipagem.")
                    return
            while ultimo_treino in exerc_aleatorio:
                exerc_aleatorio = random.choice(exercicios)

            print(f'Sugestão de treino do dia: {exerc_aleatorio} tipagem: {tipo_aleatorio}')
        except NameError:
            print(f'Sugestão de treino do dia: {exerc_aleatorio} tipagem: {tipo_aleatorio}')
    except FileNotFoundError:
         print("\nErro: o arquivo treinos.txt não existe\n")

sugerir = input("Deseja uma sugestão para treino do dia? (Digite 'sim' ou 'não') ").lower()
if sugerir == 'sim':
    SugerirTreino()
