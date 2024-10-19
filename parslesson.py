import requests
import bs4


response = requests.get("https://www.iplocation.net/")
print(response.text)