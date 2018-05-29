def AlgLRU():

    class Ref:

        def __init__(self,valor,tempo):
            self.valor = valor
            self.tempo = tempo

        def obterValor(self):
            return self.valor

        def obterTempo(self):
            return self.tempo

    with open("referencias.txt","r") as arquivo:
        arq = arquivo.readlines()

    referencias = []
    quadros = []
    quadro2 = []
    limite = 0

    for i in range(len(arq)):

        if i == 0:
            valquadro = int(arq[0])  #obtendo o valor do numero de quadros
        else:
            referencias.append(Ref(int(arq[i]),0)) #passando o valor das referencias para o array,junto com o tempo 0
                                                   #porque o tempo só irá ser adicionado mais para frente
    k=0
    i=0
    faltadePG=0

    while k<valquadro: #enquanto o valor de k seja menor que o numero de quadros

        verifica = False
        for l in range(len(quadros)): #laço para verificar os valores que estão no quadro
            if referencias[i].obterValor()== quadros[l].obterValor(): #verifica se o valor da referencia está no quadro
                verifica = True
                break
        if verifica == True: #se o valor estiver, atualiza-se o tempo dele e passa para a proxima referencia
            referencias[i].tempo = i+1
            i+=1
        else: #se nao estiver
            quadros.append(referencias[i]) #adiciona a referencia no quadro
            referencias[i].tempo= i+1 #atualiza o tempo dele
            i+=1 #passa para a proxima referencia
            faltadePG+=1 #deu falta de pagina
            k+=1 #1 posição do quadro preenchida
        if i == len(referencias): #se rodar todas as referencias e nao encher o quadro, para o laço
            limite = 1
            break

    l=0
    indice = i #indice recebe i para continuar a verificação das proximas referencias, ou seja, a partir de 1 depois da que
               #preencheu o quadro
    n=1
    quadros2 = quadros #quadros2 recebe todos que estão em quadro,quadro2 serve para organizar quem tem o menor tempo
                       #e assim informar que deve sair na substituição
    quadros2 = sorted(quadros, key=Ref.obterTempo) #ordenando o tempo das referencias em ordem crescente

    if limite != 1: #se nao chegou no fim da lista de referencias

        while n != 0:
            verifica = False
            for l in range(len(quadros)): #laço para verificar os valores que estão no quadro
                if referencias[indice].obterValor() == quadros[l].obterValor():#se o valor atual da referencia é igual a
                                                        #algum que ja está no quadro
                    verifica = True
                    val = l #val recebe o valor de l para ser usada na hora de atualizar o tempo da referencia no quadro
                    break #se o valor atual estiver no quadro para o laço

            if verifica == True: #se o valor estiver no quadro
                referencias[indice].tempo = indice + 1 #atualiza o seu tempo (o valor do indice+1(ja que indice começo com 0)
                quadros[val].tempo = indice+1 #atualiza o tempo da variavel no quadro
                quadro2=quadros #ja que foi atualizado o tempo de uma referencia
                quadros2 = sorted(quadros, key=Ref.obterTempo) #ordena os tempos em ordem crescente
                indice += 1 #passa para a proxima referencia
            else:
                j=0
                while quadros[j].obterValor()!= quadros2[0].obterValor(): #verificando qual o indice da referencia que tem o
                                                                          #menor tempo no quadro
                    j+=1
                    k+=1 #indice no quadro da referencia de menor tempo

                valorsa = quadros2[0] #pra saber qual referencia vai ser retirada do quadro
                indideadc = j #para saber qual o indice que vai ser adicionado a nova referencia
                quadros.remove(valorsa) #removendo a referencia do quadro
                referencias[indice].tempo = indice + 1  # atualizando o tempo da referencia que vai entrar no quadro
                quadros.insert(indideadc,referencias[indice]) #adicionando a nova referencia no quadro
                quadros2=quadros #ja que ouve uma atualização no quadro
                quadros2 = sorted(quadros,key=Ref.obterTempo) #ordenando os tempos em ordem crescente
                faltadePG+=1 #+1 falta de pagina
                indice+=1#passa para a proxima referencia

            if indice==len(referencias): #quando chegar no fim do arquivo de referencias n=0 para parar o laço
                n=0

                print("LRU {}".format(faltadePG)) # printando a quantidade de falta de paginas

    else: #se limite nao for diferente de 1, significa que o arquivo ja chegou ao fim
        print("LRU {}".format(faltadePG))
    return