import datetime

def get_data(msg_inpt): #FUNÇÃO DE ENTRADA VALIDADA DE DATA
    isValid=False #ENQUANTO FOR INVALIDO ELE MANTEM NO LOOP
    while not isValid:
        data_Inpt=input(f'{msg_inpt}\n(Formato: DD/MM/AA):')#INPUT DA DATA
        try:
            d=datetime.datetime.strptime(data_Inpt, "%d/%m/%y")#VERIFICA A FOMRATAÇÃO DA DATA
            isValid=True # SE APROVADO SAI DO LOOP CASO CONTRÁRIO MANTÉM PEDINDO UMA DATA VÁLIDA
            return d #RETORNA A DATA VÁLIDA
        except:
            print("Data invalida") #MSG EXIBIDA CASO A DATA SEJA INVÁLIDA


def get_dif_data(Data_Inicio,Data_Fim): #FUNÇÃO DE CALCULO DE DIFERENÇA ENTRE DATAS RESULTANDO EM DIAS 
    datadif=Data_Fim-Data_Inicio#CALCULO DA DIFERENÇA DE DIAS
    Lst_Dias=[]#LISTA PARA ARMAZENAR DO DIA INICIAL ATÉ O DIA FINAL
    Lst_Dias.append(Data_Inicio)#INSERE O DIA INICIAL
    for i in range(int(datadif.days)):#PARA CADA DIA NA DIFERENÇA (DE INICIAL PARA FINAL)
        Lst_Dias.append(Data_Inicio-datetime.timedelta(days=-i)) #ADICIONA 1 DIA DA DATA INICIAL E INCLUI NA LISTA DE DATAS
    Lst_Dias.append(Data_Fim)
    return Lst_Dias #RETORNA A LISTA COM AS DATAS PERCORRIDAS NA DIFERENÇA DE DATAS


def get_valor(msg_inpt):#FUNÇÃO DE ENTRADA DE VALOR PARA FINS MONETÁRIO COM CONDICIONAL DE VALIDADE
    isValid=False 
    while not isValid:
        valor=input(f'{msg_inpt}\nR$').replace(',','.') #INPUT DE VALOR COM , E SUBISTITUI POR . PARA CONVERSÃO EM FLOAT
        try:
            Val=float(valor)
            isValid=True
            #print(valor.replace('.',','),Val)
            return Val #RETORNA O VALOR EM FLOAT PARA TRATAMENTO MONETÁRIO
        except:
            print("Digite um Número Válido") #RETORNA MSG CASO O NUMERO SEJA INVÁLIDO

def get_sex(): #FUNÇÃO PARA ENTRADA DE SEXO MASCULINO OU FEMININO
    isValid=False
    while not isValid:
        sex=input("Sexo\nMasculido(M)/Feminino(F)?").upper() #o INPUT DEVER SER PELA ABREVIAÇÃO M OU F
        if sex=="F":
            isValid=True 
            return sex #RETORNA  O VALOR F
        elif sex=="M":
            isValid=True
            return sex #RETORNA  O VALOR M
        else:
            print("Tente novamente!") #CASO NAO SEJA  M OU F DA INVALIDO E PEDE PARA TENTAR NOVAMENTE


def get_cargo():# FUNÇÃO PARA ADICIONAR CARGO A LISTA DE CARGOS DA CLASSE CARGOS
    isValid=False#CONDICIONADO A LOOP PARA FINS DE INSERIR MULTIPLOS CARGOS 
    while not isValid:
        print(cls_Cargo.idCargo,"Cadatrados") # INFORMA O Nº DE CARGOS CADASTRADOS
        if input("Deseja Cadastrar Novo Cargo?").upper()=="S": # SE SIM (S) INICIA O PROCRESSO DE CRIAÇÃO DE NOVO CARGO
            Cargo = str(input("Insira o Nome do Cargo:\n")) #NOME DADO AO CARGO NA CLASSE CARGO
            Valor = get_valor("Valor do cargo:") #CHAMA A FUNÇÃO PARA OBTER O VALOR EM FLOAT 
            Data_Inicio =get_data("Insira a Data da Nomeação:") #CHAMA FUNÇÃO PARA OBTER DATA DA NOMEAÇÃO #!!! ADICIONAR VALIDADOR 
            if input("Cargo Atual?\n(S/N)").upper()=="S":#SE CARGO ATUAL ADICIONA A DATA ATUAL COMO DATA FINAL
                Data_Fim = datetime.datetime.today()
            else: # CASO NAO SEJA O CARGO ATUAL PEDE O INPUT ATRAVES DA FUNÇÃO GET_DATA() DA DATA DE EXONERAÇÃO #!!! ADICIONAR VALIDADOR
                Data_Fim = get_data("Insira a Data da Exonaração")
            novoCargo=cls_Cargo(Cargo,Valor,Data_Inicio,Data_Fim)#INSTANCIA NOVO CARGO
            cls_Cargo.Lst_Cargos.append(novoCargo)#INCLUI O NOVO CARGO NA LISTA DENTRO DA CLASSE CARGO
        else:
            isValid=True #CASO NAO SE DESEJE ADICIONAR OUTRO CARGO SEGUE-SE EM FRENTE                               


def get_Tempo_sem_contribuir(): # FUNÇÃO PARA DAR ENTRADAS EM PERIODOS SEM CONTRIBUIÇÃO 
    isValid=False #DENTRO DE LOOP PARA PERMITIR MULTIPLAS ENTRADAS
    while not isValid: 
        print(cls_Tempo_Sem_Contribuir.idTempo_Sem_Contribuir," Periodos sem Contribuir Cadastrados.") #INFORMA O Nº DE PERIODOS CADASTRADOS
        if input("Deseja cadastrar algum periodo sem Contribuir?\n(S/N)").upper()=="S": # SE SIM(S) DA INICIO AO CRIAÇÃO DE NOVO PERIODO
            Nome = input("Defina um Nome para o Periodo:\nExemplo: Licença Médica\nNome do Periodo:") #NOME PARA IDENTIFICAR O PERIDO
            Data_Inicio=get_data("Digite o Inicio do Periodo:")#CHAMA FUNÇÃO GET_DATA() PARA DATA DE INICIO DO PERIODO
            Data_Fim=get_data("Digite o Último dia o Periodo:")#CHAMA FUNÇÃO GET_DATA() PARA DATA DE ENCERRAMENTO DO PERIODO
            NovoTempoSemContribuir=cls_Tempo_Sem_Contribuir(Nome,Data_Inicio,Data_Fim)#INSTANCIA NOVO PERIODO
            cls_Tempo_Sem_Contribuir.Lst_Peridos_Sem_Contribuir.append(NovoTempoSemContribuir)#ATRIBUI NOVO PERIODO NA LISTA DE PERIODO DENTRO DA CLASSE DE PERIODOS
        else:
            isValid=True # CASO NAO SEJA DESEJADO ADICIONAR PERIODO PASSA-SE A DIANTE


class cls_Cargo: #CLASEE DE CARGOS
    idCargo=0 #CONTADOR DE QUANTIDADE DE CARGOS
    Lst_Cargos=[] #LISTA DE CARGOS ATRIBUIDOS PELA FUNÇÃO GET_CARGO()
    def __init__(self,Cargo,Valor,Data_Inicio,Data_Fim): #CAMPOS EXIGIDOS CARGO, VALOR , DATA INICIAL, DATA FINAL 
        self.Cargo = Cargo #NOME DADO AO CARGO
        self.Valor = Valor #VALOR DO CARGO (INDIVIDUAL)
        self.Data_Inicio=Data_Inicio #DATA DA NOMEAÇÃO OU ENTRADA NO CARGO
        self.Data_Fim=Data_Fim #DATA DA EXONERAÇÃO , SAIDA DO CARGO OU CASO SEJA O CARGO ATUAL SERA DEFINIDA COMO DATA ATUAL
        self.Periodo_No_Cargo=(Data_Fim - Data_Inicio) #CALCULO DE CONTAGUEM DE DIAS DO DIA INICIAL AO FINAL 
        if self.Periodo_No_Cargo.days > 1825: #SE MAIOR DE 5(ANOS)= 1825 (DIAS) O CARGO DEVE SER INCORPORADO #!!!DEFINIR O MAIRO PERMANESSE
            Incorporado = True
        else:
            Incorporado = False
        self.Incorporado=Incorporado#DEFINE BOLLEAN COMO TRUE SE INCORPORADO OU FALSE CASO NÃO #!!! CONDICIONAR A 10 ANOS INTERROMPIDOS
        self.Datas_No_Cargo=get_dif_data(Data_Inicio,Data_Fim) #DEFINE A LISTA DOS DIAS NO CARGO 
        cls_Cargo.idCargo+=1#SOMA +1 NO CONTADOR DE CARGOS

class cls_Tempo_Sem_Contribuir: # CLASSE DE PERIODOS SEM CONTRIBUIÇÃO
    idTempo_Sem_Contribuir=0 #ID DE Nº DE PERIODOS SEM CONTRIBUIÇÃO
    Lst_Peridos_Sem_Contribuir=[] # LISTA DE PERIODOS SEM CONTRIBUIÇÃO
    def __init__(self,Nome,Data_Inicio,Data_Fim):# CAMPOS NECESSÁRIOS PARA CRIAÇÃO DE PERIODO, NOME , DATA INICIAL E DATA FINAL
        self.Nome = Nome # NOME DADO AO PERIODO
        self.Data_Inicio = Data_Inicio #DATA INICIAL
        self.Data_Fim = Data_Fim #DATA FINAL (OU DATA EM QUE VOLTOU A CONTRIBUIR)
        self.Lst_Peridos_Sem_Contribuir = get_dif_data(Data_Inicio,Data_Fim) #CALCULA A LISTA DE DIAS EM QUE SE NÃO CONTRIBUIU
        cls_Tempo_Sem_Contribuir.idTempo_Sem_Contribuir+=1 #ADICIONA +1 AO CONTADOR DE PERIODOS SEM CONTRIBUIÇÃO


class clss_Funcionario:#CLASSE DE FUNCIONARIO
    idFuncionario=0#CONTADOR DE FUNCIONARIO #!!! IMPLEMENTAR MULTIPLO FUTURAMENTE
    Lst_Funcionarios=[] #LISTA DE FUNCIONARIOS
    def __init__(self,Data_Atual,Nome,Sexo,Data_Nascimento,Data_Admissao,Lst_Cargos,Lst_Peridos_Sem_Contribuir):
        self.Nome = Nome #NOME DO FUNCIONARIO
        self.Sexo = Sexo #SEXO DO FUNCIONARIO PARA DETEMINAÇÃO DE PREVIDENCIA
        self.Data_Nascimento = Data_Nascimento #DATA DE NASCIMENTO DO FUNCIONARIO
        self.Idade = Data_Atual.year - Data_Nascimento.year # CALCULO DE IDADE DO FUNCIONARIO    
        self.Data_Admissao = Data_Admissao # DATA DE ADMISSÃO DO FUNCIONARIO
        self.Lst_Cargos = Lst_Cargos #LISTA CONTENDO TODOS OS CARGOS DO FUNCIONARIO
        self.Lst_Peridos_Sem_Contribuir= Lst_Peridos_Sem_Contribuir # LISTA DE TODOS OS PERIODOS SEM CONTRIBUIÇÃO DO FUNCIONARIO
        clss_Funcionario.idFuncionario+=1 # INCREMENTA +1 NA LISTA DOS FUNCIONARIOS


if __name__ == "__main__": #iNICIAÇÃO DO PROGRAMA
        Data_Atual = datetime.datetime.today() #OBTEM A DATA ATUAL
        Nome = str(input("Nome:")) #SOLICITA A INSERÇÃO DE NOME DO FUNCIONÁRIO
        Sexo = get_sex() #CHAMA FUNÇÃO COM CONDICIONAL PARA OBTER O SEXO DO FUNCIONARIO
        Data_Nascimento = get_data("Insira a Data de Nascimento:") #CHAMA A FUNÇÃO GET_DATA() PARA OBTER A DATA DE NASCIMENTO DO FUNCIONARIO
        Data_Admissao = get_data("Insira a Data de Admissão:")#CHAMA A FUNÇÃO GET_DATA() PARA OBTER A DATA DE ADMISSÃO DO FUNCIONARIO
        get_cargo()  #CHAMA A FUNÇÃO PARA CRIAÇÃO DE LISTA DE CARGOS
        get_Tempo_sem_contribuir() #CHAMA A FUNÇÃO PARA CRIAÇÃO DA LISTA DE PERIODOS SEM CONTRIBUIÇÃO
        '''
        NOVOFUNCIONARIO INSTANCIA A CLASSE FUNCIONARIO
        COM OS ATRIBUITOS 
            *DATA ATUAL = OBTIDA AUTOMATICAMENTE
            *NOME = DADO O INPUT PELO USUÁRIO
            *SEXO = OBITDO ATRAVÉS DA FUNÇÃO GET_SEX() SELECIONADA PELO USUÁRIO
            *DATA DE NASCIMENTO = OBITIDA ATRAVÉS DA FUNÇÃO GET_DATA() COM O INPUT DO USUÁRIO
            *DATA DE ADMISSAO = OBITIDA ATRAVÉS DA FUNÇÃO GET_DATA() COM O INPUT DO USUÁRIO
            *CLS CARGO = TODOS OS CARGOS ADICIONADOS ATRAVÉS DA FUNÇÃO GET_CARGO() DENTRO DA LISTA CONTÉM OS OBJETOS DA CLASSE CARGO
            *CLS TEMPO SEM CONTRIBUIR = TODOS OS PERIODOS SEM CONTRIBUIÇÃO ADICIONADOS ATRAVÉS DA FUNÇÃO GET_TEMPO_SEM_CONTRIBUIR() DENTRO DA LISTA ESTÃO OS OBJETOS DA CLASSE TEMPO SEM CONTRIBUIR
        BASICAMENTE DENTRO DO FUNCIONÁRIO ESTÃO TODAS AS DEMAIS CLASSES 
        '''
        NovoFuncionario=clss_Funcionario(Data_Atual,Nome,Sexo,Data_Nascimento,Data_Admissao,cls_Cargo.Lst_Cargos,cls_Tempo_Sem_Contribuir.Lst_Peridos_Sem_Contribuir)#INSTANCIA A CLASSE DE FUNCIONARIO
        clss_Funcionario.Lst_Funcionarios.append(NovoFuncionario)#ADICIONA O FUNCIONARIO NOVO DENTRO DA LISTA DE FUNCIONARIOS DA CLASSE FUNCIONARIO
        '''
        AQUI SO TEMOS A EXIBIÇÃO DOS DADOS DE CADA FUNCIONARIO 
        '''
        for i in clss_Funcionario.Lst_Funcionarios: 
            print(f'Nome: {i.Nome}\nSexo: {i.Sexo}\nData de Nascimento:{i.Data_Nascimento.strftime("%d/%m/%Y")} Idade: {i.Idade}\nAdmitido em:{i.Data_Admissao.strftime("%d/%m/%Y")}')
            for c in i.Lst_Cargos:

                if c.Incorporado==True:
                    x='SIM'
                else:
                    x='NÃO'

                print(f'Cargo: {c.Cargo}     Valor: R${c.Valor}\nNomeado em:             Exonerado em:\n{c.Data_Inicio.strftime("%d/%m/%Y")}   {c.Data_Fim.strftime("%d/%m/%Y")}\nIncorporado:{x}\n')

                for cc in c.Datas_No_Cargo:
                    print(cc.strftime("%d/%m/%Y"))

            for t in i.Lst_Peridos_Sem_Contribuir:
                print(f'Nome do Periodo:\n{t.Nome}\nData Inical do Periodo:{t.Data_Inicio}\nData Final do Periodo:{t.Data_Fim}')
                for tt in t.Lst_Peridos_Sem_Contribuir:
                    print(tt.strftime("%d/%m/%Y"))
