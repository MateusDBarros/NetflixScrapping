# Netflix Mystery TV Shows Scraper

Este projeto é um script em Python que acessa uma página da Netflix e extrai informações sobre filmes ou séries de mistério, coletando os títulos e as descrições dos itens listados.

## Funcionalidades

- **Requisição HTTP:** Utiliza a biblioteca `requests` para acessar a URL da página.
- **Extração de Dados:** Emprega o `BeautifulSoup` para fazer o parsing do HTML e extrair os elementos `<h3>` (títulos) e seus respectivos `<p>` (descrições), que estão no mesmo nível na estrutura do HTML.
- **Formatação de Texto:** Usa o módulo `textwrap` para formatar as descrições, quebrando o texto em linhas com largura fixa (50 caracteres) para facilitar a leitura.
- **Exibição no Terminal:** Imprime as informações extraídas no console com uma separação visual entre os itens.

## Pré-requisitos

- **Python 3:** Certifique-se de que o Python 3 esteja instalado no seu sistema.
- **Bibliotecas Python:** Você precisará instalar as seguintes bibliotecas:
  - `requests`
  - `beautifulsoup4`
