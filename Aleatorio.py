import random

def sugestao_aleatoria():
    try:
        arquivo_treinos = open("treinos.txt", "r", encoding = "utf8")
        lista_treinos = arquivo_treinos.readlines()
        arquivo_treinos.close()
        while True:
            treino_aleatorio = random.choice(lista_treinos).strip()
            if treino_aleatorio != ultimo_treino:
                return print(f"\nQue tal o próximo treino ser {treino_aleatorio}?\n")
    except FileNotFoundError:
        print("\nErro: o arquivo treinos.txt não existe\n")

ultimo_treino = "50 Push-ups"

sugestao_aleatoria()