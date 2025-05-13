try:
 while True:
   escolha1=input("Qual será a ação? (visualizar,adicionar,substituir,remover) ").lower()
   if escolha1=='adicionar':
    file=open("Treino.txt",'a')
    quant=int(input("Quantos treinos você quer adicionar? "))
    for i in range (quant):
        adicionar=input("Insira o treino que você deseja adicionar: ")
        tipagem=input("insira o tipo de treino")
        file.write( adicionar + ' '+ 'tipagem: ' + tipagem + '\n')
    decisão=input("Deseja continuar? ")
    if decisão=='sim':
      continue

   if escolha1=='substituir':
    file=open("Treino.txt",'r')
    lista=file.readlines()
    for i in range (len(lista)):
       print(f"Indice: [{i}] item: {lista[i]}")
    sub=int(input("Qual o índice do item será substituído? "))
    novo=input("qual será o novo treino? ")
    tipagem=input("insira a sua tipagem: ")
    lista[sub]=novo+ ' ' + 'tipagem: '+ tipagem +'\n'
    file.close()
    file=open("Treino.txt","w")
    for i in range (len(lista)):
       valor=lista[i]
       file.write(valor)
    file.close()
    decisão=input("Deseja continuar? ")
    if decisão=='sim':
      continue

   if escolha1=='visualizar':
    file=open("Treino.txt",'r')
    print(file.read())
    decisão=input("Deseja continuar? ")
    if decisão=='sim':
      continue
    
   if escolha1=='remover':
     file=open("Treino.txt",'r')
     lista=file.readlines()
     for i in range (len(lista)):
       print(f"Indice: {i} item: {lista[i]}")
     sub=int(input("Qual o índice do item será substituído? "))
     lista.pop(sub)
     file=open("Treino.txt","w")
     for i in range (len(lista)):
       valor=lista[i]
       file.write(valor)
     file.close()
     decisão=input("Deseja continuar? ")
     if decisão=='sim':
      continue
    
   else:
      file.close()
      break

except:
 breakpoint
