import requests
from bs4 import BeautifulSoup


response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# headings = soup.find_all(name="span", class_="titleline")[1]
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
for article in articles:
    article_texts.append(article.getText())
    article_links.append(article.find(name="a").get("href"))

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# head = headings.find(name="a")
# print(article_texts)
# print("-------------------------------")
# print(article_links)
# print("-------------------------------")
# print(article_upvote)

# print(response.text)

# index_of_most_upvoted_article = 0
# counter = 0
# most_votes = article_upvote[0]
# for article in article_upvote:
#     counter += 1
#     if article > most_votes:
#         most_votes = article
#         index_of_most_upvoted_article = counter

largest_number = max(article_upvote)
largest_index = article_upvote.index(largest_number)

print(f"The most upvoted article on website Hacker News:\n{article_texts[largest_index]}\n\nLink: {article_links[largest_index]}")








