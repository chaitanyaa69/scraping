from bs4 import BeautifulSoup
with open("website.html",'r',encoding='utf-8') as file:
    contents=file.read()
soup=BeautifulSoup(contents,"html.parser")
#print(soup) #extracts and displays all the html contents
#print(soup.title) prints title tag
#print(soup.title.string) prints the string inside the title tag
#print(soup.prettify())
anchor_tags_with_a=soup.find_all(name="a") #prints all the anchor tags and its content
print(anchor_tags_with_a)
for tag in anchor_tags_with_a:
    #print(tag.getText()) #prints the text included in the anchor tag
    print(tag.get("href")) #prints the links included in the anchor tag
heading=soup.find(name="h1",id="name") #finds an h1 element with the id name
print(heading)
section=soup.find(name="h3",class_="heading") #finds an h3 element with the class heading
print(section) #inorder to print the string use print(section.string)
headings=soup.select(".heading")
print(headings)
