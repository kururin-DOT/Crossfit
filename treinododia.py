
file=open("dia_a_dia.txt","a", encoding='utf-8')
exercicio=[]
lista=[]
dia=int(input("Que dia é hoje? "))
if dia<0 or dia>31:
    quit()
else:
    ri=str(dia)
mes=int(input("Que mes estamos? "))
if mes<1 or mes>12:
    quit()
else:
    yue=str(mes)
ano=int(input("Em que ano estamos? "))
nian=str(ano)
quantidade=int(input("Quantos exercícios foram realizads hoje? "))
if quantidade<1:
    print("resposta inválida")
    quit()
for i in range (quantidade):
    exercício=input("Exercício feito hoje: ")
    exercicio.append(exercício)
    duração=float(input("Duração desse exercício: "))
    lista.append(str(duração))

for i in range (len(exercicio)):
    a=exercicio[i]
    b=lista[i]
    file.write(ri + f"/" + yue + "/" + nian + ' '+ "exercicios realizado: " + str(a) + ' ' + "Duracao: " + str(b) + '\n')

file.close()