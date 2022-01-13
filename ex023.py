n = int(input("Digite um numero entre 0 e 9999:"))
unidade = n // 1 % 10# '//' divisão inteira e '%' resto da divisão;
dezena  = n // 10 % 10       #EX: 1234 // 1= 1234 % 10 = 4...unidade é 4
centena = n // 100 % 10          #1234 // 10= 123 % 10 = 3...dezena é 3
milhar  = n // 1000 % 10         #1234 // 100= 12 % 10 = 2...centena é 2
print("Analisando o número {}...\n" #1234 // 1000= 1 % 10= 1...milhar é 1.
      "unidade: {}\n"
      "dezena:  {}\n"
      "centena: {}\n"
      "milhar:  {}".format(n, unidade, dezena, centena, milhar))