
import requests
from bs4 import BeautifulSoup

# Web sayfasını al
url = 'https://bigpara.hurriyet.com.tr/doviz/dolar/'  # Dolar kuru sayfasının URL'si
response = requests.get(url)

# Sayfanın içeriğini BeautifulSoup ile analiz et
soup = BeautifulSoup(response.content, 'html.parser')

# Dolar kuru bilgisini bulmak
# class='value' ya da sayfadaki başka bir etiketin class adı olabilir.
# Burada sayfayı inceleyip doğru sınıf adını kontrol ettik
dolar_kuru = soup.find('span', class_='value').text.strip()

# Sonucu terminalde yazdır
print(f"Anlık Dolar Kuru: {dolar_kuru}")