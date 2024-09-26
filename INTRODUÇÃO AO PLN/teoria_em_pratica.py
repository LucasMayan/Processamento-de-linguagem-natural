import requests
from bs4 import BeautifulSoup

# URL do site do IBGE com os dados de densidade demográfica dos municípios
url = 'https://cidades.ibge.gov.br/brasil/sp/panorama'

# Fazendo uma requisição para obter o conteúdo da página
response = requests.get(url)
conteudo = response.content

# Analisando o conteúdo HTML com BeautifulSoup
soup = BeautifulSoup(conteudo, 'html.parser')

# Inspecionar o conteúdo para ver como a tabela é identificada
# Você pode imprimir o conteúdo HTML para inspeção
print(soup.prettify())

# Tente localizar a tabela correta. Aqui estou usando um seletor mais geral
# que você pode ajustar conforme necessário.
tabelas = soup.find_all('table')

# Verifique se alguma tabela foi encontrada
if tabelas:
    tabela = tabelas[0]  # Seleciona a primeira tabela encontrada, se houver
    tbody = tabela.find('tbody')
    
    if tbody:
        municipios = []
        for linha in tbody.find_all('tr'):
            colunas = linha.find_all('td')
            nome_municipio = colunas[0].text.strip()
            densidade_demografica = float(colunas[1].text.strip().replace(',', '.'))
            if densidade_demografica >= 100:
                municipios.append((nome_municipio, densidade_demografica))

        # Imprimindo a lista de municípios com densidade acima de 100 hab/km²
        for municipio in municipios:
            print(f"Município: {municipio[0]}, Densidade Demográfica: {municipio[1]} hab/km²")
    else:
        print("Não foi possível encontrar o tbody na tabela.")
else:
    print("Não foi possível encontrar nenhuma tabela na página.")
