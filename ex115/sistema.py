from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if  not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['Ver Pessoas Cadastradas',"Cadastrar Nova Pessoa",'Sair do Sistema'])
    if resposta == 1:
        #OPÇAO DE LISTAR UM CONTEÚDO de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome:'))
        idade = leiaInt('Idade:')
        cadastrar(arq,nome,idade)

    elif resposta == 3:
        cabeçalho('\033[31mSaindo do Sistema... Até logo!!\033[m')
        break
    else:
        cabeçalho('\033[31mErro! Digite uma opção válida!\033[m')
    sleep(2)

