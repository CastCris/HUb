#Modos
modo_ds = 1#modo desenvolvedor
#Renicialização
reniciar = 0
#Valores para as ondas
#Ciclo
section_ciclo = 1
ciclo_1 = 1
ciclo = 0
ciclo_des = 1
#Seção 1
#Quantidade desejada
quant_dej_dir_1_1 = 40
quant_dej_dir_1_2 = 0
quant_dej_dir_1_3 = 0
quant_dej_dir_1_4 = 0
quant_dej_dir_1_5 = 0
quant_dej_dir_1_6 = 0
#Largura
rigth_armazenada_1_1 = 90
rigth_armazenada_1_2 = 0
rigth_armazenada_1_3 = 0
rigth_armazenada_1_4 = 0
rigth_armazenada_1_5 = 0
rigth_armazenada_1_6 = 0
#Espaçamento
esp_des_1_1 = 2
esp_des_1_2 = 0
esp_des_1_3 = 0
esp_des_1_4 = 0
esp_des_1_5 = 0
esp_des_1_6 = 0
#Fator 1
fator1_1_1 = 10
fator1_1_2 = 0
fator1_1_3 = 0
fator1_1_4 = 0
fator1_1_5 = 0
fator1_1_6 = 0
#Fator 2
fator2_1_1 = 10
fator2_1_2 = 0
fator2_1_3 = 0
fator2_1_4 = 0
fator2_1_5 = 0
fator2_1_6 = 0
#Divisor
di_1_1 = 10
di_1_2 = 0
di_1_3 = 0
di_1_4 = 0
di_1_5 = 0
di_1_6 = 0
#Suavidade
sua_1_1 = 1
sua_1_2 = 0
sua_1_3 = 0
sua_1_4 = 0
sua_1_5 = 0
sua_1_6 = 0
#Número
fator1 = int(10)# número desejado a ser multiplicado
fator2 = int(10)# número desejado a ser multiplicado pelo fator1_di
n_di = int(10)# número divisor
armazenador_x = int(1)#Armazenador do x
n_flutuante = int(0)
n_flutuante_exibir = n_flutuante
#Vezes que o resto_pro repete
multpli = int(1)
#Quantidade
quant = int(1)
#Quantidade desejada
#Largura
quant_dej_dir = int(1)#direita
#Total
quant_dej = quant_dej_dir
#Direita
rigth = int(1)#direita marcadora
rigth_desj = int(1)#direita desejada
#Espaçamento
esp = int(1)
esp_des = int(1)
contagem_esp = int(0)#contagem esp
#Suava|Robusto
pro_ro = 1#geral
pro_ro_exibir = pro_ro
#lados
pro_ro_es = 0#esquerdo
pro_ro_es_exibir = pro_ro_es
pro_ro_di = 0#direito
pro_ro_di_exibir = pro_ro_di
#Outros
#Incializador
onda = 1
#Texto
text = 1
#Mais não!
vezes = 0
#Configurações
exibir_instrucoes = 1
configuracoes = 0
while (reniciar != 1):
    #Repetidor
    while(onda == 1):
        onda = 1
        #Texto
        while(text == 1):
            #Início
            if(vezes<1):
                print("Olá, bem_vindo ao ondinhas.com!","\n" ,"Aqui você pode, como deve ter presumido,fazer  ondinhas dos mais variáveis jeitos, deste de suaves á ondas ígrimes ou, até, verdadeiras tempestades, além de poder personalisa-lás.", "\n", "Caso queira ver o projeto de uma vez, apenas pressione c no termianal! Porém, caso queria mudar alguma das  configurações das ondas, sinta-se a vontade para fazer isso. Apenas digite config e faça as suas mudanças")
            elif(vezes != 0):
                if(vezes<2):
                    print("Gostou do programinnhas? Não importa, para ser franco contigo, não tem como  enviar feedback XD, por enquanto...", "\n", "Entretanto, como toda via, você pode repetir quantas vezes quiser, apenas digite 'C' logo abixo e, claro, se quiser fazer alguma mudança, digite confing")
            comecar = str(input(""))
            if(comecar == "config"):
                configuracoes = 1
                text = 0
            elif(comecar == "c") or (comecar == "C"):
                text = 0
            else:
                print("Inválido, tente novamente")
        while(configuracoes == 1):
            if(exibir_instrucoes == 1):
                print("\n" ,"Por padrão elas vem com as seguintes configurações:", "\n", "O valor da Largura(a quantidade total de linhas que as duas ondinha, junta, terão) é de cerca de 80 linhas", "\n", "Já a sua altura(ou peenchimento) é de cerca de 20 digitos em ambos os lados","\n", "O valor do espaçamento é 6", "\n", "A suavidade geral está  ativida ativada", "\n", "As ondas se repentem em 2 ciclo(um ciclo para cada lado)", "\n","E, para finalizar, o número padrão para ser multiplicado é o 10 o qual será multiplicado por ele mesmo, sendo também o divisor. Além disso, o número não é quebrado, ou, em termos técnicos, dicimal","\n", "Para modifica-lás digite logo abaixo o nome da configuração que quer modificar, sendo:","\n", "'T' para o tamanho", "\n","'A' para preenchimento","\n","'S' para a suavidade", "\n", "'E' para selecionar o espaçamento","\n", "'C' para  ciclo", "\n","'N'[m|m1|m2|di|que], sendo:[m] para escolher, igaulemente, os fatoes, [m1] para multiplicar algum número por [m2], [di] para  escolher o divisor e [que] para escolher se o número será decimal","\n","\n","Caso queira voltar ao velho padrão, digite 'P' na linha de comando", "\n", "Assim como: caso queria confirmar as configurações digite: 'F', e para listar as configurações, digite: 'L'", "\n", "Nota: caso queira ser mais específico na hora da aplicação, digite, exceto no C, as opações di/es para configurar os valores do lado direito/esquerdo e número respectivo. Se prescisar de ajuda, digite 'H' logo baixo", "\n", "Agora é você definirá as confiurações aqui, não eu mais, desenvolvedor...")
                exibir_instrucoes = 0
            #Confiurações
            while(configuracoes == 1):
                print("Nada ainda")
        #Execução
        if(comecar == "C") or (comecar == "c"):            
                #Comprimento
            def onda_quant(quant):
                if( section_ciclo == 1):
                    if(ciclo_1 == 1):
                        return quant_dej_dir_1_1
                    elif(ciclo_1 == 2):
                        return quant_dej_dir_1_2
                    elif(ciclo_1 == 3):
                        return quant_dej_dir_1_3
                    elif(ciclo_1 == 4):
                        return quant_dej_dir_1_4
                    elif(ciclo_1 == 5):
                        return quant_dej_dir_1_5
                    elif(ciclo_1 == 6):
                        return quant_dej_dir_1_5
            quant_armazenada = onda_quant(int())
            #Largura
            def onda_d(d):
                if( section_ciclo == 1):
                    if(ciclo_1 == 1):
                        return rigth_armazenada_1_1
                    elif(ciclo_1 == 2):
                        return rigth_armazenada_1_2
                    elif(ciclo_1 == 3):
                        return rigth_armazenada_1_3
                    elif(ciclo_1 == 4):
                        return rigth_armazenada_1_4
                    elif(ciclo_1 == 5):
                        return rigth_armazenada_1_5
                    elif(ciclo_1 == 6):
                        return rigth_armazenada_1_6
            rigth_armazenada = onda_d(int())
            #Espaçamento
            def onda_esp(esp):
                if( section_ciclo == 1):
                    if(ciclo_1 == 1):
                        return esp_des_1_1
                    elif(ciclo_1 == 2):
                        return esp_des_1_2
                    elif(ciclo_1 == 3):
                        return esp_des_1_3
                    elif(ciclo_1 == 4):
                        return esp_des_1_4
                    elif(ciclo_1 == 5):
                        return esp_des_1_5
                    elif(ciclo_1 == 6):
                        return esp_des_1_6
            esp_armazenado = onda_esp(int())
            #Número
            #Fatores
            def onda_fato1(f1):
                if(section_ciclo == 1):
                    if(ciclo_1 == 1):
                        return fator1_1_1
                    elif(ciclo_1 == 2):
                        return fator1_1_2 
                    elif(ciclo_1 == 3):
                        return fator1_1_3 
                    elif(ciclo_1 == 4):
                        return fator1_1_4 
                    elif(ciclo_1 == 5):
                        return fator1_1_5 
                    elif(ciclo_1 == 6):
                        return fator1_1_6 
            fator1_armazenado = onda_fato1(int())
            def onda_fato2(f1):
                if(section_ciclo == 1):
                    if(ciclo_1 == 1):
                        return fator2_1_1
                    elif(ciclo_1 == 2):
                        return fator2_1_2 
                    elif(ciclo_1 == 3):
                        return fator2_1_3 
                    elif(ciclo_1 == 4):
                        return fator2_1_4 
                    elif(ciclo_1 == 5):
                        return fator2_1_5 
                    elif(ciclo_1 == 6):
                        return fator2_1_6 
            fator2_armazenado = onda_fato2(int())
            def onda_di(divisor):#Número divisor
                if(section_ciclo == 1):
                    if(ciclo_1 == 1):
                        return di_1_1
                    elif(ciclo_1 == 2):
                        return di_1_2
                    elif(ciclo_1 == 3):
                        return di_1_3
                    elif(ciclo_1 == 4):
                        return di_1_4
                    elif(ciclo_1 == 5):
                        return di_1_5
                    elif(ciclo_1 == 6):
                        return di_1_6
            di_armazenado = onda_di(int())
            def onda_suave(su):
                if(section_ciclo == 1):
                    if(ciclo_1 == 1):
                        return sua_1_1
                    elif(ciclo_1 == 2):
                        return sua_1_2
                    elif(ciclo_1 == 3):
                        return sua_1_3
                    elif(ciclo_1 == 4):
                        return sua_1_4
                    elif(ciclo_1 == 5):
                        return sua_1_5
                    elif(ciclo_1 == 6):
                        return sua_1_6
            pro_ro_armazenamento = onda_suave(int())
            ciclo = 0
            while(ciclo<ciclo_des):
                #Comprimento
                quant_dej_dir = quant_armazenada
                print("Quant:", quant_dej_dir)
                #Largura
                rigth_desj = rigth_armazenada
                print("R", rigth_desj)
                #Espaçamento
                esp_des = esp_armazenado
                print("E",esp_des)
                #Fatores
                fator1 = fator1_armazenado
                fator2 = fator2_armazenado
                print("Fatores:", "\n", "1", fator1, "\n", "2", fator2)
                contagem_esp = 0
                quant = 0
                rigth = 0
                while(quant < quant_dej_dir):
                    #Onda
                    #Proporção
                    proporcao = float(rigth_desj/quant_dej_dir)
                    #Flutuante
                    if(n_flutuante == 1):
                        proporcao = float(rigth_desj/quant_dej_dir)
                    #Não fluante
                    elif(n_flutuante == 0):
                        #Proporcão nomral|grande
                        if(proporcao >= 1):
                                #Aproximação
                                aproxi_b_d = int(proporcao)
                                aproxi_a_d = int(proporcao)+1
                                if(aproxi_a_d-proporcao < proporcao-aproxi_b_d):
                                    if(modo_ds == 1):
                                        print("1",aproxi_a_d-proporcao)
                                    proporcao = aproxi_a_d
                                elif(proporcao-aproxi_b_d < aproxi_a_d-proporcao):
                                    if(modo_ds == 1):
                                        print("2",proporcao-aproxi_b_d)
                                    proporcao = aproxi_b_d
                                else:
                                    proporcao = int(proporcao)
                                if(modo_ds == 1):
                                    print("P" ,proporcao)
                                    print("P+1", aproxi_a_d)
                                    print("P-1", aproxi_b_d)
                        #Proporção pequena
                        else:
                            resto_prop = proporcao
                            if(modo_ds == 1):
                                print("P", proporcao ,"Res", resto_prop)
                            proporcao = int(1)
                            while(resto_prop<1):
                                resto_prop = resto_prop+resto_prop
                                multpli = multpli+1
                                if(resto_prop>=1):
                                    esp_des = esp_des*multpli
                                    #Aproximação
                                    aproxi_esp_dej_b_di = int(esp_des)#Menos
                                    aproxi_esp_dej_a_di = int(esp_des)+1#Mais
                                    if(aproxi_esp_dej_a_di -esp_des<esp_des-aproxi_esp_dej_b_di):
                                        esp = aproxi_esp_dej_a_di
                                    elif(esp_des-aproxi_esp_dej_b_di<aproxi_esp_dej_a_di-esp_des):
                                        esp=aproxi_esp_dej_b_di
                                    else:
                                        esp_des = int(esp_des)
                                    if(modo_ds == 1):
                                        print("esp_des",esp_des)
                    if(rigth_armazenada>quant_dej):
                        rigth_desj = quant_dej
                    #Onda direita
                    while(rigth <= rigth_desj) or (quant <= quant_dej_dir):
                        #Inicializador
                        if(quant == 0):
                            print(int(fator1))
                        #Ondinhas
                        def ondas(x):
                            if(proporcao>=1):
                                return x*((fator2**rigth)**proporcao)
                        x = ondas(fator1)
                        armazenador_x = x
                        #Suave
                        if(pro_ro == 1) or (pro_ro_di == 1):
                            if(quant % esp_des == 0) and (quant!= 0) or (quant!= quant_dej-1):
                                contagem_esp = esp+contagem_esp
                                esp = 0
                                while(esp <= esp_des):
                                    esp = esp+1
                                    if(modo_ds == 1):
                                        print("Q", quant, "E", contagem_esp ,x)
                                    else:
                                        print(x)
                            else:
                                if(modo_ds == 1):
                                    print("Q", quant ,x)
                                else:
                                    print(x)
                        #Caótico
                        elif(pro_ro == 0):
                            if(quant % esp_des == 0) and (quant != 0):
                                esp = 0
                                while(esp <= esp_des):
                                    if(modo_ds == 1):
                                        print("Q", quant, "E", esp ,x, )
                                    else:
                                        print(x)
                                    esp = esp+1
                            else:
                                if(modo_ds == 1):
                                    print("Q", quant, x)
                                else:
                                    print(x)
                        rigth = rigth+1
                        quant = quant+1
                        if(rigth >= rigth_desj):
                            armazenador_x = x
                            print(armazenador_x)
                ciclo = ciclo+1
        vezes = vezes+1
        print("V", vezes)
        print("O", onda)
        text = 1
