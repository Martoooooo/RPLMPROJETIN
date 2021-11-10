import time

print("Você é Natan, 23 anos, um perito criminal investigando um caso na PUCPR")
#time.sleep(2)
print("Ao chegar no prédio principal, você repara no saguão: uma sala grande, com uma escada dupla no centro, uma mesa com algumas cadeiras à sua esquerda,"+
      " um mural ao lado da escada, com um aluno na frente, e algumas portas que levam para laboratórios de alguns cursos.")
#time.sleep(4)
print("Mas logo ao entrar, algo prende sua atenção: um corpo jogado na frente da escadaria principal.")
#time.sleep(3)

dicas = [1, 2 ,3]
quantidade_max_dicas = 3

inventario = []

def analisar_qnt_dicas():
    if (len(dicas) > quantidade_max_dicas):
        print("Você ja atingiu o limite de dicas.")
        cont = 1
        for dica in dicas:
            print(cont+" "+dica)
            cont += 1
    
while(True):
    print("Você pode: \n1- Olhar a escadaria\n2- Olhar o corpo\n3- Olhar o mural\n4- Olhar as salas\n5- Sair")
    escolha01 = int(input("Qual ação você deseja tomar?\nR: "))
    
    while type(escolha01) != int:
        escolha01 = int(input("Qual ação você deseja tomar?\nR: "))

    while(escolha01 == 1):
        print('Na escadaria você encontra dois rastros de algo que aparenta ser sangue, um de cada lado do corrimão')
        res1 = input('Você quer provar para ver se é sangue mesmo? s/n \n')
        if(res1 == 's'):
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(2)
            print('\nÉ sangue mesmo.')
            time.sleep(1)
            print("Você volta para a frente da escada\n")
        break

    if(escolha01 == 2):
        print('Você aproxima no corpo e encontra um pedaço de madeira ao lado coberto de sangue')
        time.sleep(1)
        escolha01_01= int(input('Você deseja investigar o corpo ou o pedaço de madeira?\n1- Corpo\n2- Madeira\n3- Sair\nR:'))
        
        if(escolha01_01 == 1):
            time.sleep(1)
            print('Ao analisar o corpo detalhadamente, você nota um ferimento brutal na cabeça do moribundo e uma identidade em seu bolso.')
            time.sleep(1)
            print('Você nota que o corpo pertence a Vitor Bianchini, estudante da PUCPR')
            time.sleep(1)
            escolha01_01_01 = input('Você deseja guardar a identidade? s/n\nR: ')
            if (escolha01_01_01 == 's'):
                analisar_qnt_dicas()
                dicas.append("Dica: A identidade do corpo encontrado nas escadarias")
                inventario.append("Identidade")
                print("Você guarda a identidade de Vitor")

            
        if(escolha01_01 == 2):
            print('A madeira tem uma ponta afiada e aparentemente foi utilizada para matar o corpo do usuário')
            escolha01_01_01 = input('Você deseja pegar o pedaço de madeira? s/n\nR:')
            if(escolha01_01_01 == 's'):
                dicas.append('Dica: Pedaço de madeira afiado com sangue')
                inventario.append("Pedaço de madeira")

            
            
        if(escolha01 == 3):
            break

    
        
    if(escolha01 == 3):
        print('Você olha o mural e se depara com uma linda paisagem junto com um cachorro e uma pessoa')
        escolha01_01 = input('Você deseja pegar a imagem como uma dica? s/n')
        if(escolha01_01 == 's'):
            dicas.append("Dica: Uma imagem de uma paisagem com um animal e aparetemente seu dono")
            inventario.append("Foto de cachorro e dono")
    
    if(escolha01 == 4):
        print("Você repara que desse saguão é possível ver 3 portas: 2 acima da escadaria e 1 abaixo")

        escolha01_01 = int(input("Qual delas você deseja investigar?\n1- A porta de baixo\n2- A porta de cima à esquerda\n3- A porta de cima à direita\nR:"))
        
        if escolha01_01 == 1:
            print("Ao lado da porta há uma pequena placa, que diz: Laboratório do curso de farmácia")
            escolha01_01_01 = input("Deseja entrar? s/n")

            if escolha01_01_01 == "s":
                print("Ao entrar na sala você vê um laboratorio comum, com diversos equipamentos.")
                escolha01_01_01_01 = input("Você deseja ver quais equipamentos estão disponiveis? s/n")
                if (escolha01_01_01_01 == 's'):
                    print("Você nota uma maquina capaz de realizar testes de DNA.")
                    escolha01_01_01_01_01 = input("Deseja utilizar a maquina? s/n")
                    if escolha01_01_01_01_01 == "s":
                        if  "Pedaço de madeira" in dicas:
                            print("Você descobre que o sangue dno graveto não pertence a Vitor")
                            dicas.append("O sangue do graveto não é de Vitor")
                        else:
                            print("Você não tem os materiais nescessarios.")
                        
            if escolha01_01_01 == 'n':
                print("Você volta para o corredor")
                
        if escolha01_01 == 2:
            print("Ao lado da porta há uma pequena placa, que diz: Sala de revelação")
            escolha01_01_01 =input("Deseja entrar? s/n")

            if escolha01_01_01 == "s":
                print("A sala de revelação é pequena, iluminada somente por uma luz avermelhada. Dentro dela é possível ver vários recipientes cheios de líquidos diferentes,"+
                      "e alguns equipamentos para auxiliar na revelação de fotos. Logo acima dos equipamentos, há 2 fotos penduradas")
                escolha01_01_01_01 = input("Deseja investigar as fotos? s/n")
                
                if escolha01_01_01_01 == "s":
                    print("Em uma das fotos, é possível ver um estudante andando a caminho de um banco de madeira")
                    time.sleep(2)
                    print("A outra imagem parece ter sido tirada alguns segundos após a primeira. Nela é possível ver a mochila desse aluno caindo por trás desse banco, logo acima de um pequeno cachorro")
                    time.sleep(1)
                    
                    if "\nDica: Uma imagem de uma paisagem com um animal e aparetemente seu dono" in dicas:
                        print("O mesmo cachorro que você viu na foto do mural")
                    if "Dica: A identidade do corpo encontrado nas escadarias" in dicas:
                        print("O dono do cachorro é o Vitor")
                        time.sleep(1)
                        print("Você volta para a frente da escada")
                        time.sleep(1)
                        
            if escolha01_01_01 == "n":
                print("Você volta para a frente da escada")
            
        if escolha01_01 == 3:
            print("Ao lado da porta há uma pequena placa, que diz: Laboratório de Mecânica")
            
            escolha01_01_01 =input("Deseja entrar? s/n")

            if escolha01_01_01 == "s":
                print("O Laboratório de Mecânica é grande, com varios intrumentos de grande e pequeno porte, geralmente utilizados em construção")
                print("Todos eles estão em grades de ferro, organizados por tamanho.")
                escolha01_01_01_01 = input("Deseja observar a organização dos materias? s/n")
                if (escolha01_01_01_01 == 's'):
                    print("Você nota que existe uma ficha com o nome de todos os estudantes que utilizaram ferramentas.")
                    print("Ao se aproximar da grade, nota a falta de um martelo.")
                    escolha01_01_01_01_01 = input("Voce deseja voltar para o corpo ou continuar investigando? \n1- Voltar para o local do crime \n2- Continuar investigando")
                    if (escolha01_01_01_01_01 == 1):
                        print("Você volta para o corpo")
                    elif (escolha01_01_01_01_01 == 2):
                        print("Você nota que na ficha de estudantes, não há nenhum aluno que não devolveu algum instrumento.")
                        print("Dica: um martelo sumiu do Laboratório de Mecânica")
                        dicas.append("Dica: um martelo sumiu do Laboratório de Mecânica")
                    

            
            if escolha01_01_01 == "n":
                print("Você volta para a frente da escada")

            
    if(escolha01 == 5):        
        break

print("fim do programa. Natan.")
