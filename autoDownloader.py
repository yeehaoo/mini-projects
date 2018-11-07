import requests

url = "https://upload.wikimedia.org/wikipedia/commons/1/15/Red_Apple.jpg"
response = requests.get(url)
if response.status_code == 200:
    with open("./file.jpg", 'wb') as f:
        f.write(response.content)
