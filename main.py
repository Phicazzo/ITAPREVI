import datetime

def get_data(msg_inpt):
    isValid=False
    while not isValid:
        data_Inpt=input(f'{msg_inpt}\n(Formato: DD/MM/AA):')
        try:
            d=datetime.datetime.strptime(data_Inpt, "%d/%m/%y")
            isValid=True
            print(d.strftime("%d/%m/%Y"))
            return d
        except:
            print("Data invalida")


def get_valor(msg_inpt):
    isValid=False
    while not isValid:
        valor=input(f'{msg_inpt}\nR$').replace(',','.')
        try:
            Val=float(valor)
            isValid=True
            #print(valor.replace('.',','),Val)
            return Val
        except:
            print("Digite um Número Válido")


def get_sex():
    isValid=False
    while not isValid:
        sex=input("Sexo\nMasculido(M)/Feminino(F)?").upper()
        if sex=="F":
            isValid=True
            return sex
        elif sex=="M":
            isValid=True
            return sex
        else:
            print("Tente novamente!")



class cls_Cargo:
    idCargo=0
    def __init__(self,Cargo,Valor,Data_Inicio,Data_fim):
        self.Cargo = Cargo
        self.Valor = Valor
        self.Data_Inicio=Data_Inicio
        self.Data_fim=Data_fim
        self.__Dias_no_Cargo=(Data_fim - Data_Inicio)
        if self.__Dias_no_Cargo.days > 1825:
            Incorporado = True
        else:
            Incorporado = False
        self.Incorporado=Incorporado
        cls_Cargo.idCargo+=1


        


if __name__ == "__main__":
    Data_Nascimento=get_data("Digite a Data de Nascimento")
    #Data_Nascimento = Para Calcular a Idade

    Data_Admissao=get_data("Digite a Data de Admissão")
    #Data_Admissao pra calcular o inicio de contribuição

    Data_Atual = datetime.datetime.today()
    #Data_Atual = Para Calcular a Idade Atual / Calular o tempo de contribuição
    
    # Print de Teste de datatime
    ##print(f'{Data_Admissao.strftime("%d/%m/%Y")}\n{Data_Nascimento.strftime("%d/%m/%Y")}\n{Data_Atual.strftime("%d/%m/%Y")}')
    #
    
    Valor_Salario_Inicial=get_valor("Insira o Salário Inicial:")
    #Valor do salario inicial / Usar para calculo de valor 
    #print(str(Valor_Salario_Inicial).replace('.',','))
    
    Sexo=get_sex()
    #print(Sexo)
    Lst_Cargos=[]
    Saindo=False
    while not Saindo:
        if input("Adiconar Cargo?\n(S/N)").upper()=="S":
            Cargo=input("Nome do Cargo:").upper()
            Valor=get_valor("Digite o Valor do Cargo:")
            Data_Inicio=get_data("Data de Nomeação:")
            if input("Cargo Atual?\n(S/N)").upper=="S":
                Data_fim=Data_Atual.copy()
            else:
                Data_fim=get_data("Data da Exoneração:")
            novoCargo=cls_Cargo(Cargo,Valor,Data_Inicio,Data_fim)
            Lst_Cargos.append(novoCargo)
            #Cargo,Valor,Data_Inicio,Data_fim)
        else:
            Saindo=True


    for i in Lst_Cargos:
        
        if i.Incorporado :
            x="SIM"
        else:
            x="NÃO"
            #{" "*15}
            #{'-'*500}

        print(f'\nCargo:\n{i.Cargo}\nValor:{i.Valor}\nPeriodo:\nDe:{i.Data_Inicio.strftime("%d/%m/%Y")}    A:{i.Data_fim.strftime("%d/%m/%Y")}\nIncorporado:{x}\n')
