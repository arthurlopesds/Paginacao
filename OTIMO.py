def AlgOTM():
    with open("referencias.txt","r") as arquivo:
        arq = arquivo.readlines()

    class Ref:
        def __init__(self,valor,tempo):
            self.valor = valor
            self.tempo = tempo

        def obterValor(self):
            return self.valor

        def obterTempo(self):
            return self.tempo

    def zeraQuadro(q):
        for d in range(len(q)):  # zerando o tempo de todas as referencias
            q[d].tempo = 0

    referencias = []
    quadros = []
    quadros2 = [] #uma copia do quadro que vai servir para ordenar os tempos das referencias em ordem crescente,para assim
                  #ter o conhecimento de quem deve sair do quadro para a entrada de uma nova referencia.

    for i in range(len(arq)):   #Lendo os arquivos e separando o numero de quadros e as ref em variaveis diferentes
        if i == 0:
            quadro = int(arq[i])
        else:
            referencias.append(Ref(int(arq[i]),0))
    k=0
    i=0
    faltadePG = 0
    n= 0
    limite=0

    while k<quadro: #enquanto o valor de k seja menor que o numero de quadros

        verifica = False
        for l in range(len(quadros)): #laço para verificar os valores que estão no quadro
            if referencias[i].obterValor()== quadros[l].obterValor(): #verifica se o valor da referencia está no quadro
                verifica = True
                break
        if verifica == True: #se o valor estiver, atualiza-se o tempo dele e passa para a proxima referencia

            i+=1
        else: #se nao estiver
            quadros.append(referencias[i]) #adiciona a referencia no quadro
            i+=1 #passa para a proxima referencia
            faltadePG+=1 #deu falta de pagina
            k+=1 #1 posição do quadro preenchida
        if i == len(referencias): #se rodar todas as referencias e nao encher o quadro, para o laço
            limite = 1
            break

    indice = i
    n=0
    i=0
    j=0
    entrou = 0
    sai = 0

    if limite!=1: #se a sequencia de referencias nao chegou ao fim
        while n!=1:
            if indice == len(referencias): #quando chegar no fim do arquivo de referencias n=0 para parar o laço
                print("OTM {}".format(faltadePG))
                break
            verifica=False
            for l in range(len(quadros)):
                if referencias[indice].valor == quadros[l].valor: #verificando se a pagina existe no quadro
                    verifica = True
                    break
            if verifica == True: #se existe, passa para a proxima pagina
                indice+=1
            else:
                quadros2 = quadros
                while j<quadro:

                    for i in range(indice+1,len(referencias)): #procurando as paginas que estão no quadro que tem o tempo maior,
                                                                # para saber qual vai ser removida
                        if quadros[j].valor == referencias[i].valor: #procurando onde está a referencia do quadro na
                                                                         # sequencia para saber o seu tempo para uma verificação
                                                                         #posterior.
                                quadros2[j].tempo = i + 1 #adicionando o tempo a referencia
                                break
                    j+=1 #passando de referencia
                j=0
                i=0
                quadros2 = sorted(quadros2,key=Ref.obterTempo,reverse=True) #ordenando as referencias pelo seu tempo em ordem
                                                                            # decrescente
                for i in range(len(quadros2)):  #verificando se existe alguma referencia com o tempo 0
                    if quadros2[i].obterTempo() == 0:
                        sai = quadros2[i]
                        entrou = 1
                        break
                i=0

                if entrou == 0: #se nao tem nenhuma referencia com tempo 0, ou seja , ela ainda aparece na sequencia
                    for i in range(len(quadros)): #laço para pegar a referencia ser retirada, e o seu indice no quadro para
                                                  #adicionar a referencia que vai entrar em seu lugar.
                        if quadros2[0].obterValor() == quadros[i].obterValor():
                            sai = quadros[i] #qual referencia vai ser retirada
                            indiceadc = i #indice de onde vai ser adicionanda a proxima referencia
                            break

                    quadros.remove(sai)  #removendo a referencia do quadro
                    quadros.insert(indiceadc, referencias[indice]) #inserindo a nova referencia
                    quadros2.clear() #apagando os dados
                    zeraQuadro(quadros) #zerando o tempo das referencias do quadro
                    quadros2 = quadros #quadros2 recebe valores e tempos atualizados
                    faltadePG+=1 #+1 falta de pagina
                    indice+=1#Passando para a proxima referencia

                else: #se existem referencias com o tempo 0
                    for i in range(len(quadros)): #laço para verificar qual o indice certo para a nova referencia que vai
                                                  #entrar no lugar da que vai sair
                        if sai.obterValor() == quadros[i].obterValor():
                            indiceadc = i #pegando o indice de onde a nova referencia vai entrar
                            break
                    quadros.remove(sai) #removendo do quadro
                    quadros.insert(indiceadc,referencias[indice]) #inserindo a nova referencia
                    zeraQuadro(quadros)#zerando o tempo de todas as referencias
                    faltadePG+=1#+1 falta de pagina
                    indice+=1 #Passando para a proxima referencia
                    entrou = 0 #Zerando a variavel que indica que tem uma referencia com tempo 0

    else: #se a sequencia de referencias chegou ao fim
        print("OTM {}".format(faltadePG))
    return