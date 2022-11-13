import requests

def all_href(soup,params=None):
    ''' # busca todos os links de uma pagina
        # parametro:
        # soup - recebe a pagina parser
        # params - recebe um padrão para procurar nos links
        # retorno:
        # memory - retorna os links encontrados
    '''
    memory = list()
    link = soup.find_all('a')
    for i in link:
        try:
            href = i['href']
        except:
            None
        if params == None:
            memory.append(href)
        else:
            if href.startswith(params):
                memory.append(href)
            else:
                None
    return memory

def all_insert(soup):
    ''' # Busca todos os campos de inserção da pagina
        # parametro:
        # soup - recebe a pagina parser
        # retorno:
        # memory - retorna os nomes dos cmapos de inserção
    '''
    insert = soup.find_all('input')
    payload = list()
    for i in insert:
        try:
            payload.append(i['id'])
        except:
            None
    return payload

def all_imgs(soup):
    ''' # Busca todos links de imagens
        # parametro:
        # soup - recebe a pagina parser
        # retorno:
        # memory - retorna todos links de imagens
    '''
    memory = list()
    img = soup.find_all('img')
    for i in img:
        try:
            memory.append(i['src'])
        except:
            None
    return memory


def imgs_download(name=str(),url=str()):
    ''' # Faz o download de imagens
        # parametro:
        # name - nome com o qual será salvo o arquivo
        # url - recebe o url para download
        # retorno:
        # return - retorna a confirmação de download
    '''
    extensions = ['.jpeg','.jpg','.gif','.png','.bmp','.psd','.tiff','.pdf','.svg','.raw','.webp']
    for ext in extensions:
        if url.endswith(ext):
            file = open('{}{}'.format(name,ext),'wb')
            r = requests.get(url)
            file.write(r.content)
            file.close()
            return 'download confirmed.'
        else:
            None
