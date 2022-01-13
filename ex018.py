from math import radians, sin,cos,tan
angulo = float(input("Digite o angulo:"))
seno = sin(radians(angulo))# é necessario transformar a medida para radianos, por isso usamos"(seno = sin(radians(angulo))"
print("O ângulo de {} tem o SENO de {:.2f}".format(angulo,seno))
cosseno = cos(radians(angulo))
print("O ãngulo de {} tem o COSSENO de {:.2f}".format(angulo, cosseno))
tangente = tan(radians(angulo))
print("O angulo de {} tem a TANGENTE DE {:.2f}".format(angulo,tangente))
#Esse exercicio eu não consegui fazer!