from bs4 import BeautifulSoup
import requests
date=input("Enter the date in YYYY-MM-DD format: ")
url=f"https://www.billboard.com/charts/hot-100/{date}"
response=requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)
with open("thebillboard.text", mode="w",encoding="utf-8") as file:
    for i in song_names:
        file.write(f"{i}\n")