import random
import string
fi=input('Insira o nome do ficheiro de entrada(entry.txt): ')
fo=input('Insira o nome do ficheiro de saida(.txt): ')
tamanho_grelha=[]
words=[]
matriz=[]



##################################################################################################################################
#“ler_ficheiro”
#Argumentos: arquivo do tipo- ficheiro
#Retorno da função: Retorna duas listas diferentes, uma com as dimensões da grelha e outra com as palavras a implementar na sopa de letras.
##########################################################################################################################################

def ler_ficheiro(arquivo): #lê o ficheiro de entrada e extrai os dados 
    file=open(arquivo,'r')
    
    n=file.readline()
    lista=n.split()
    lista=list(map(int,lista))  #coloca o tamanho da sopa em uma lista
    for i in lista:
        tamanho_grelha.append(i)

    for line in file:
        line=line.replace("\n","")
        words.append(line)
        if(words.count('')>0):
            words.remove('')
            break
    
        
    file.close()
	
##################################################################################
#“cria_grelha”
#Argumentos: tamanho_grelha - lista
#Retorno da função: retorna uma lista de listas preenchida com “ . ”.
####################################################################################	
		
def cria_grelha(tamanho_grelha): #cria uma grelha "vazia" com "."
    # Python tem desdobramento de sequências no assignment
    # essa única linha atribui os valores para n e p
    n, p = tamanho_grelha
    for i in range(n):
        matriz.append([])
        for j in range(p):
            matriz[i].append(".")
			

			
            
def sort_string_descending(palavras): #ordena a lista pelo seu tamanho de forma descendente
    palavras.sort(key=len, reverse=True)  
	
#############################################################################################
#“por_palavra_interno”
#Argumentos:
#tamanho_grelha - lista
#palavra - string
#grelha – lista de listas
#Retorno da função: Coloca as palavras na grelha de forma aleatória.
###################################################################################################	

def por_palavra_interno(tamanho_grelha, palavra,grelha): #coloca a palavra dentro da grelha de forma aleatoria
      n, p = tamanho_grelha
      palavra = random.choice([palavra,palavra[::-1]]) #escolher se a palavra será invertida ou não
                #horizontal,vertical,diagonal
      d = random.choice([[1,0],[0,1],[1,1]]) #decide o sentido da palavra

      if(d[0]==1 and d[1]==0): #se for horizontal
          xtamanho=n-len(palavra)+1
          ytamanho=p
      elif(d[0]==0 and d[1]==1): #se for vertical
          xtamanho=n
          ytamanho=p-len(palavra)+1
      elif(d[0]==1 and d[1]==1): #se for diagonal
          xtamanho=n-len(palavra)+1
          ytamanho=p-len(palavra)+1
        

      x= random.randrange(0,xtamanho)
      y= random.randrange(0,ytamanho)  #posição

      for i, letra in enumerate(palavra):
           char = grelha[x+d[0]*i][y+d[1]*i]   
           if  char!=".":
               # Se atingiu um espaço já preenchido - reiniciar o processo.
               return False
           grelha[x+d[0]*i][y+d[1]*i] = letra.upper()
      return True

	  
#############################################################	  
#“por_palavra”
#Argumentos:
#tamanho_grelha - lista
#palavra - string
#grelha – lista de listas
#Retorno da função: retorna a palavra
##################################################################	  

def por_palavra(tamanho_grelha, palavra, grelha): 
    contador = 0
    while not por_palavra_interno(tamanho_grelha, palavra, grelha): #enquanto não conseguir colocar uma palavra na grelha
        contador += 1
        if contador > 5000:
            raise ValueError("Não foi possível posicionar a palavra {0}".format(palavra))
    print("Pus {0} {1} vezes".format(palavra,contador))
    return palavra

##################################################################################
#“matrix_to_str”
#Argumentos:
#Matrix – lista de listas
#Retorno da função: transforma a grelha anteriormente no formato de lista de listas numa string, retornando assim o resultado esperado da sopa de letras.
##############################################################################################

def matrix_to_str(matrix):
    result=''
    for line in matrix:
        result+=''.join(line)+'\n'

    return result
	
###############################################################################################	
#“preenche_grelha” 
#Argumentos: 
#tamanho_grelha - lista
#grelha – lista de listas
#Retorno da função: Depois de colocadas as palavras na grelha esta função irá susbtituir os “ . ” de forma a preencher com letras geradas aleatóriamente a restante sopa de letras.
######################################################################################################	

def preenche_grelha(tamanho_grelha, grelha): #preenche a grelha com letras aleatorias depois de as palavras estarem colocadas
    for i in range(tamanho_grelha[0]):
        for j in range(tamanho_grelha[1]):
            if grelha[i][j] == ".":
                grelha[i][j]= random.choice(string.ascii_uppercase)
    return matrix_to_str(grelha)

###################################################################################################################
#“escreve_ficheiro”
#Argumentos: 
#in_file – ficheiro inicial com o tamanho da grelha e as palavras (.txt)
#out_file – ficheiro final que inicialmente se encontra vazio (.txt)
#Retorno da função: retorna um ficheiro anteriormente vazio com a sopa de letras gerada bem como as respetivas palavras a encontrar e ainda o número de palavras dentro da sopa de letras.
###########################################################################################################################

                
def escreve_ficheiro(in_file,out_file): #escreve o ficheiro: 1º-nº de palavras,2º-as palavras,3º-a grelha
    leitura=open(in_file)
    escrita=open(out_file,'w')
    ler_ficheiro(in_file)
    cria_grelha(tamanho_grelha)
    sort_string_descending(words)
    escrita.write(str(len(words))+ "\n")
    for palavra in words:
        escrita.write(por_palavra(tamanho_grelha,palavra,matriz)+"\n")
    escrita.write(preenche_grelha(tamanho_grelha,matriz))
    
    
    leitura.close()
    escrita.close()
    
escreve_ficheiro(fi,fo)









