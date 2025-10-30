import requests
request = "https://api.chucknorris.io/jokes/random"

try:
    response = requests.get(request)
    if response.status_code == 200:
        print(response.json()["value"])
except Exception as e:
    print(e)