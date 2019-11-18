estoque = list()
produto = dict()
while True:
    print('_'*30)
    escolha = int(input('Olá, bem vindo ao seu estoque'
                        '\nDigite 1 para acessar o seu estoque'
                        '\nDigite 2 para cadastrar um novo produto '
                        '\nDigite 3 para sair'
                        '\nOpção: '))
    print('_'*30)
    if escolha == 2:
        while True:
            produto.clear()
            produto['codigo:'] = int(input('Código do produto: '))
            produto['nome:'] = str(input('Nome: '))
            produto['cor:'] = str(input('Cor: '))
            produto['tamanho:'] = int(input('Tamanho: '))
            estoque.append(produto.copy())
            while True:
                resp = str(input('Deseja continuar ? S/N ')).upper()[0]
                if resp in 'SN':
                    break
                print('ERRO ! Digite apenas S ou N')
            if resp == 'N':
                break
    elif escolha == 1:
        for x in estoque:
            print(x)
        print()
    elif escolha == 3:
        print('Programa encerrado')
        break
    else:
        print('Número inválido')