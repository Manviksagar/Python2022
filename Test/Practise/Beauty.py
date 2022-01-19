from bs4 import BeautifulSoup

with open("index.html","r") as f:
    doc= BeautifulSoup(f,"html.parser")

# print(doc.prettify())

tags=doc.find_all("p")
# print(tags)

tag=doc.find_all("p")[0]
print(tag)
print("------------")
print(tag.find_all("br"))