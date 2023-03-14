import requests
from bs4 import BeautifulSoup

url = 'https://www.tiktok.com/@twice_tiktok_official/video/7210262310001200386'

print(f"Getting the view count for {url}...")
response = requests.get(url)
print(response)
soup = BeautifulSoup(response.text, 'html.parser')

view_count = soup.find('strong', {'class': 'jsx-3424274966 video-meta-count'}).text
print(f"The video has been viewed {view_count} times.")
