def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if ano == 16 or ano == 17 or ano >= 65:
        return(f'Com {idade} anos: VOTO OPCIONAL!')
    elif ano < 16:
        return(f'Com {idade} anos: NÃO VOTA! ')
    else:
        return(f' Com {idade} anos: VOTO OBRIGÁTORIO!')


a = int(input('Em que ano você nasceu?'))
print(voto(a))

    