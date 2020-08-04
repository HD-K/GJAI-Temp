import requests
from bs4 import BeautifulSoup

movie_info = []


url = "https://movie.naver.com/movie/running/current.nhn"
responce = requests.get(url)
soup = BeautifulSoup(responce.text, "html.parser")

movie_section = soup.select(
    'div[id=wrap] > div[id=container] > div[id=content] > div.article > div.obj_section > div.lst_wrap > ul.lst_detail_t1 > li'
)

for li in movie_section:
    a_tag = li.select_one('dl.lst_dsc > dt.tit > a')
    movie_title = a_tag.text
    movie_code = a_tag['href'].split('?code=')

    movie_info_set = ({
        "title" : movie_title,
        "code" : movie_code[1]
    })

    movie_info.append(movie_info_set)


for i in movie_info:
    print(i)