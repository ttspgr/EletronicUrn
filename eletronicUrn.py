#Criação das funções do menu principal do programa e iniciação de estruturas utilizadas ao longo do código

cadastroPres = [] # Matriz de dados dos Presidentes
nomePres = [] # Indice 0 do cadastro de Presidentes
numeroPres = [] # Indice 1 do cadastro de Presidentes
partidoPres = [] # Indice 2 do cadastro de Presidentes
votosPres = [] # Indice 3 do Cadastro de Presidentes criado iterativamente, para cada candidato

cadastroGov = [] # Matriz de dados dos Governadores, segue a indexação vista para o cargo de Presidente
nomeGov = []
numeroGov = []
partidoGov = []
votosGov = []

cadastroPref = [] # Matriz de dados dos Prefeitos, segue a indexação vista para o cargo de Presidente
nomePref = []
numeroPref = []
partidoPref = []
votosPref = []

resultadoEleitos = []
partidosEleitos = []
numEleitosPorPartido = []

cadastroEle = [] # Matriz de dados dos Eleitores
nomeEleitor = [] # Indice 0 do cadastro de Eleitores
cpfEleitor = [] # Indice 1 do cadastro de Eleitores

ordemParaAuditoria = [] # Lista contendo a ordem dos editores que registraram seu CPF e votaram

votosEmBranco = [0, 0, 0] # Lista com a quantidade de votos em branco para 0: Prefeito, 1:Governador e 2:Presidente
votosNulos = [0, 0, 0] # Lista com a quantidade de votos nulos para 0: Prefeito, 1:Governador e 2:Presidente

# Função de Cadastro de Candidatos. Módulo generalista de cadastro para candidatos dos cargos Presidente, Governador e Prefeito.
def cadastroCandidatos():
    continuacaoCadastro = "SIM"
    while continuacaoCadastro == "SIM":
        nomeCandidato = input("Insira o nome do candidato: ")
        numeroCandidato = input("Insira o número do candidato: ")
        partidoCandidato = input("Insira o partido do candidato: ")
        cargoCandidato = input("Insira o cargo do candidato: ").lower()

# Recebe os dados do Candidato e as insere em uma lista homóloga para cada dado para diferentes cargos.
        if cargoCandidato == "presidente":
            nomePres.append(nomeCandidato)
            numeroPres.append(numeroCandidato)
            partidoPres.append(partidoCandidato)

        elif cargoCandidato == "governador":
            nomeGov.append(nomeCandidato)
            numeroGov.append(numeroCandidato)
            partidoGov.append(partidoCandidato)

        elif cargoCandidato == "prefeito":
            nomePref.append(nomeCandidato)
            numeroPref.append(numeroCandidato)
            partidoPref.append(partidoCandidato)

        continuacaoCadastro = input("Deseja cadastrar um novo candidato? Digite SIM para continuar, ou NÃO para encerrar o cadastramento de candidatos. ")

# Recebe os dados de candidato em forma de listas e as insere em uma matriz para cada cargo.
    cadastroPres.append(nomePres)
    cadastroPres.append(numeroPres)
    cadastroPres.append(partidoPres)
    cadastroPres.append(votosPres)

    cadastroGov.append(nomeGov)
    cadastroGov.append(numeroGov)
    cadastroGov.append(partidoGov)
    cadastroGov.append(votosGov)

    cadastroPref.append(nomePref)
    cadastroPref.append(numeroPref)
    cadastroPref.append(partidoPref)
    cadastroPref.append(votosPref)

# Função de Cadastro de Eleitores. 
def cadastroEleitores():
    continuacaoCadastro = "SIM"
    while continuacaoCadastro == "SIM":
        eleitor = input("Insira o nome do Eleitor: ")
        cpf = input("Insira o CPF do eleitor: ")
        nomeEleitor.append(eleitor)
        cpfEleitor.append(cpf)
        continuacaoCadastro = input("Deseja cadastrar um novo eleitor? Digite SIM para continuar, ou NÃO para encerrar o cadastramento de eleitores. ")
    cadastroEle.append(nomeEleitor)
    cadastroEle.append(cpfEleitor)

# Popula vetor de votos com elementos nulos para votação de acordo com o número de candidatos cadastrados
def populaVetor():
    for i in range(len(cadastroPref[0])):
        votosPref.append(0)
    for i in range(len(cadastroGov[0])):
        votosGov.append(0)
    for i in range(len(cadastroPres[0])):
        votosPres.append(0)

# Função de Verificação do CPF previamente a votação. 
def verificadorCPF(listaDeCadastro):
    cpfAVerificar = input("Insira o CPF: ")
    while cpfAVerificar not in listaDeCadastro:
        print("CPF não cadastrado. Informe um CPF válido para votação: ")
        cpfAVerificar = input("Informe seu CPF: ")
    ordemParaAuditoria.append(cadastroEle[0][listaDeCadastro.index(cpfAVerificar)])    
    return cpfAVerificar

# Função de votos generalista, que verifica a entrada do voto e a adiciona a uma lista de votos.
def votoPorCargo(cargo, indiceParaBrancosENulos, listaDeCandidatos):
    confirmacao = ""
    while confirmacao != "CONFIRMA":
        print(f'Para votar em {cargo}, por favor insira o número do candidato. \nCaso deseje votar em branco, digite "-1". \nCaso deseje votar nulo, digite "-2". \nApós a inserção do número do candidato, serão exibidas as informações. \nCheque os dados mostrados e verifique o seu voto. \nSe as informações exibidas estão de acordo com seu voto, digite "CONFIRMA".')
        declaracaoDeVoto = input()
        if declaracaoDeVoto == '-1':
            print("Voto em Branco.")
            confirmacao = input('Caso esse seja seu voto, digite: "CONFIRMA". \nSe esse não for seu voto digite: "RETORNA"\n')
            if confirmacao == 'CONFIRMA':
                votosEmBranco[indiceParaBrancosENulos] += 1
        elif declaracaoDeVoto == '-2':
            print("Voto Nulo.")
            confirmacao = input('Caso esse seja seu voto, digite: "CONFIRMA". \nSe esse não for seu voto digite: "RETORNA"\n')
            if confirmacao == 'CONFIRMA':
                votosNulos[indiceParaBrancosENulos] +=1
        elif declaracaoDeVoto in listaDeCandidatos[1]:
            print(f"Voto em {declaracaoDeVoto} \nCandidato: {listaDeCandidatos[0][listaDeCandidatos[1].index(declaracaoDeVoto)]} \nNúmero do Candidato: {listaDeCandidatos[1][listaDeCandidatos[1].index(declaracaoDeVoto)]} \nPartido do Candidato: {listaDeCandidatos[2][listaDeCandidatos[1].index(declaracaoDeVoto)]}")
            confirmacao = input('Caso esse seja seu voto, digite: "CONFIRMA". \nSe esse não for seu voto digite: "RETORNA"\n')
            if confirmacao == 'CONFIRMA':
                listaDeCandidatos[3][listaDeCandidatos[1].index(declaracaoDeVoto)] += 1
                    
# Ordenador da quantidade de votos para exibição de resultados em ordem decrescente
def ordenador(listaDeCadastro):
    for i in range(len(listaDeCadastro[3])):
        maior = i

        for j in range(i+1, len(listaDeCadastro[3])):
            if listaDeCadastro[3][j] > listaDeCadastro[3][maior]:
                maior = j

        if listaDeCadastro[3][i] != listaDeCadastro[3][maior]:
            auxiliar = listaDeCadastro[3][i]
            listaDeCadastro[3][i] = listaDeCadastro[3][maior]
            listaDeCadastro[3][maior] = auxiliar

            auxiliar = listaDeCadastro[0][i]
            listaDeCadastro[0][i] = listaDeCadastro[0][maior]
            listaDeCadastro[0][maior] = auxiliar

            auxiliar = listaDeCadastro[2][i]
            listaDeCadastro[2][i] = listaDeCadastro[2][maior]
            listaDeCadastro[2][maior] = auxiliar

# Função do item 4 do menu da urna. Retorna dados da Eleição de acordo com o cargo fornecido nos parâmetros
def apuracao(cargo, indiceParaBrancosENulos, listaDeCandidatos):
    totalValidos = sum(listaDeCandidatos[3])
    totalBrancosCargo = votosEmBranco[indiceParaBrancosENulos]
    totalNulosCargo = votosNulos[indiceParaBrancosENulos]
    totalVotos = totalValidos + totalBrancosCargo + totalNulosCargo
    porcentagemValidos = totalValidos/totalVotos
    porcentagemBrancos = votosEmBranco[indiceParaBrancosENulos]/totalVotos
    porcentagemNulos = votosNulos[indiceParaBrancosENulos]/totalVotos
    print(
    f"        RANKING DO RESULTADO PARA {cargo}              "
    )
    print(
    "|  Nome  | Partido | Total de Votos | % votos Válidos | ")
    for item in range(len(listaDeCandidatos[0])):
        print(
    f"| {item+1}. {listaDeCandidatos[0][item]}  | {listaDeCandidatos[2][item]} | {listaDeCandidatos[3][item]} | {listaDeCandidatos[3][item]/sum(listaDeCandidatos[3])*100:.2f}%"        
        )
    print(
    f"| Total de votos = {totalVotos}\n"
    f"| Total de votos válidos e % = {totalValidos}; {porcentagemValidos*100:.2f}%)\n"
    f"| Total de brancos e % = {votosEmBranco[indiceParaBrancosENulos]} ({porcentagemBrancos*100:.2f})%\n"
    f"| Total de nulos e % = {votosNulos[indiceParaBrancosENulos]} ({porcentagemNulos*100:.2f})%" 
    )

# Função para auditoria dos votos de eleitores com relação aos candidatos. Verifica de acordo com o cargo
def checaQtdVotos(indiceParaBrancosENulos, listaDeCandidatos):
    qtdDeVotosEleitores = len(ordemParaAuditoria)
    qtdDeVotosBrancosCandidatos = votosEmBranco[indiceParaBrancosENulos]
    qtdDeVotosNulosCandidatos = votosNulos[indiceParaBrancosENulos]
    qtdDeVotosCandidatos = (sum(listaDeCandidatos[3]) + qtdDeVotosBrancosCandidatos + qtdDeVotosNulosCandidatos)/3
    if qtdDeVotosCandidatos == qtdDeVotosEleitores:
        return True
    else: 
        return False

# Função que popula um vetor apenas com o primeiro posicionado da lista de candidatos, após ordenação
def vencedores(listaDeCandidatos):
    resultadoEleitos.append(listaDeCandidatos[2][0])

# Função para criação de lista alternativa a fim de eliminar as redundâncias de partidos que aparecem mais que uma vez na lista anterior
def populapartidosEleitos():
    vencedores(cadastroPres)
    vencedores(cadastroGov)
    vencedores(cadastroPref)
    for partido in resultadoEleitos:
        if partido not in partidosEleitos:
            partidosEleitos.append(partido)

# Contagem de Eleitos e adição a um vetor que apresentará, de acordo com a ordem da lista populada anteriormente, o número de candidatos eleitos daquele partido
def qtdEleitosPartido():
    for partido in partidosEleitos:
        numEleitos = resultadoEleitos.count(partido)
        numEleitosPorPartido.append(numEleitos)    
        
# Função para relatório e estatísticas da eleição que utiliza das funções anteriores para ordem de votação dos eleitores, e estatísticas da eleição
def relatorio():
    print('Eleitores que votaram:')
    for i in ordemParaAuditoria:
        print(i)
    checaPref = checaQtdVotos(0, cadastroPref)
    checaGov = checaQtdVotos(1, cadastroGov)
    checaPres = checaQtdVotos(2, cadastroGov)
    if checaPref and checaGov and checaPres:
        print(f"O Total de Eleitores é igual ao total de votos (auditoria): {len(ordemParaAuditoria)}")
    populapartidosEleitos()
    qtdEleitosPartido()
    print(f"Partido que elegeu mais políticos: {partidosEleitos[0]} ({numEleitosPorPartido[0]})")
    print(f"Partido que elegeu menos políticos: {partidosEleitos[-1]} ({numEleitosPorPartido[-1]})")
    
# Função de exibição do menu principal e seleção da ação na urna eletrônica    
def exibeMenu():
    while True: # Laço de continuidade para execução da função após saída de uma ação
        print('+++++++ MENU - SIMULADOR DO SISTEMA DE VOTAÇÃO +++++++' '\n1. Cadastrar Candidatos' '\n2. Cadastrar Eleitores' '\n3. Votar' '\n4. Apurar Resultados' '\n5. Relatório e Estatísticas' '\n6. Encerrar')
        entrada = input('Opção escolhida:\n') # Escolha de ação pelo usuário seguido das diferentes verificações para ações respectivas
        if entrada == '1':
            cadastroCandidatos()
            populaVetor()
        elif entrada == '2':
            cadastroEleitores()
        elif entrada == '3':
            verificadorCPF(cpfEleitor)
            votoPorCargo('Prefeito', 0, cadastroPref)
            votoPorCargo('Governador', 1, cadastroGov)
            votoPorCargo('Presidente', 2, cadastroPres)      
        elif entrada == '4':
            ordenador(cadastroPref)
            ordenador(cadastroGov)
            ordenador(cadastroPres)  
            apuracao('PRESIDENTE', 2, cadastroPres)
            apuracao('GOVERNADOR', 1, cadastroGov)
            apuracao('PREFEITO', 0, cadastroPref)
        elif entrada == '5':
            ordenador(cadastroPref)
            ordenador(cadastroGov)
            ordenador(cadastroPres)
            relatorio()
        elif entrada == '6':
            break

exibeMenu()