import requests
from bs4 import BeautifulSoup
import lxml

url = "https://www.pagina12.com.ar/"

# Manejo de errores
try:
    p12 = requests.get(url) 
except Exception as e:
    print("error en la Matrix")
    print(e)
    print("\n")


"""
print(p12.status_code)
print(p12.headers) #encabezado respuesta
print()
print(p12.request.headers) # Encabezado peticion

print(p12.request.method) #tipo de peticion
"""

soup = BeautifulSoup(p12.text, "lxml") # Parsear el html

sections = soup.find("ul", {"class": "main-sections"}).find_all("li") #find busca el nombre de la clase o elemento

sec = sections[0]

print(sec.a.get("href")) # Retorna el atributo
print(sec.a.get_text()) #Retorna el texto

links_sections = [sec.a.get("href") for sec in sections]
name_sections = [sec.get_text() for sec in sections]

linkSec = requests.get(links_sections[0])

s_section = BeautifulSoup(linkSec.text, "lxml")

list_links = []

def links_articles(bs4Objet):


    f_art = bs4Objet.find("article", {"class": "article-item"})

    if f_art:
        list_links.append(f_art.a.get("href"))
    
    list_arts = bs4Objet.find("section", {"class": "list-content"}).find_all("a")

    for e in list_arts:
        if e.get("href") not in list_links:
            list_links.append(e.get("href")) 
    
    for link in list_links:
        print(link)
        
        
    # top_arts_list = list_top_arts.find_all("article")

    # for ar in top_arts_list:
    #     list_links.append(ar.a.get("href"))

    

    # for l in list_links:
    #     print(l)

links_articles(s_section)

url_art = list_links[0]

try:
    art = requests.get(url_art)
    if art.status_code == 200:
        s_art = BeautifulSoup(art.text, "lxml")
        #Extraer titulo
        title = s_art.find("h1", attrs={"class": "article-title"}).get_text()
        print(title)

        date_art = s_art.find("span", attrs={"pubdate": "pubdate"}).get("datetime")
        print(date_art)

        prefix_art = s_art.find("h2", attrs={"class": "article-prefix"}).get_text()
        print(prefix_art)

        summ_art = s_art.find("div", attrs={"class": "article-summary"}).get_text()
        print(summ_art)

        text_art = s_art.find("div", attrs={"class": "article-text" }).find_all("p")

        for p in text_art:
            print(p.get_text(), "\n")

        media = s_art.find("div", attrs={"class": "article-main-media-image__container"})
        img_list = media.find_all("img")

        if len(img_list) == 0:
            print("No hay imgs")
        else:
            img_art = img_list[-1]
            print(img_art.get("data-src"))
        
        img_req = requests.get(img_art.get("data-src"))




        

except Exception as e:
    print("Error:")
    print(e)
    print("\n")



