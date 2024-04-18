#Tempo
#import time
#Renicialização
reniciar = 0
#Valores para as ondas
#Número
n = int(10)# número desejado a ser multiplicado
n_di = int(10)# número divisor
armazenador_x = int(1)#Armazenador do x
#Quantidade
quant = int(1)
#Quantidade desejada
#Largura
quant_dej_dir = int(100)#direita
quant_dej_es = int(20)#esquerda
#Total
quant_dej = quant_dej_dir+quant_dej_es
#Altura
#Esquerda
left = int(1)#esquerda marcadora
left_des = int(5)#esquerda desejada
#Direita
rigth = int(1)#direita marcadora
rigth_desj = int(100)#direita desejada
rigth_armazenada = rigth_desj
#Espaçamento
esp = int(1)
esp_des = int(2)
#Suava|Robusto
pro_ro = 0#geral
#lados
pro_ro_es = 0#esquerdo
pro_ro_di = 0#direito
#Orientador
orientador = int(0)
#Ciclo
ciclo = 0
ciclo_des = 2
#Contador
contar = 0
#Mais não!
mais_no = 0
while (reniciar != 1):
    #Início
    if(mais_no != 1):
        print("Olá, bem_vindo ao ondinhas.com!","\n" ,"Aqui você pode, como deve ter presumido, fazer ondinhas dos mais variáveis jeitos, deste de suaves á ondas ígrimes ou, até, verdadeiras tempestades, além de poder personalisa-lás.", "\n", "Caso queira ver o projeto de uma vez, apenas pressione c no termianal! Porém, caso queria mudar alguma das configurações das ondas, sinta-se a vontade para fazer isso. Apenas digite config e faça as suas mudanças")
    comecar = str(input(""))
    #Configurações
    if(comecar == "config"):
        comecar = str(input(""))
        print("Por padrão elas vem com as seguintes configurações:", "\n", "O valor de Largura(quantidade de linhas que a ondinha terá) é, para cada lado da ondinhas, 40 linhas", "\n", "Já a sua altura(ou peenchimento) é de cerca de 20 digitos em ambos os lados","\n", "O valor do espaçamento é 6", "\n", "A suavidade geral está ativida ativada", "\n", "As ondas se repentem em 2 ciclo(um ciclo para cada lado)","\n","E, para finalizar, o número padrão para ser multiplicado é o 10, o qual é também o divisor","\n", "Para modifica-lás digite logo abaixo o nome da configuração que quer modificar, sendo:","\n", "'T' para o tamanho", "\n","'A' para preenchimento","\n", "'S' para a suavidade", "\n", "'E' para selecionar o espaçamento","\n", "'C' para ciclo", "\n","'N'[m|di] para multiplicar[m] algum número e [di] para escolher o divisor","\n","Caso queira voltar ao velho padrão, digite p na linha de comando", "\n", "Assim como: caso queria confirmar as configurações digite: 'F', e para listar as configurações, digite: 'L'", "\n", "Nota: caso queira ser mais específico na hora da aplicação, digite, exceto no N, as opações di/es para configurar os valores do lado direito/esquerdo respectivamente","\n", "Agora é você definirá as confiurações aqui, não eu mais, desenvolvedor...")
        configuracoes = 1
        while(configuracoes == 1):
            print("Escolha alguma das configurações")
            comecar = str(input(""))
            #Tamanho
            if(comecar == "T") or (comecar == "t"):#geral
                print("Tamanho geral:")
                quant_dej = int(input(""))
                quant_dej_dir = quant_dej/2
                quant_dej_es = quant_dej/2
            elif(comecar == "T di") or (comecar == "t di"):#direita
                print("Tamanho do lado direito(cima):") 
                quant_dej_dir=int(input(""))
                quant_dej = quant_dej+quant_dej_dir
            elif(comecar == "T es") or (comecar == "t es"):#esuquerda
                print("Esquerda(baixo):")
                quant_dej_es = int(input(""))
                quant_dej = quant_dej_es+quant_dej
            #Altura
            elif(comecar == "A") or (comecar == "a"):#geral
                print("Altura geral, isto é, para todos os lados da ondinha")
                altura = int(input(""))
                rigth_desj = altura
                left_des = altura
            elif(comecar == "A di") or (comecar == "a di"):
                print("Altura para o lado direito(parte de cima) da ondinha")
                rigth_desj = int(input(""))
            elif(comecar == "A es") or (comecar == "a es"):
                print("Altura do lado esquerdo, parte de baixo, da ondinha")
                left_des = int(input(""))
            #Suavidade
            elif(comecar == "S") or (comecar == "s"):#geral
                #Suavidade
                print("Suavidade geral(isto é, vai valer tanto para a direita quanto a esquerda). Digite S para sim e N para não")
                pro_ro = str(input(""))
                if(pro_ro == "S") or (pro_ro == "s"):
                    pro_ro = int(1)
                elif(pro_ro == "N") or (pro_ro == "n"):
                    pro_ro = int(0)
                else:
                    print("Inválido, digite novamente")
                    configuracoes = 0
                    configuracoes = 1
            elif(comecar == "S di") or (comecar == "s di"):#direito
                print("Suavidade do lado direito")
                pro_ro_di = str(input(""))
                if(pro_ro_di == "S") or (pro_ro_di == "s"):
                    pro_ro_di == 1
                elif(pro_ro_di == "N") or (pro_ro_di == "n"):
                    pro_ro_di == 0
                else:
                    print("Inválido, digite novamente")
                    configuracoes = 0
                    configuracoes = 1
            elif(comecar == "S es") or (comecar == "s es"):#esuqerdo
                print("Suavidade esquerda")
                pro_ro_es = str(input(""))
                if(pro_ro_es == "S") or (pro_ro_es == "s"):
                    pro_ro_es = int(1)
                elif(pro_ro_es == "N") or (pro_ro_es == "n"):
                    pro_ro_es = int(0)
                else:
                    print("Inválido, tente novamente")
                    configuracoes = 0
                    configuracoes = 1
            #Espaçamento
            elif(comecar == "E") or (comecar == "e"):
                print("Espaçamento")
                esp_des = int(input(""))
            #Números
            elif(comecar == "N m") or (comecar == "n m"):
                print("Número a ser multiplicado:")
                n = int(input(""))
            elif(comecar == "N di") or (comecar == "n di"):
                print("Divisor")
                n_di = int(input(""))
            elif(comecar == "C") or (comecar == "c"):
                print("Ciclo")
                ciclo_des = int(input(""))
            elif(comecar == "p"):
                #Valores para as ondas
                #Número
                n = int(10)# número desejado a ser multiplicado
                n_di = int(10)# número divisor
                #Quantidade desejada
                quant_dej_dir = int(40)#direita
                quant_dej_es = int(40)#esquerda
                #Total
                quant_dej = quant_dej_dir+quant_dej_es
                #Esquerda
                left_des = int(20)#esquerda desejada
                #Direita
                rigth_desj = int(20)#direita desejada
                #Espaçamento
                esp_des = int(10)
                #Suave|Robusto
                pro_ro = 0#geral
                #lados
                pro_ro_es = 0#esquerdo
                pro_ro_di = 0#direito
                #Ciclo
                ciclo_des = 2 
            elif(comecar == "l") or (comecar == "L"):
                print("#Valores para as ondas:", "\n", "\n", "Tamanhos", "\n", "Geral:", quant_dej, "\n", "Direita:", quant_dej_dir, "\n", "Esquerda:", quant_dej_es, "\n", "\n", "Altura", "\n", "Direita:", rigth_desj, "\n", "Esquerda:", left_des, "\n","\n", "\n", "Suavidade", "\n", "Geral:", pro_ro, "\n", "Lado direito:", pro_ro_di, "\n", "Lado esquerdo", pro_ro_es, "\n","\n", "Espaçamento", "\n", "Geral:", esp_des, "\n", "\n", "Número", "\n", "Divisor:", n_di, "\n", "Multiplicador:",  n, "\n", "\n", "Ciclo:", ciclo_des)
            elif(comecar == "f") or (comecar == "F"):
                configuracoes = 0
            else:
                print("Inválido, digite novamente")
    #Execução
    if(comecar == "C") or (comecar == "c"):
        ciclo = 0
        while(ciclo<ciclo_des):
            rigth_desj = rigth_armazenada
            quant = 0
            rigth = 0
            left = 0
            while(quant <quant_dej):
                if(orientador == 0):
                    proporcao = int(rigth_desj/quant_dej_dir)
                    if(rigth_desj>quant_dej):
                        rigth_desj = quant_dej
                    while(rigth <= rigth_desj) and (quant <= quant_dej_dir):
                        #Inicializador
                        if(quant == 0):
                            print(int(n))
                        #Ondinhas
                        def ondas(x):
                            if(proporcao<=1):
                                return x*(n**rigth)
                            elif(proporcao>1) and (rigth == 1):
                                return x*(n**proporcao)
                            elif(proporcao>1) and (rigth != 1):
                                return (x*armazenador_x)*(n**proporcao)
                        x = ondas(n)
                        armazenador_x = x
                        #Suave
                        if(pro_ro == 1):
                            if(quant % esp_des == 0) and (quant!= 0) or (quant!= quant_dej-1):
                                esp = 0
                                while(esp <= esp_des):
                                    print(x)
                                    esp = esp+1
                            else:
                                print(x)
                        #Caótico
                        elif(pro_ro == 0):
                            if(quant % esp_des == 0) and (quant != 0):
                                esp = 0
                                while(esp <= esp_des):
                                    #print(proporcao)
                                    print(x)
                                    esp = esp+1
                            else:
                                print(x)
                        rigth = rigth+1
                        quant = quant+1
                        if(rigth >= rigth_desj):
                            orientador = 1
                            quant = 0
                            armazenador_x = x
                            print(armazenador_x)
                #Esquerdo
                elif(orientador == 1):
                    while(left<left_des) and (quant<quant_dej_es):
                        def ondas_e(y):
                            return y/(n_di**left)
                        y = (ondas_e(armazenador_x))
                        #Contra tempo
                        #Progressível
                        if(pro_ro_es == 1) or (pro_ro == 1):
                            if(quant % esp_des == 0) and (quant != quant_dej) or (quant != quant_dej-1):
                                esp = 0
                                while(esp <= esp_des):
                                    #print(contar, ",", int(y))
                                    print(int(y))
                                    esp = esp+1
                            else:
                                print(int(y))
                        #Rpbusto
                        elif(pro_ro_es == 0) or (pro_ro == 0):
                            if(quant % esp_des == 0):
                                esp = 0
                                while(esp <= esp_des):
                                    print(int(y))
                                    esp = esp+1
                            else:
                                print(int(y))
                        quant = quant+1
                        left = left+1
                        contar = contar+1
                        if(left >= left_des):
                            orientador = 0
                quant=quant_dej
                #print(quant,"o" ,orientador, "r", rigth, "l", left)
                #print("Fim do ciclo")
            ciclo = ciclo+1
    mais_no = 1