f=input('Insira o nome do ficheiro a ler: ')
grelha=[]
palavras=[]

#######################################################################################################################
#Selecionar_grelha_solucoes - Esta função lê o ficheiro .txt e armazena numa lista as palavras das soluções e a grelha.
#Argumentos:
#Arquivo – ficheiro (grelha.txt),
#Retorno da função: Lista com as palavras e lista com a grelha
########################################################################################################################


def selecionar_grelha_solucoes(arquivo):
    file=open(arquivo)
    n=int(file.readline()) #numero de palavras
    for i in range(n): #iterar as palavras e colocar em uma lista
        linha=file.readline()
        linha=linha.replace("\n", "")
        palavras.append(linha)
    for line in file: #iterar a grelha e colocar em uma lista
        line=line.replace("\n","")
        grelha.append(line)
        
    file.close()
    
##############################################################################################################################################    
#“verificar_direcoes” – Esta função cria um referencial utilizado as variáveis i e j
#                       que permite que se procure nas oito direções possíveis as palavras após ter sido encontrada a primeira letra.
#Argumentos: 
#op – variável do for da função possibilidades 
#lista_palavras – lista criada pela função  Selecionar_grelha_solucoes (lista)
#soluções – palavras que são dadas pelo ficheiro (.txt)
#I – Posição na coluna (int)
#J – Posição na linha (int)
#
#Retorno: Retorna True ou False consoante o resultado da procura tenha sido o pretendido ou não.
###############################################################################################################################################


def verificar_direcoes(op,grelha,palavra,i,j):
    if(len(palavra)==1): #critério de paragem
        return True
    else:
        if(op==1):  
            i=i    #este
            j=j+1
        elif(op==2):
            i=i    #oeste
            j=j-1
        elif(op==3):
            i=i-1   #norte
            j=j
        
        elif(op==4):
            i=i+1
            j=j       #sul
        elif(op==5):
            i=i-1
            j=j-1    #noroeste
        elif(op==6):
            i=i+1      #sudoeste
            j=j-1
        elif(op==7):
            i=i-1
            j=j+1        #nordeste
        elif(op==8):
            i=i+1
            j=j+1           #sudoeste
    try:
        if(grelha[i][j]==palavra[0].upper()): #se o "slot" da grelha for igual à letra da palavra
            nova=palavra[1:]          #então encurta a palavra

            a=verificar_direcoes(op,grelha,nova,i,j)  #verifica novamente mas agora com a palavra "nova"(encurtada)

            if(a==True):
                return a
        else:
            return False
    except:
        resposta=False
        return resposta   #se der erro returna false
            

########################################################################################         
#“ler_coordenadas_finais” – Esta função indica as coordenadas das palavras encontradas.
#Argumentos:
#i – Posição na coluna (int)
#j – Posição na linha (int)
#w – Posição da lista das soluções (int)
#possibilidades – função
#linha - dicionário
########################################################################################


def ler_coordenadas_finais(z,i,j,possibilidades,linha,w):
    if(possibilidades[z]=='este'):
        return("{0}{1}".format((chr(ord(linha[j])+len(w)-1)),i+1))  
    elif(possibilidades[z]=='oeste'):
        return("{0}{1}".format((chr(ord(linha[j])-len(w)+1)),i+1))
    elif(possibilidades[z]=='norte' ): 
        return ("{0}{1}".format(linha[j],abs(i+1-len(w)+1)))
    elif(possibilidades[z]=='sul'):
        return ("{0}{1}".format(linha[j],abs(i+1+len(w)-1)))
    elif(possibilidades[z]=='noroeste'):
        return ("{0}{1}".format((chr(ord(linha[j])-len(w)+1)),abs(i+1-len(w)+1)))
    elif(possibilidades[z]=='sudoeste'):
        return("{0}{1}".format((chr(ord(linha[j])-len(w)+1)),abs(i+1+len(w)-1)))
    elif(possibilidades[z]=='nordeste'):
        return("{0}{1}".format((chr(ord(linha[j])+len(w)-1)),abs(i+1-len(w)+1)))
    elif(possibilidades[z]=='sudeste'):
        return("{0}{1}".format((chr(ord(linha[j])+len(w)-1)),abs(i+1+len(w)-1)))
        

###############################################################################################################################    
#“possibilidades” – Esta função armazena um dicionário com todas as direções possíveis que uma palavra pode tomar.
#Argumentos:
#lista_palavras – lista criada pela função selecionar_grelha_solucoes (lista)
#soluções – palavras que são dadas pelo ficheiro (.txt)
#i – Posição na coluna (int)
#j – Posição na linha (int)
#w – Posição da lista das soluções (int)
#Retorno: se for True, faz o print das coordenadas. Caso contrário, continua a procurar outras palavras.
###############################################################################################################################       

    
def possibilidades(w,i,j):
    possibilidades={1:"este",2:"oeste",3:"norte",4:"sul",5:"noroeste",6:"sudoeste",7:"nordeste",8:"sudeste"}
    linha={0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}
    nova=w[1:] #encurta a palavra(p.e-"branco" passa a "ranco"
    for z in range(1,9):
        veri=verificar_direcoes(z,grelha,nova,i,j) #vai verificar as oito direções possiveis

        if(veri==True): #se veri returnar True então conseguiu com sucesso achar a palavra em uma das direções
            print("{0}:{2}{1}-{4},{3}".format(w,i+1,linha[j],possibilidades[z],ler_coordenadas_finais(z,i,j,possibilidades,linha,w))) 

            return(veri)
        
    #se veri returnar False então incrementa o valor de z, isto é , vai procurar outra direção
        
##############################################################################################################################################
#“verificar_firstletter” - Esta função vai verificar se a palavra é igual a alguma na grelha procurando em todas as direções. 
#Argumentos:
#Grelha - (lista)
#w – Posição da lista das soluções (int)
#Funcionamento da função: Esta função chama a “possibilidades” caso encontre a primeira letra de uma palavra. Se o resultado da execução da função “possibilidades” for True a função “verificar_primeiraletra” começa a procurar a primeira letra da seguinte palavra.
############################################################################################################################################        
       

def verificar_firstletter(w,grelha):
        for i in range(len(grelha)):    #i-linha ; j-coluna
            for j in range(len(grelha)):
                if(w[0].upper()==grelha[i][j]): #se a primeira letra da palavra for igual à letra da grelha
                    terminado=possibilidades(w,i,j) #chama esta função
                    if(terminado==True):
                        #permite não repetir palavras
                        return terminado
                    
                    
selecionar_grelha_solucoes(f) 
for i in palavras:    #percorre as palavras
    verificar_firstletter(i,grelha)
                                            




                           
                       
    
                    
                    
                    
                
                    
    

    
