#Funções
'''def incluirCliente (a):
    from openpyxl import load_Workbook
    arquivo_excel=Workbook()
    y=load_Workbook("Cadastro.xlsx")
    planilha1=arquivo_excel.active
    for linha in a:
        planilha1.append(linha)

def fecharConta ():
def calcPermanência ():'''

def preencherVetor(valores, tipo):
    vetor = [ ]
    valores = valores.split(',')
    for i in range(len(valores)):
        if tipo == 'int':
            valor = int(valores[i].strip())
        elif tipo == 'float':
            valor = float(valores[i].strip())
        else:
            valor = valores[i].strip()
        vetor.append(valor)
    return vetor

#Banco de dados
quartosS=[1,2,3,4,5,6,7,8,9,15,19]
quartosP=[10,11,12,16,17,18]
quartosH=[13,14,20]

cerveja=['SKOL', 'BRAHMA',]      #7reais
refri=['COCA', 'GUARANA',]       #5reais
amendoin=['AMEN',]               #4reais
bala=['halls', 'chocolate',]     #3reais

#Para salvar a data
import time
data=time.strftime('%Y-%m-%d', time.localtime())
print(f"{data}")
turno=input('Turno: ')
valorPromocional=input('Hoje o valor é promocional (s/n): ').upper()
print()

#Início do Programa
print('O que deseja fazer?')
função=int(input('Deseja: 1-Incluir um cliente     2-Fechar conta: '))
while função<0 or função>2:
    print('Comando inválido!')
    função=int(input('Deseja: 1-Incluir um cliente     2-Fechar conta: '))
while função!=0:

#Para adicionar um cliente
    print()
    if função==1:
        print('Ficha de Cadastro de Cliente')
        
    #Para introduzir o quarto        
        nQuarto=int(input('Número do Quarto: '))                            
        while nQuarto<0 or nQuarto>20:                 #Caso insira o número errado /1        
            print('Quarto inválido ou interditado')
            nQuarto=int(input('Número do Quarto: '))
        
    #Para salvar a hora da entrada
        horaEntrada=time.strftime('%H:%M', time.localtime())
        
        print()
        print('##### Cliente Adicionado #####')
        
    #Para adicionar no Excel

#Para fechar conta:
    elif função==2:
        nQuarto=int(input('Quarto do cliente: '))
    
    #Para diferenciar o tipo de quarto
        if nQuarto in quartosS:
            permanência=60.00
            pernoite=100.00
            horaAd=20.00
        elif nQuarto in quartosP:
            permanência=65.00
            pernoite=140.00
            horaAd=25.00
        elif nQuarto in quartosH:
            permanência=140.00
            pernoite=240.00
            horaAd=40.00
        
    #Para importar a hora da saída
        horaSaída=time.strftime('%H:%M', time.localtime())
        
    #Para importar o tempo de permanência
        tempoPerm=int(input('Insira o tempo em horas inteiras (12 p/ pernoite): '))
        
    #Para calcular o preço da permanência
        if (tempoPerm==12):
            valorPermanência=pernoite
        elif (tempoPerm>3):
            valorPermanência=((tempoPerm-3)*horaAd)+permanência
        else:
            valorPermanência=permanência
        
    #Para saber se teve consumo
        consumoSN=input('Teve consumo (s/n)? ').upper()
        
    #Se teve consumo
        if consumoSN=='S':
            consumido=input('Oque foi consumido? ').upper()
            consumo=preencherVetor(consumido,'str')
        
        #Tentando calcular o consumo XXXXX---------------------------------
            valorConsumo=0
            for i in range (len(consumo)):
                if consumo[i] in cerveja:
                    valorConsumo+=7
                elif consumo[i] in refri:
                    valorConsumo+=5
                elif consumo[i] in amendoin:
                    valorConsumo+=4
                elif consumo[i] in bala:
                    valorConsumo+=3
                    
        else:
            valorConsumo=0
            
        #Valor Total
        valorTotal=valorPermanência+valorConsumo
        print()
        print(f"Valor da Permanência: R${valorPermanência:.2f}  +  Valor do Consumo: R${valorConsumo:.2f}  =  Valor Total: R${valorTotal:.2f}")
        print('##### Conta Fechada #####')

    #Para reiniciar o programa
    print()
    função=int(input('Deseja: 1-Incluir um cliente     2-Fechar conta: '))