import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
movies_web_page = response.text

soup = BeautifulSoup(movies_web_page, "html.parser")
movies_titles = [title.getText() for title in soup.find_all(name="h3", class_="title")]

movies_titles.reverse()
# Other 2 options for reversing list
# for n in range(len(movies_titles) -1, -1, -1):
#     print(movies_titles[n])
# movies_titles[::-1]

with open("100_best_movies.txt", "w") as file:
    for title in movies_titles:
        file.write(f"{title}\n")
