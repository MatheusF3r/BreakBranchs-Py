def combination(params=str()):
    ''' # Combina todos itens de uma string
        # parametro:
        # params - recebe a variavel para recombinação
        # retorno:
        # combinations_ - retorna uma lista com o valor recombinado
    '''
    split_ = params.split()
    combinations_ = list()
    count = int()

    while len(split_)-1>= count:
        combinations = list()
        for i in split_:
            combinations.insert(count,i)
        count +=1
        combinations_.append(combinations)
    return combinations_

'''
web = combination('DOM PEDRO PRIMEIRO')
c = int()
for i in web:
    term = str(web[c]).replace(',','').replace("'",'').replace('[','').replace(']','')
    print('filetype:xlsx "{}"'.format(term))
    c +=1
'''
