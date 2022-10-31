def factory(parms=int()):
    ''' # Fatora um numero
        # parametros:
        # parms - recebe um valor numerico inteiro.
        # retorno:
        # total - retorna um valor inteiro fatorado.
    '''
    total = int(1)
    while parms >= 1:
        total *= parms
        parms -=1
    return total
