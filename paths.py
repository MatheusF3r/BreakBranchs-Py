from random import choice

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

# ex: web = combination("1 2 3")

def breakArrangement(params=list(),allocation=int()):
    ''' # Combina todos itens de uma lista, em uma determinada alocação
        # parametro:
        # params - recebe a lista para combinar
        # allocation - recebe o tamanho da alocação
        # retorno:
        # memory - retorna uma lista de todos os valores combinados
    '''
    possibilites = len(params) ** len(params)-1
    memory = list()
    while len(memory) <= possibilites:
        memory_secondary = list()
        while len(memory_secondary) <= allocation-1:
            memory_secondary.append(choice(params))
        if memory_secondary in memory:
            memory_secondary.clear()        
        else:
            memory.append(memory_secondary)
    return memory
