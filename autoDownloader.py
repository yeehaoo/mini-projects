import requests
import win32clipboard

win32clipboard.OpenClipboard()
url = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

response = requests.get(url)
if response.status_code == 200:
    with open("./file.jpg", 'wb') as f:
        f.write(response.content)
