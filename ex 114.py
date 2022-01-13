import urllib
import urllib.request

try:#tratamento de exceções
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[0;31mO site pudim não está acessível no momento!\033[m')
else:
    print('Consegui acessar o site pudim com sucesso!!')
    print(site.read())#read() lê o endereço do site, no caso!




