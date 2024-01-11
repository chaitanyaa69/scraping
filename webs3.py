from bs4 import BeautifulSoup
import requests

response=requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
webpage=response.text
soup=BeautifulSoup(webpage,"html.parser")
#print(soup.prettify())
all_mv=soup.find_all(name="h3",class_="title") #because all the movie titles are included in the h3 with class named title
#print(all_mv)
movies_list=[movie.get_text() for movie in all_mv]
#print(movies_list) #prints the movies list
#print(movies_list[::-1]) #prints the movies list in reverse order
#for i in range(len(movies_list)-1,-1,-1):
#    print(movies_list[i])
movies=movies_list[::-1]
with open("movies.text", mode="w",encoding="utf-8") as file:
    for i in movies:
        file.write(f"{i}\n")
