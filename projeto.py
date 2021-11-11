import time

print("Você é Natan, 23 anos, um perito criminal investigando um caso na PUCPR")
#time.sleep(2)
print("Ao chegar no prédio principal, você repara no saguão: uma sala grande, com uma escada dupla no centro, uma mesa com algumas cadeiras à sua esquerda,"+
      " um mural ao lado da escada, com um aluno na frente, e algumas portas que levam para laboratórios de alguns cursos.")
#time.sleep(4)
print("Mas logo ao entrar, algo prende sua atenção: um corpo jogado na frente da escadaria principal.")
#time.sleep(3)

quantidade_max_inventario = 5

inventario = []
diario= []

def mostraInventario():
    cont = 1
    print('\n----Inventário----')
    for item in inventario:
        print(str(cont)+" "+item)
        cont += 1
    cont = 1
    print('\n-------DICA-------')
    for dica in diario:
        print(str(cont)+" "+dica)
        cont += 1

    input("")
    
def adicionarDicas(dica):
    for dica1 in diario:
        if(dica1 == dica):
            return
    diario.append(dica)

def analisar_qnt_dicas(item):
    for item1 in inventario:
        if(item1 == item):
            print('😮 Você já tem o item adicionado!!')
            return
    if (len(inventario) >= quantidade_max_inventario):
        print("Você ja atingiu o limite do inventario.")
        cont = 1
        for item in inventario:
            print(str(cont)+" "+item)
            cont += 1
        res = input('Deseja excluir algum item?s/n\nR: ')
        if(res == 's'):
            nItem = int(input('Digite o número a ser excluido: '))
            inventario.pop(nItem - 1)
            inventario.append(item)
    else:
        inventario.append(item)
    
while(True):
    print("Você pode:\n"+
          "1-🪜 Olhar a escadaria\n"+
          "2-💀 Olhar o corpo\n"+
          "3-🖼️  Olhar o mural\n"+
          "4-📘 Olhar as salas\n"+
          "5-Dar palpite (você tem apena 1 chance)\n"+
          "6-Diário e Inventário\n"+
          "7-❌ Sair")
               
    
    time.sleep(1)
    escolha01 = int(input("Qual ação você deseja tomar?\nR: "))

    if escolha01 == 6:
        mostraInventario()
    
    while type(escolha01) != int:
        escolha01 = int(input("Qual ação você deseja tomar?\nR: "))

    while(escolha01 == 1):
        time.sleep(1)
        print('\nNa escadaria você encontra dois rastros de algo que aparenta ser sangue, um de cada lado do corrimão')
        
        time.sleep(1)
        res1 = input('Você quer provar para ver se é sangue mesmo? s/n \nR: ')
        if(res1 == 's'):
            
            time.sleep(1)
            print(".")
            
            time.sleep(1)
            print(".")
            
            time.sleep(1)
            print(".")
            
            time.sleep(2)
            print('\nÉ sangue mesmo.')
            diario.append("Há sangue na escadaria")
            
            time.sleep(1)
            print("Você volta para a frente da escada\n")
            
            time.sleep(1)
        break
        
    if(escolha01 == 2):
        
        time.sleep(1)
        print('\n💀 Você aproxima no corpo e encontra um pedaço de madeira ao lado coberto de sangue')
        
        time.sleep(1)
        escolha01_01= int(input('💀 Você deseja investigar o corpo ou o pedaço de madeira?\n'+
                                '1- Corpo\n'+
                                '2- Madeira\n'+
                                '3- Sair\n'+
                                'R:'))
        
        if(escolha01_01 == 1):
            
            time.sleep(1)
            print('💀 Ao analisar o corpo detalhadamente, você nota um ferimento brutal na cabeça do moribundo e uma identidade em seu bolso.')
            
            time.sleep(1)
            print('💀 Você nota que o corpo pertence a 💀 Vitor Bianchini💀, estudante da PUCPR')
            
            time.sleep(1)
            escolha01_01_01 = input('Você deseja guardar a identidade? s/n\n'+
                                    'R: ')
            
            if (escolha01_01_01 == 's'):
                
                diario.append("Há uma identidade no corpo, aparentemente a vítima\n"+
                              "se chamava Vitor -------- --------- --- -----")
                
                analisar_qnt_dicas("Identidade")
                
                time.sleep(1)
                print("Você guarda a identidade de Vitor")
            
            if(escolha01_01_01 == 'n'):
                continue

            
        if(escolha01_01 == 2):
            
            time.sleep(1)
            print('A madeira tem uma ponta afiada e aparentemente foi utilizada para matar o corpo do usuário')
            escolha01_01_01 = input('Você deseja pegar o pedaço de madeira? s/n \nR: ')
            
            if(escolha01_01_01 == 's'):
                diario.append("Há um pedaço de madeira com sangue perto do corpo")

                analisar_qnt_dicas("Pedaço de madeira")
                
                time.sleep(1)
                print("Você guarda o pedaço de madeira")

        if(escolha01 == 3):
            break

    
        
    if(escolha01 == 3):
        
        time.sleep(1)
        print('🖼️ Você olha o mural e se depara com uma linda paisagem junto com um cachorro e uma pessoa')
        
        time.sleep(1)
        escolha01_01 = input('🖼️ Você deseja pegar a imagem como uma dica? s/n \n R: ')
        if(escolha01_01 == 's'):
            
            analisar_qnt_dicas("Foto do mural")
            
            time.sleep(1)
            print("Você pega a foto do cachorro e seu dono")
            
            
    
    if(escolha01 == 4):
        
        time.sleep(1)
        print("📘 Você repara que desse saguão é possível ver 3 portas: 2 acima da escadaria e 1 abaixo")

        time.sleep(1)
        escolha01_01 = int(input("📘 Qual delas você deseja investigar?\n1- A porta de baixo\n2- A porta de cima à esquerda\n3- A porta de cima à direita\nR:"))
        
        if escolha01_01 == 1:
            
            time.sleep(1)
            print("📘 Ao lado da porta há uma pequena placa, que diz: Laboratório do curso de farmácia")
            
            time.sleep(1)
            escolha01_01_01 = input("📘 Deseja entrar? s/n")

            if escolha01_01_01 == "s":
                
                time.sleep(1)
                print("Ao entrar na sala você vê um laboratorio comum, com diversos equipamentos.")
                
                time.sleep(1)
                escolha01_01_01_01 = input("Você deseja ver quais equipamentos estão disponiveis? s/n")
                if (escolha01_01_01_01 == 's'):
                    
                    time.sleep(1)
                    print("Você nota uma maquina capaz de realizar testes de DNA.")
                    
                    time.sleep(1)
                    escolha01_01_01_01_01 = input("Deseja utilizar a maquina? s/n")
                    if escolha01_01_01_01_01 == "s":
                        if  "Pedaço de madeira" in inventario:
                            
                            time.sleep(1)
                            print("Você descobre que o sangue no graveto não pertence a Vitor")
                            diario.append("O sangue do graveto não é de Vitor")
                            
                        else:
                            
                            time.sleep(1)
                            print("Você não tem nada para analisar.")
                        
            if escolha01_01_01 == 'n':
                
                time.sleep(1)
                print("Você volta para o corredor")
                
        if escolha01_01 == 2:
            
            time.sleep(1)
            print("Ao lado da porta há uma pequena placa, que diz: Sala de revelação")
            
            time.sleep(1)
            escolha01_01_01 =input("Deseja entrar? s/n")

            if escolha01_01_01 == "s":
                
                time.sleep(1)
                print("A sala de revelação é pequena, iluminada somente por uma luz avermelhada. Dentro dela é possível ver vários recipientes cheios de líquidos diferentes,"+
                      "e alguns equipamentos para auxiliar na revelação de fotos. Logo acima dos equipamentos, há 2 fotos penduradas")
                
                time.sleep(1)
                escolha01_01_01_01 = input("Deseja investigar as fotos? s/n \nR:")
                
                if escolha01_01_01_01 == "s":
                    
                    time.sleep(1)
                    print("Em uma das fotos, é possível ver um estudante andando a caminho de um banco de madeira")
                    
                    time.sleep(2)
                    print("A outra imagem parece ter sido tirada alguns segundos após a primeira. Nela é possível ver a mochila desse aluno caindo por trás desse banco, logo acima de um pequeno cachorro")
                    
                    time.sleep(1)
                    
                    if "Foto do mural" in inventario:
                        
                        time.sleep(1)
                        print("O mesmo cachorro que você viu na foto do mural")
                        
                    if "Identidade" in inventario:
                        
                        time.sleep(1)
                        print("O dono do cachorro é o Vitor")
                        
                        time.sleep(1)
                        print("Você volta para a frente da escada")
                        
                        time.sleep(1)
                        
            if escolha01_01_01 == "n":
                
                time.sleep(1)
                print("Você volta para a frente da escada")
            
        if escolha01_01 == 3:
            
            time.sleep(1)
            print("Ao lado da porta há uma pequena placa, que diz: Laboratório de Mecânica")
            
            time.sleep(1)
            escolha01_01_01 =input("Deseja entrar? s/n")

            if escolha01_01_01 == "s":
                time.sleep(1)
                print("O Laboratório de Mecânica é grande, com varios intrumentos de grande e pequeno porte, geralmente utilizados em construção")
                
                time.sleep(1)
                print("Todos eles estão em grades de ferro, organizados por tamanho.")
                
                time.sleep(1)
                escolha01_01_01_01 = input("Deseja observar a organização dos materias? s/n")
                if (escolha01_01_01_01 == 's'):
                    
                    time.sleep(1)
                    print("Você nota que existe uma ficha com as ferramentas da sala e uma coluna para assinaturas\n"+
                          "nela se lê o seguinte: ")
                    
                    time.sleep(1)
                    print("|   Ferramenta    |    Empréstimo   |")
                    print("|-----------------|-----------------|")
                    print("|    Serrote      |      Martin     |")
                    print("|   Furadeira     |      Nicolas    |")
                    print("|    Martelo      |      Mateus     |")
                    print("|                ...                |")
                    
                    print("Natan: Foram feitos 3 empréstimos de ferramentas no dia do crime.\n" +
                                  "Serrote e furadeira não parecem ser capazes de causar aquele tipo de ferimento...")
                    
                    diario.append("Arma suspeita: Martelo")
                    
                    time.sleep(1)
                    escolha01_01_01_01_01 = input("Voce deseja voltar para o corpo ou continuar investigando? \n1- Voltar para o local do crime \n2- Continuar investigando")
                    if (escolha01_01_01_01_01 == 1):
                        
                        time.sleep(1)
                        print("Você volta para o corpo")
                    elif (escolha01_01_01_01_01 == 2):
                        
                        time.sleep(1)
                        print("Você nota que na ficha de estudantes, não há nenhum aluno que não devolveu algum instrumento.")
                        
                        time.sleep(1)
                        print("Dica: um martelo sumiu do Laboratório de Mecânica")
                        dicas.append("Dica: um martelo sumiu do Laboratório de Mecânica")
                    

            
            if escolha01_01_01 == "n":
                print("Você volta para a frente da escada")

            
    if(escolha01 == 7):        
        break

print("fim do programa. Natan.")
