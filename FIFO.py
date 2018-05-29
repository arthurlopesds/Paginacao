def AlgFIFO():
    with open("referencias.txt","r") as arquivo:
        arq = arquivo.readlines()

    referencias = []
    quadros = []

    for i in range(len(arq)):   #Lendo os arquivos e separando o numero de quadros e as ref em variaveis diferentes
        if i == 0:
            quadro = int(arq[i])
        else:
            referencias.append(int(arq[i]))
    n=1
    k=0
    p=0
    faltaDPG=0
    i=0
    limite = 0

    while k < quadro: #já que o quadro começa vazio, preencho ele
        if referencias[i] in quadros:
            i+=1
        else:
            quadros.append(referencias[i])
            faltaDPG+=1
            i+=1
            k += 1
        indice = i

        if i == len(referencias):
            limite  = 1
            break

    if limite!=1:
        sai = quadros[p]
        while n!=0:
            if referencias[indice] in quadros: #verifico se a referencia ja está no quadro, se sim, vou pra outra referencia
                indice+=1
            else:
                quadros.remove(sai) #se nao estiver, removo a primeira que entrou
                quadros.insert(p,referencias[indice]) #adiciono a referencia no lugar da primeira que entrou
                faltaDPG+=1 #+1 falta de pagina
                p+=1 #P que indica qual a pagina que vai sair do quadro
                if p==quadro: #se p igual ao tamanho do quadro, ele é zerado para nao ultrapassar o limite do quadro
                    p=0
                sai = quadros[p] #sai indica quem deve sair na proxima falta de pagina
                indice+=1
            if indice == len(referencias): #se chegou ao fim das referencias
                n=0

        print("FIFO {}".format(faltaDPG))
    else:
        print("FIFO {}".format(faltaDPG))
    return