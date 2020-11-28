from partes import responder


def cmd_url(busca, driver, chat_id):
    from time import sleep
    driver.get(busca)
    sleep(10)
    parser = driver.find_element_by_xpath('//span[@class="view-count style-scope yt-view-count-renderer"]')
    contagem_v = parser.get_attribute('innerHTML')
    v = contagem_v.split(' ')
    valor = str(v[0])
    valor = valor.replace('.', '')
    valor = int(valor)
    Minimo = Maximo = atual_min = atual_max = 0
    quant = {10000000: {'minimo': 10000, 'maximo': 190000}, 1000000: {'minimo': 1000, 'maximo': 19000},
             100000: {'minimo': 100, 'maximo': 1900}, 10000: {'minimo': 10, 'maximo': 190},
             1000: {'minimo': 1, 'maximo': 19}}
    contagem = valor
    for key, values in quant.items():
        if contagem >= key:
            for k, v in values.items():
                if k == 'minimo':
                    atual_min = v
                else:
                    atual_max = v
            while contagem >= key:
                contagem -= key
                Maximo += atual_max
                Minimo += atual_min
    sleep(3)
    title = driver.find_element_by_xpath(
        '//h1[@class="title style-scope ytd-video-primary-info-renderer"]//yt-formatted-string[@class="style-scope ytd-video-primary-info-renderer"]')
    t = title.get_attribute('innerHTML')
    views = driver.find_element_by_xpath('//span[@class="view-count style-scope yt-view-count-renderer"]')
    v = views.get_attribute('innerHTML')
    nome_do_canal = driver.find_element_by_xpath(
        '//yt-formatted-string[@id="text"]//a[@class="yt-simple-endpoint style-scope yt-formatted-string"]')
    n = nome_do_canal.get_attribute('innerHTML')
    like = driver.find_elements_by_xpath(
        '//a[@class="yt-simple-endpoint style-scope ytd-toggle-button-renderer"]//yt-formatted-string[@id="text"]')
    sleep(5)
    count = pos = neg = 0
    for x in like:
        if count <= 1:
            por = ''
            parser = x.get_attribute('innerHTML')
            values = parser.split('&')
            value = values[0]
            if len(values) > 1:
                por = values[1].split(';')
            if ',' in value:
                value = value.replace(',', '')
            if value.isdigit():
                print(value)
                if por == 'mil':
                    value += '000'
                value = int(value)
                if count == 0:
                    pos = value
                else:
                    neg = value
        count += 1

    tot = pos + neg
    maior = (pos / tot) * 100
    menor = 100 - maior
    maior = f'{maior:.2f}'
    menor = f'{menor:.2f}'
    responder.resp([f'views:{v}', f'canal:{n}', f'titulo:{t}',
            f'faturamneto esperado R${Minimo} e R${Maximo} porcentagem: {maior} gostaram {menor} n gostaram', ' '], chat_id)


def search(tema, driver, chat_id):
    from bs4 import BeautifulSoup
    global search
    search = False
    driver.get(f'https://www.youtube.com/results?search_query={tema}&sp=CAI%253D')
    t = driver.find_element_by_xpath('//ytd-item-section-renderer[@class="style-scope ytd-section-list-renderer"]')
    HTML = t.get_attribute('outerHTML')
    soup = BeautifulSoup(HTML, 'html.parser')
    teste = soup.find_all('a', {'id': 'video-title'})
    urls = list()
    for x in teste:
        urls.append('https://youtube.com/' + x['href'])
    responder.resp(urls, chat_id)
