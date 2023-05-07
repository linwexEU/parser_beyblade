import requests
import fake_useragent 
from bs4 import BeautifulSoup  

user = fake_useragent.UserAgent().random

header = {
    "user-agent": user
}

for i in range(1, 9):
    link = f"https://leva.com.ua/ua/bayblade/?page={i}"
    res = requests.get(link, headers=header)
    soup = BeautifulSoup(res.text, "lxml")
    div_all = soup.find_all("div", class_="image")

    for i in div_all:
        image_all = i.find_all("script")

        for image in image_all:
            image_link = str(image.text.split(" ")[5][6:-2])
            image_name = "".join(image.text.split("alt")[1][3:]).split("\\")[0]
            try:
                post = requests.get(image_link, headers=header).content

                with open(f"{image_name}.jpg", "wb") as file:
                    file.write(post)

                print(image_name, "- успешно скачан!")
            except:
                pass
    
