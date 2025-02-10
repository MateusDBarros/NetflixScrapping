import requests
from bs4 import BeautifulSoup
import textwrap


def main():
    url = 'https://www.netflix.com/tudum/articles/mystery-tv-shows'

    response = requests.get(url)

    if response.status_code == 200:

        html_content = response.text

        soup = BeautifulSoup(html_content, 'html.parser')

        movies = soup.find_all('h3', class_='css-4maxu3')
        print(f'Exibindo {len(movies)} filmes.\n')

        for movie in movies:
            title = movie.text
            description = movie.find_next_sibling('p').text
            formated_description = textwrap.fill(description, width=50)
            print('Titulo: ', title)
            print()
            print('Descrição: ', formated_description)
            print()
            print(f'---------------------------------------------------------------------------------')
            print()
    else:
        print("Faha na requisição. Codigo de status:", response.status_code)


if __name__ == '__main__':
    main()
