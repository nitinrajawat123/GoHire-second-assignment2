import requests
from bs4 import BeautifulSoup

def get_top_articles(url, num_articles=5):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = soup.find_all('h3', class_='gs-c-promo-heading__title')
    top_articles = articles[:num_articles]

    titles = [article.text.strip() for article in top_articles]
    return titles

if __name__ == "__main__":
    bbc_url = "https://www.bbc.com/news"
    top_articles_titles = get_top_articles(bbc_url, num_articles=5)

    print("Top 5 Trending Articles on BBC News:")
    for i, title in enumerate(top_articles_titles, start=1):
        print(f"{i}. {title}")
