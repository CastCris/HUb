#Modos
modo_ds = 1#modo desenvolvedor
#Renicialização
reniciar = 0
#Valores para as ondas
#Ciclo
section_ciclo = 1
ciclo_1_1 = 1
ciclo_1_2 = 0
ciclo_1_3 = 0
ciclo_1_4 = 0
ciclo_1_5 = 0
ciclo_1_6 = 0
#Repetidores
repet_ciclo_1_1 = 1
repet_ciclo_1_2 = 0
repet_ciclo_1_3 = 0
repet_ciclo_1_4 = 0
repet_ciclo_1_5 = 0
repet_ciclo_1_6 = 0
#Removedor
remover_1 = 0
repetidor = 0
depois = 1

ciclo = 0
ciclo_des = repet_ciclo_1_1+repet_ciclo_1_2+repet_ciclo_1_3+repet_ciclo_1_4+repet_ciclo_1_5+repet_ciclo_1_6
#Seção 1
#Quantidade desejada
quant_dej_dir_1_1 = 40
quant_dej_dir_1_2 = 0
quant_dej_dir_1_3 = 0
quant_dej_dir_1_4 = 0
quant_dej_dir_1_5 = 0
quant_dej_dir_1_6 = 0
#Largura
#Prohressiva
rigth_armazenada_1_1 = 40
rigth_armazenada_1_2 = 0
rigth_armazenada_1_3 = 0
rigth_armazenada_1_4 = 0
rigth_armazenada_1_5 = 0
rigth_armazenada_1_6 = 0
#Inicial
r_init_armazenada_1_1 = 1
r_init_armazenada_1_2 = 0
r_init_armazenada_1_3 = 0
r_init_armazenada_1_4 = 0
r_init_armazenada_1_5 = 0
r_init_armazenada_1_6 = 0
#Proporcional|Não porporcional
r_init_pro_ro = 1
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
sua_1_2 = 1
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
contagem_esp_armazenamento = int(0)
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
#Config
entra = 0
#Texto
text = 1
#Mais não!
vezes = 0
#Configurações
exibir_instrucoes = 1
configuracoes = 0
#Marcador
marcador_1 = 0
while (reniciar != 1):
    #Repetidor
    while(onda == 1):
        onda = 1
        configuracoes = 0
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
                print("")
                exibir_instrucoes = 0
            #Confiurações
            print("Digite a configuração desejada")
            ciclo_1_1 = 2
            entra = 0
            while(configuracoes == 1):
                #Ciclo
                ciclo_des = 0
                #Onda atual
                def onda_atual(atual):
                    if(ciclo_1_1 == 2):
                        return 1
                    elif(ciclo_1_2 == 2):
                        return 2
                    elif(ciclo_1_3 == 2):
                        return 3
                    elif(ciclo_1_4 == 2):
                        return 4
                    elif(ciclo_1_5 == 2):
                        return 5
                    elif(ciclo_1_6 == 2):
                        return 6
                o_atual = onda_atual(int())
                if(entra == 0):
                    print("Seção", section_ciclo, "Onda:", o_atual,)
                print("Digite as suas modificações")
                comecar = str(input(""))
                #Define onda
                #Seção
                if(comecar == "st") or (comecar == "St") or (comecar == "sT"):
                    print("Escolha uma seção padrão para as suas ondas:")
                    escolha_section = int(input(""))
                    def section(esc):
                        if(escolha_section == 1):
                            return 1
                        elif(escolha_section == 2):
                            return 2
                        elif(escolha_section == 3):
                            return 3
                    section_ciclo = section(int())
                #Onda
                #Adicionar e configurar
                #1
                elif(comecar == "o1"):
                    if(section_ciclo == 1):
                        ciclo_1_1 = 2
                        ciclo_1_2 = 0
                        ciclo_1_3 = 0
                        ciclo_1_4 = 0
                        ciclo_1_5 = 0
                        ciclo_1_6 = 0
                #2
                elif(comecar == "o2"):
                    if(section_ciclo == 1):
                        ciclo_1_1 = 0
                        ciclo_1_2 = 2
                        ciclo_1_3 = 0
                        ciclo_1_4 = 0
                        ciclo_1_5 = 0
                        ciclo_1_6 = 0
                #3
                elif(comecar == "o3"):
                    if(section_ciclo == 1):
                        ciclo_1_1 = 0
                        ciclo_1_2 = 0
                        ciclo_1_3 = 2
                        ciclo_1_4 = 0
                        ciclo_1_5 = 0
                        ciclo_1_6 = 0
                #4
                elif(comecar == "o4"):
                    if(section_ciclo == 1):
                        ciclo_1_1 = 0
                        ciclo_1_2 = 0
                        ciclo_1_3 = 0
                        ciclo_1_4 = 2
                        ciclo_1_5 = 0
                        ciclo_1_6 = 0
                #5
                elif(comecar == "o5"):
                    if(section_ciclo == 1):
                        ciclo_1_1 = 0
                        ciclo_1_2 = 0
                        ciclo_1_3 = 0
                        ciclo_1_4 = 0
                        ciclo_1_5 = 2
                        ciclo_1_6 = 0
                #6
                elif(comecar == "o6"):
                    if(section_ciclo == 1):
                        ciclo_1_1 = 0
                        ciclo_1_2 = 0
                        ciclo_1_3 = 0
                        ciclo_1_4 = 0
                        ciclo_1_5 = 0
                        ciclo_1_6 = 2
                #Repetidor
                elif(comecar == "o r") or (comecar == "O r"):
                    print("Repetido da Onda:", o_atual, "Seção", section_ciclo)
                    if(ciclo_1_1 == 2):
                        repet_ciclo_1_1 = int(input(""))
                    elif(ciclo_1_2 == 2):
                        repet_ciclo_1_2 = int(input(""))
                    elif(ciclo_1_3 == 2):
                        repet_ciclo_1_3 = int(input(""))
                    elif(ciclo_1_4 == 2):
                        repet_ciclo_1_4 = int(input(""))
                    elif(ciclo_1_5 == 2):
                        repet_ciclo_1_5 = int(input(""))
                    elif(ciclo_1_6 == 2):
                        repet_ciclo_1_6 = int(input(""))
                #Remover
                elif(comecar == "o-") or (comecar == "O-"):
                    escolha_onda_remover = int(input(""))
                    if(section_ciclo == 1):
                        #1
                        if(escolha_onda_remover == 1):
                            quant_dej_dir_1_1 = 0
                            repet_ciclo_1_1 = 0
                            remover_1 = 1
                        #2
                        elif(escolha_onda_remover == 2):
                            quant_dej_dir_1_2 = 0
                            repet_ciclo_1_2 = 0
                            remover_1 = 2
                        #3
                        elif(escolha_onda_remover == 3):
                            quant_dej_dir_1_3 = 0
                            repet_ciclo_1_3 = 0
                            remover_1 = 3
                        #4
                        elif(escolha_onda_remover == 4):
                            quant_dej_dir_1_4 = 0
                            repet_ciclo_1_4 = 0
                            remover_1 = 4
                        #5
                        elif(escolha_onda_remover == 5):
                            quant_dej_dir_1_5 = 0
                            repet_ciclo_1_5 = 0
                            remover_1 = 5
                        #6
                        elif(escolha_onda_remover == 6):
                            quant_dej_dir_1_6 = 0
                            repet_ciclo_1_6 = 0
                            remover_1 = 6
                #Comprimenoto
                elif(comecar == "T") or (comecar == "t"):
                    print("Tamanho da Onda", o_atual, "Seção:",section_ciclo)
                    if(section_ciclo == 1):
                        if(ciclo_1_1 == 2):
                            quant_dej_dir_1_1 = int(input(""))
                        elif(ciclo_1_2 == 2):
                            quant_dej_dir_1_2 = int(input(""))
                        elif(ciclo_1_3 == 2):
                            quant_dej_dir_1_3 = int(input(""))
                        elif(ciclo_1_4 == 2):
                            quant_dej_dir_1_4 = int(input(""))
                        elif(ciclo_1_5 == 2):
                            quant_dej_dir_1_5 = int(input(""))
                        elif(ciclo_1_6 == 2):
                            quant_dej_dir_1_6 = int(input(""))
                #Altura
                elif(comecar == "a") or (comecar == "A"):
                    print("Altura da Onda:", o_atual, "Seção", section_ciclo)
                    if(section_ciclo == 1):#S1
                        if(ciclo_1_1 == 2):#1
                            rigth_armazenada_1_1 = int(input(""))
                        elif(ciclo_1_2 == 2):#2
                            rigth_armazenada_1_2 = int(input(""))
                        elif(ciclo_1_3 == 2):#3
                            rigth_armazenada_1_3 = int(input(""))
                        elif(ciclo_1_4 == 2):#4
                            rigth_armazenada_1_4 = int(input(""))
                        elif(ciclo_1_5 == 2):#5
                            rigth_armazenada_1_5 = int(input(""))
                        elif(ciclo_1_6 == 2):#6
                            rigth_armazenada_1_6 = int(input(""))
                #Suavidade
                elif(comecar == "S") or (comecar == "s"):
                    print("Suavidade da Onda[S|N]:", o_atual, "Seção", section_ciclo)
                    if(section_ciclo == 1):
                        if(ciclo_1_1== 2):
                            sua_1_1 = str(input(""))
                            if(sua_1_1 == "S") or (sua_1_1 == "s"):
                                sua_1_1 = int(1)
                            elif(sua_1_1 == "N") or (sua_1_1 == "n"):
                                sua_1_1 = int(0)
                        elif(ciclo_1_2 == 2):
                            sua_1_2 = str(input(""))
                            if(sua_1_2 == "S") or (sua_1_2 == "s"):
                                sua_1_2 = int(1)
                            elif(sua_1_2 == "N") or (sua_1_2 == "n"):
                                sua_1_2 = int(0)
                        elif(ciclo_1_3 == 2):
                            sua_1_3 = str(input(""))
                            if(sua_1_3 == "S") or (sua_1_3 == "s"):
                                sua_1_3 = int(1)
                            elif(sua_1_3 == "N") or (sua_1_3 == "n"):
                                sua_1_3 = int(0)
                        elif(ciclo_1_4 == 2):
                            sua_1_4 = str(input(""))
                            if(sua_1_4 == "S") or (sua_1_4 == "s"):
                                sua_1_4 = int(1)
                            elif(sua_1_4 == "N") or (sua_1_4 == "n"):
                                sua_1_4 = int(0)
                        elif(ciclo_1_5 == 2):
                            sua_1_5 = str(input(""))
                            if(sua_1_5 == "S") or (sua_1_5 == "s"):
                                sua_1_5 = int(1)
                            elif(sua_1_5 == "N") or (sua_1_5 == "n"):
                                sua_1_5 = int(0)
                        elif(ciclo_1_6 == 2):
                            sua_1_6 = str(input(""))
                            if(sua_1_6 == "S") or (sua_1_6 == "s"):
                                sua_1_6 = int(1)
                            elif(sua_1_6== "N") or (sua_1_6 == "n"):
                                sua_1_6 = int(0)
                #Espaçamento
                elif(comecar == "e") or (comecar == "E"):
                    print("Espaçamento da Onda:", o_atual, "Seção", section_ciclo)
                    if(section_ciclo == 1):
                        if(ciclo_1_1 == 2):
                            esp_des_1_1 = int(input(""))
                        elif(ciclo_1_2 == 2):
                            esp_des_1_2 = int(input(""))
                        elif(ciclo_1_3 == 2):
                            esp_des_1_3 = int(input(""))
                        elif(ciclo_1_4 == 2):
                            esp_des_1_4 = int(input(""))
                        elif(ciclo_1_5 == 2):
                            esp_des_1_5 = int(input(""))
                        elif(ciclo_1_6 == 2):
                            esp_des_1_6 = int(input(""))
                #Números
                #Multiplico comum
                elif(comecar == "N m") or (comecar == "n M") or (comecar == "n m"):
                    print("Número a ser multiplicado por si mesmo, da Onda", o_atual, "Seção", section_ciclo)
                    if(section_ciclo == 1):
                        if(ciclo_1_1 == 2):
                            n_m_1 = int(input(""))
                            fator1_1_1 = n_m_1
                            fator2_1_1 = n_m_1
                        elif(ciclo_1_2 == 2):
                            n_m_1 = int(input(""))
                            fator1_1_2 = n_m_1
                            fator2_1_2 = n_m_1
                        elif(ciclo_1_3 == 2):
                            n_m_1 = int(input(""))
                            fator1_1_3 = n_m_1
                            fator2_1_3 = n_m_1
                        elif(ciclo_1_4 == 2):
                            n_m_1 = int(input(""))
                            fator1_1_4 = n_m_1
                            fator2_1_4 = n_m_1
                        elif(ciclo_1_5 == 2):
                            n_m_1 = int(input(""))
                            fator1_1_5 = n_m_1
                            fator2_1_5 = n_m_1
                        elif(ciclo_1_6 == 2):
                            n_m_1 = int(input(""))
                            fator1_1_6 = n_m_1
                            fator2_1_6 = n_m_1
                #Fatores
                #Fator1
                elif(comecar == "N m1") or (comecar == "n M1") or (comecar == "n m1"):
                    print("Multiplo 1 da Onda", o_atual, "Seção", section_ciclo)
                    if(section_ciclo == 1):
                        if(ciclo_1_1 ==2):
                            fator1_1_1 = int(input(""))
                        elif(ciclo_1_2 == 2):
                            fator1_1_2 = int(input(""))
                        elif(ciclo_1_3 == 2):
                            fator1_1_3 = int(input(""))
                        elif(ciclo_1_4 == 2):
                            fator1_1_4 = int(input(""))
                        elif(ciclo_1_5 == 2):
                            fator1_1_5 = int(input(""))
                        elif(ciclo_1_6 == 2):
                            fator1_1_6 = int(input(""))
                #Fator 2
                elif(comecar == "N m2") or (comecar == "n M2") or (comecar == "n m2"):
                    print("Multiplo 2 da Onda", o_atual, "Seção", section_ciclo)
                    if(section_ciclo == 1):
                        if(ciclo_1_1 == 2):
                            fator2_1_1 = int(input(""))
                        elif(ciclo_1_2 == 2):
                            fator2_1_2 = int(input(""))
                        elif(ciclo_1_3 == 2):
                            fator2_1_3 = int(input(""))
                        elif(ciclo_1_4 == 2):
                            fator2_1_4 = int(input(""))
                        elif(ciclo_1_5 == 2):
                            fator2_1_5 = int(input(""))
                        elif(ciclo_1_6 == 2):
                            fator2_1_6 = int(input(""))
                #Número divisor
                elif(comecar == "N d") or (comecar == "n D") or (comecar == "n d"):
                    print("Divisor da Onda", o_atual, ", Seção", section_ciclo)
                    if(section_ciclo == 1):
                        if(ciclo_1_1 == 2):
                            di_1_1 = int(input(""))
                        elif(ciclo_1_2 == 2):
                            di_1_2 = int(input(""))
                        elif(ciclo_1_3 == 2):
                            di_1_3 = int(input(""))
                        elif(ciclo_1_4 == 2):
                            di_1_4 = int(input(""))
                        elif(ciclo_1_5 == 2):
                            di_1_5 = int(input(""))
                        elif(ciclo_1_6 == 2):
                            di_1_6 = int(input(""))
                #Listagem
                #Local
                elif(comecar == "L") or (comecar == "l"):
                    print("Lista das configurações da onda atual:")
                    if(section_ciclo == 1):
                        print("\n", "==============","\n","Seção 1")
                        #1
                        if(ciclo_1_1 != 0):
                            print("Onda 1", "\n", "Tamanho:", quant_dej_dir_1_1, "\n","Altura:", rigth_armazenada_1_1,"\n", "Altura inicial:", r_init_armazenada_1_1, "\n", "Espaçamento:", esp_des_1_1, "\n", "Fatores:", "\n", "1:", fator1_1_1, "\n","2", fator2_1_1, "\n", "Divisor:", di_1_1, "\n", "Suavidade:", sua_1_1, "\n", "Repetição:", repet_ciclo_1_1)
                        #2
                        elif(ciclo_1_2 != 0):
                            print("Onda 2", "\n", "Tamanho:", quant_dej_dir_1_2, "\n","Altura:", rigth_armazenada_1_2,"\n", "Altura inicial:", r_init_armazenada_1_2, "\n", "Espaçamento:", esp_des_1_2, "\n", "Fatores:", "\n", "1:", fator1_1_2, "\n","2", fator2_1_2, "\n", "Divisor:", di_1_2, "\n", "Suavidade:", sua_1_2, "\n", "Repetição:", repet_ciclo_1_2)
                        #3
                        elif(ciclo_1_3 != 0):
                            print("Onda 3", "\n", "Tamanho:", quant_dej_dir_1_3, "\n","Altura:", rigth_armazenada_1_3, "\n", "Altura inicial:", r_init_armazenada_1_3, "\n", "Espaçamento:", esp_des_1_3, "\n", "Fatores:", "\n", "1:", fator1_1_3, "\n","2", fator2_1_3, "\n", "Divisor:", di_1_3, "\n", "Suavidade:", sua_1_3, "\n", "Repetição:", repet_ciclo_1_3)
                        #4
                        elif(ciclo_1_4 != 0):
                            print("Onda 4", "\n", "Tamanho:", quant_dej_dir_1_4, "\n","Altura:", rigth_armazenada_1_4,"\n", "Altura inicial:", r_init_armazenada_1_4, "\n", "Espaçamento:", esp_des_1_4, "\n", "Fatores:", "\n", "1:", fator1_1_4, "\n","2", fator2_1_4, "\n", "Divisor:", di_1_4, "\n", "Suavidade:", sua_1_4, "\n", "Repetição:", repet_ciclo_1_4)
                        #5
                        elif(ciclo_1_5 != 0):
                            print("Onda 5", "\n", "Tamanho:", quant_dej_dir_1_5, "\n","Altura:", rigth_armazenada_1_5,"\n", "Altura inicial:", r_init_armazenada_1_5 ,"\n", "Espaçamento:", esp_des_1_5, "\n", "Fatores:", "\n", "1:", fator1_1_5, "\n","2", fator2_1_5, "\n", "Divisor:", di_1_5, "\n", "Suavidade:", sua_1_5, "\n", "Repetição:", repet_ciclo_1_5)
                        #6
                        elif(ciclo_1_6 != 0):
                            print("Onda 6", "\n", "Tamanho:", quant_dej_dir_1_6, "\n","Altura:", rigth_armazenada_1_6,"\n", "Altura inicial:", r_init_armazenada_1_6,"\n", "Espaçamento:", esp_des_1_6, "\n", "Fatores:", "\n", "1:", fator1_1_6, "\n","2", fator2_1_6, "\n", "Divisor:", di_1_6, "\n", "Suavidade:", sua_1_6, "\n", "Repetição:", repet_ciclo_1_6)
                        print("==============", "\n")
                #Geral
                elif(comecar == "Lg") or (comecar == "lg"):
                    if(section_ciclo == 1):
                        print("\n", "==============","\n","Seção 1")
                        #1
                        if(quant_dej_dir_1_1 != 0):
                            print("Onda 1", "\n", "Tamanho:", quant_dej_dir_1_1, "\n""Altura:",    rigth_armazenada_1_1,"\n", "Altura inicial:",r_init_armazenada_1_1,   "\n", "Espaçamento:", esp_des_1_1, "\n","Fatores:", "\n", "1:",  fator1_1_1, "\n","2", fator2_1_1, "\n","Divisor:", di_1_1, "\n",    "Suavidade:", sua_1_1, "\n","Repetição:", repet_ciclo_1_1)
                        #2
                        if(quant_dej_dir_1_2 != 0):
                            print("Onda 2", "\n", "Tamanho:", quant_dej_dir_1_2, "\n""Altura:",    rigth_armazenada_1_2,"\n", "Altura inicial:",r_init_armazenada_1_2,   "\n", "Espaçamento:", esp_des_1_2, "\n","Fatores:", "\n", "1:",  fator1_1_2, "\n","2", fator2_1_2, "\n","Divisor:", di_1_2, "\n",    "Suavidade:", sua_1_2, "\n","Repetição:", repet_ciclo_1_2)
                        #3
                        if(quant_dej_dir_1_3 != 0):
                            print("Onda 3", "\n", "Tamanho:", quant_dej_dir_1_3, "\n""Altura:",    rigth_armazenada_1_3, "\n", "Altura inicial:",r_init_armazenada_1_3,  "\n", "Espaçamento:", esp_des_1_3, "\n","Fatores:", "\n", "1:",     fator1_1_3, "\n","2", fator2_1_3, "\n","Divisor:", di_1_3, "\n",   "Suavidade:", sua_1_3, "\n","Repetição:", repet_ciclo_1_3)
                        #4
                        if(quant_dej_dir_1_4 != 0):
                            print("Onda 4", "\n", "Tamanho:", quant_dej_dir_1_4, "\n""Altura:",    rigth_armazenada_1_4,"\n", "Altura inicial:",r_init_armazenada_1_4,   "\n", "Espaçamento:", esp_des_1_4, "\n","Fatores:", "\n", "1:",  fator1_1_4, "\n","2", fator2_1_4, "\n","Divisor:", di_1_4, "\n",    "Suavidade:", sua_1_4, "\n","Repetição:", repet_ciclo_1_4)
                        #5
                        if(quant_dej_dir_1_5 != 0):
                            print("Onda 5", "\n", "Tamanho:", quant_dej_dir_1_5, "\n""Altura:",    rigth_armazenada_1_5,"\n", "Altura inicial:",r_init_armazenada_1_5 ,  "\n", "Espaçamento:", esp_des_1_5, "\n","Fatores:", "\n", "1:",  fator1_1_5, "\n","2", fator2_1_5, "\n","Divisor:", di_1_5, "\n",    "Suavidade:", sua_1_5, "\n","Repetição:", repet_ciclo_1_5)
                        #6
                        if(quant_dej_dir_1_6 != 0):
                            print("Onda 6", "\n", "Tamanho:", quant_dej_dir_1_6, "\n""Altura:",    rigth_armazenada_1_6,"\n", "Altura inicial:",r_init_armazenada_1_6,   "\n", "Espaçamento:", esp_des_1_6, "\n","Fatores:", "\n", "1:",   fator1_1_6, "\n","2", fator2_1_6, "\n","Divisor:", di_1_6, "\n",     "Suavidade:", sua_1_6, "\n","Repetição:", repet_ciclo_1_6)
                        print("==============", "\n")
                #Dúvida
                elif(comecar == "?"):
                    print("Seção:", section_ciclo, "Onda:", o_atual)
                #Finalização
                elif(comecar == "f") or (comecar == "F"):
                    ciclo_des = repet_ciclo_1_1+repet_ciclo_1_2+repet_ciclo_1_3+repet_ciclo_1_4+repet_ciclo_1_5+repet_ciclo_1_6
                    ciclo_1_1 = 1
                    if(ciclo_1_2 != 0):
                        ciclo_1_2 = 0
                    elif(ciclo_1_3 != 0):
                        ciclo_1_3 = 0
                    elif(ciclo_1_4 != 0):
                        ciclo_1_4 = 0
                    elif(ciclo_1_5 != 0):
                        ciclo_1_5 = 0
                    elif(ciclo_1_6 != 0):
                        ciclo_1_6 = 0
                    configuracoes = 2
                #Modo DS
                elif(comecar == "ds") or (comecar == "Ds"):
                    print("Como você descobriu aqui !!!???")
                    modo_ds = int(input(""))
                #Altura Inicial
                elif(comecar == "ai") or (comecar == "Ai") or (comecar == "AI!"):
                    print("Digite a altura inicicial de sua onda")
                    if(ciclo_1_1 == 2):
                        r_init_armazenada_1_1 = int(input(""))
                    elif(ciclo_1_2 == 2):
                        r_init_armazenada_1_2 = int(input(""))
                    elif(ciclo_1_3 == 2):
                        r_init_armazenada_1_3 = int(input(""))
                    elif(ciclo_1_4 == 2):
                        r_init_armazenada_1_4 = int(input(""))
                    elif(ciclo_1_5 == 2):
                        r_init_armazenada_1_5 = int(input(""))
                    elif(ciclo_1_6 == 2):
                        r_init_armazenada_1_6 = int(input(""))
                #Erro
                else:
                    print("Inválido, tente novamente")
                entra = entra+1
            if(configuracoes == 2):
                comecar = str(input(""))
        #Execução   
        if(comecar == "C") or (comecar == "c"):            
            ciclo = 0
            while(ciclo<ciclo_des):
                depois = 1
                contagem_esp_armazenamento = 0
                #Comprimento
                def onda_quant(quant):
                    if( section_ciclo == 1):
                        if(ciclo_1_1 == 1) and (remover_1 != 1):
                            return quant_dej_dir_1_1
                        elif(ciclo_1_2 == 1) and (remover_1 != 2):
                            return quant_dej_dir_1_2
                        elif(ciclo_1_3 == 1) and (remover_1 != 3):
                            return quant_dej_dir_1_3
                        elif(ciclo_1_4 == 1) and (remover_1 != 4):
                            return quant_dej_dir_1_4
                        elif(ciclo_1_5 == 1) and (remover_1 != 5):
                            return quant_dej_dir_1_5
                        elif(ciclo_1_6 == 1) and (remover_1 != 6):
                            return quant_dej_dir_1_5
                quant_armazenada = onda_quant(int())
                #Largura
                #Absoluta
                def onda_d(d):
                    if(section_ciclo == 1):
                        if(ciclo_1_1 == 1):
                            return rigth_armazenada_1_1
                        elif(ciclo_1_2 == 1):
                            return rigth_armazenada_1_2
                        elif(ciclo_1_3 == 1):
                            return rigth_armazenada_1_3
                        elif(ciclo_1_4 == 1):
                            return rigth_armazenada_1_4
                        elif(ciclo_1_5 == 1):
                            return rigth_armazenada_1_5
                        elif(ciclo_1_6 == 1):
                            return rigth_armazenada_1_6
                rigth_armazenada = onda_d(int())
                #Relativa(?)
                def onda_d_inicial(di):
                    if(ciclo_1_1 == 1):
                        return r_init_armazenada_1_1
                    elif(ciclo_1_2 == 1):
                        return r_init_armazenada_1_2
                    elif(ciclo_1_3 == 1):
                        return r_init_armazenada_1_3
                    elif(ciclo_1_4 == 1):
                        return r_init_armazenada_1_4
                    elif(ciclo_1_5 == 1):
                        return r_init_armazenada_1_5
                    elif(ciclo_1_6 == 1):
                        return r_init_armazenada_1_6
                rigth_inicial_armazenada = onda_d_inicial(int())
                #Espaçamento
                def onda_esp(esp):
                    if( section_ciclo == 1):
                        if(ciclo_1_1 == 1):
                            return esp_des_1_1
                        elif(ciclo_1_2 == 1):
                            return esp_des_1_2
                        elif(ciclo_1_3 == 1):
                            return esp_des_1_3
                        elif(ciclo_1_4 == 1):
                            return esp_des_1_4
                        elif(ciclo_1_5 == 1):
                            return esp_des_1_5
                        elif(ciclo_1_6 == 1):
                            return esp_des_1_6
                esp_armazenado = onda_esp(int())
                #Número
                #Fatores
                def onda_fato1(f1):
                    if(section_ciclo == 1):
                        if(ciclo_1_1 == 1):
                            return fator1_1_1
                        elif(ciclo_1_2 == 1):
                            return fator1_1_2 
                        elif(ciclo_1_3 == 1):
                            return fator1_1_3 
                        elif(ciclo_1_4 == 1):
                            return fator1_1_4 
                        elif(ciclo_1_5 == 1):
                            return fator1_1_5 
                        elif(ciclo_1_6 == 1):
                            return fator1_1_6 
                fator1_armazenado = onda_fato1(int())
                def onda_fato2(f2):
                    if(section_ciclo == 1):
                        if(ciclo_1_1 == 1):
                            return fator2_1_1
                        elif(ciclo_1_2 == 1):
                            return fator2_1_2 
                        elif(ciclo_1_3 == 1):
                            return fator2_1_3 
                        elif(ciclo_1_4 == 1):
                            return fator2_1_4 
                        elif(ciclo_1_5 == 1):
                            return fator2_1_5 
                        elif(ciclo_1_6 == 1):
                            return fator2_1_6 
                fator2_armazenado = onda_fato2(int())
                def onda_di(divisor):#Número divisor
                    if(section_ciclo == 1):
                        if(ciclo_1_1 == 1):
                            return di_1_1
                        elif(ciclo_1_2 == 1):
                            return di_1_2
                        elif(ciclo_1_3 == 1):
                            return di_1_3
                        elif(ciclo_1_4 == 1):
                            return di_1_4
                        elif(ciclo_1_5 == 1):
                            return di_1_5
                        elif(ciclo_1_6 == 1):
                            return di_1_6
                di_armazenado = onda_di(int())
                def onda_suave(su):
                    if(section_ciclo == 1):
                        if(ciclo_1_1 == 1):
                            return sua_1_1
                        elif(ciclo_1_2 == 1):
                            return sua_1_2
                        elif(ciclo_1_3 == 1):
                            return sua_1_3
                        elif(ciclo_1_4 == 1):
                            return sua_1_4
                        elif(ciclo_1_5 == 1):
                            return sua_1_5
                        elif(ciclo_1_6 == 1):
                            return sua_1_6
                pro_ro_armazenamento = onda_suave(int())
                #DS
                if(modo_ds == 1):
                    print("Quant:", quant_armazenada, "\n", "R:", rigth_armazenada, "\n",  "E:", esp_armazenado,"\n", "Fatores", "\n", "1:", fator1_armazenado, "\n", "2:", fator2_armazenado)
                    if(section_ciclo == 1):
                        if(ciclo_1_1 == 1):
                            print("Onda 1")
                        elif(ciclo_1_2 == 1):
                            print("Onda 2")
                        elif(ciclo_1_3 == 1):
                            print("Onda 3")
                        elif(ciclo_1_4 == 1):
                            print("Onda 4")
                        elif(ciclo_1_5 == 1):
                            print("Onda 5")
                        elif(ciclo_1_6 == 1):
                            print("Onda 6")
                #Comprimento
                quant_dej_dir = quant_armazenada
                #Largura
                #Progressiva
                rigth_desj = rigth_armazenada
                #Cortada
                rigth_inical = rigth_inicial_armazenada
                #Espaçamento
                esp_des = esp_armazenado
                #Fatores
                fator1 = fator1_armazenado
                fator2 = fator2_armazenado
                #Suavidade
                pro_ro = pro_ro_armazenamento
                contagem_esp = 0
                quant = 0
                rigth = 0
                rigth_tot = 9
                #X
                X = fator1_armazenado
                #Armazenadores
                armazenador_x = 1
                armazenador_x_2 = 0
                #Sequência
                #Coração do sistema
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
                            proporcao = int(1)
                            resto = 1/resto_prop
                            esp_des = esp_des*resto
                            if(esp_des - int(esp_des) >=5):
                                esp_des = esp_des+1
                            else:
                                esp_des = int(esp_des)
                            if(modo_ds == 1):
                                print("P", proporcao ,"Res", resto, "Esp", esp_des)
                    #Para proporção grande
                    if(rigth_armazenada>quant_dej_dir):
                        rigth_desj = quant_dej_dir
                    #Para proporção pequena
                    elif(quant_armazenada>rigth_armazenada):
                        quant_dej_dir = rigth_armazenada
                    #Valor inicial da altura
                    if(rigth_inical != 1):
                        fator21 = fator2
                    else:
                        fator21 = 1
                    #Altura total
                    rigth_tot = fator1*(fator2**rigth_armazenada)
                    print("RT:", rigth_tot)
                    #Ondas
                    while(rigth <= rigth_desj) or (quant <= quant_dej_dir):
                        #X futuro
                        armazenador_x_fut = (fator1*fator21**rigth_inical)*(fator2**((rigth+1)*proporcao))
                        print("ARF:", armazenador_x_fut)
                        #Inicializador
                        if(quant<=0) and (rigth_inical == 1):
                            print(int(fator1))
                        #Ondinhas
                        def ondas(x):
                            if(proporcao>=1):
                                if(rigth_desj>=rigth) and (armazenador_x_fut<=rigth_tot):
                                    if(modo_ds == 1):
                                        print("RD!")
                                    return (x*fator21**rigth_inical)*(fator2**(rigth*proporcao))
                                elif(rigth_desj<=rigth):
                                    if(modo_ds == 1):
                                        print("RD2", rigth_desj)
                                    return armazenador_x_2
                                elif(armazenador_x_fut>=rigth_tot):
                                    if(modo_ds == 1):
                                        print("RT")
                                    return rigth_tot
                        X = ondas(fator1)
                        if(X != None):
                            armazenador_x = X
                        armazenador_x_2 = armazenador_x
                        #Exibirdores
                        #Suave
                        if(pro_ro == 1):
                            if(quant % esp_des == 0) and (quant!= 0) or (quant!= quant_dej_dir-1):
                                esp = 0
                                while(esp < esp_des):
                                    contagem_esp = 0
                                    if(modo_ds == 1):
                                        print("Q", quant, "E", contagem_esp_armazenamento, X,  "\n", "Suave, sim")
                                    else:
                                        print(X)
                                    contagem_esp = 1
                                    contagem_esp_armazenamento = contagem_esp+contagem_esp_armazenamento
                                    esp = esp+1
                            else:
                                if(modo_ds == 1):
                                    print("Q", quant, X, "\n", "Suave, não")
                                else:
                                    print(X)
                        #Caótico
                        elif(pro_ro == 0):
                            if(quant % esp_des == 0) and (quant != 0):
                                esp = 0
                                while(esp < esp_des):
                                    if(modo_ds == 1):
                                        print("Q", quant, "E", esp, X, "Não suave sim")
                                    else:
                                        print(X)
                                    esp = esp+1
                            else:
                                if(modo_ds == 1):
                                    print("Q", quant, X, "Não suave não")
                                else:
                                    print(X)
                            rigth = rigth+1
                        quant = quant+1
                        rigth = rigth+1
                        if(rigth >= rigth_desj):
                            armazenador_x = X
                            # print(armazenador_x)
                ciclo = ciclo+1
                if(section_ciclo == 1):
                    #1
                    if(repetidor<=repet_ciclo_1_1) and (depois == 1):
                        if(modo_ds == 1):
                            print("Certo", "R1", repet_ciclo_1_1, "Rep", repetidor)
                        repetidor = repetidor+1
                        if(repetidor == repet_ciclo_1_1):
                            if(quant_dej_dir_1_2 != 0):
                                if(modo_ds == 1):
                                    print("1/2", "Rep", repetidor)
                                ciclo_1_1 = 0
                                ciclo_1_2 = 1
                                depois = 2
                            else:
                                ciclo_1_1 = 1
                            repetidor = 0
                    #2
                    elif(repetidor<=repet_ciclo_1_2) and (depois == 2):
                        if(modo_ds == 1):
                            print("Certo2", "R2", repet_ciclo_1_2, "Rep", repetidor, "\n""Q",      quant_dej_dir_1_2)
                        repetidor = repetidor+1
                        if(repetidor == repet_ciclo_1_2):
                            if(quant_dej_dir_1_3 != 0):
                                ciclo_1_3 = 1
                                depois = 3
                            else:
                                ciclo_1_1 = 1
                                depois = 1
                            ciclo_1_2 = 0
                            repetidor = 0
                    #3
                    elif(repetidor<=repet_ciclo_1_3) and (depois == 3):
                        if(modo_ds == 1):
                            print("Certo3", "R3", repet_ciclo_1_3, "Rep", repetidor)
                        repetidor = repetidor+1
                        if(repetidor == repet_ciclo_1_3):
                            if(quant_dej_dir_1_4 != 0):
                                ciclo_1_4 = 1
                                depois = 4
                            else:
                                ciclo_1_1 = 1
                                depois = 1
                            ciclo_1_3 = 0
                            repetidor = 0
                    #4
                    elif(repetidor<=repet_ciclo_1_4) and (depois == 4):
                        if(modo_ds == 1):
                            print("Certo4", "R4", repet_ciclo_1_4, "Rep", repetidor)
                        repetidor = repetidor+1
                        if(repetidor == repet_ciclo_1_4):
                            if(quant_dej_dir_1_5 != 0):
                                ciclo_1_5 = 1
                                depois = 5
                            else:
                                ciclo_1_1 = 1
                                depois = 1
                            ciclo_1_4 = 0
                            repetidor = 0
                    #5
                    elif(repetidor<=repet_ciclo_1_5) and (depois == 5):
                        if(modo_ds == 1):
                            print("Certo5", "R5", repet_ciclo_1_5, "Rep", repetidor)
                        repetidor = repetidor+1
                        if(repetidor == repet_ciclo_1_5):
                            if(quant_dej_dir_1_6 != 0):
                                ciclo_1_6 = 1
                                depois = 6
                            else:
                                ciclo_1_1 = 1
                                depois = 1
                            ciclo_1_5 = 0
                            repetidor = 0
                    #6
                    elif(repetidor<=repet_ciclo_1_6) and (depois == 6):
                        if(modo_ds == 1):
                            print("Certo6", "R6", repet_ciclo_1_6, "Rep", repetidor)
                        repetidor = repetidor+1
                        if(repetidor == repet_ciclo_1_4):
                            ciclo_1_1 = 1
                            depois =1
                            ciclo_1_6 = 0
                            repetidor = 0
        vezes = vezes+1
        print("V", vezes)
        print("O", onda)
        text = 1
#Coisas para mexer aqui:
#1- Espaçamento, instável - Estável agora, check
#2- Criar padrões com utilizando as section_ciclos
#3- Criar outros tipos de ondas:
#   Divisão
#   Subtração
#   Raízes
#   Adição
#   Exponenciação
#4- Integra cálculo as ondas
#5- Altura inicial personalisável - Fase de testes
#6- Mensagens de introdução