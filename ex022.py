nome = str(input("Digite o seu nome completo:")).strip()#acrescente sempre o tipo, no caso 'str' string;
dividido = nome.split()                          #strip, aqui é a função que elimina os espaços antes e depois do nome:
print("Analisando seu nome...")
print("Seu nome em maiúsculas é {}.".format(nome.upper()))
print("Seu nome em minúsculas é {}.".format(nome.lower()))
print("Seu nome tem ao todo {} letras.".format(len(nome)- nome.count(" ")))
print("Seu primeiro nome é {} e ele tem {} letras.".format(dividido[0],len(dividido[0])))
#para esse ultimo print, poderia ter feito assim:
#print("Seu primeiro nome é {} e ele tem {} letras.".format(dividido[0],nome.find(" ")))