import os
from bs4 import BeautifulSoup
import requests

search_object = input("Введите запрос: ")
url = f"https://www.google.com/search?tbm=isch&q={search_object}"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
list_images = soup.findAll('img')
list_images = list_images[1:16] # нулевая картинка логотип в шапке с локальным адресом
i = 1
if not os.path.exists(f"{search_object}"):
    os.mkdir(f"{search_object}")
os.chdir(f"{search_object}")
for image in list_images:
    page_with_image = requests.get(image['src'])
    with open(f"{search_object}{i}.jpg", 'wb') as file:
        file.write(page_with_image.content)
        i += 1
print("Загрузка выполнена успешно")