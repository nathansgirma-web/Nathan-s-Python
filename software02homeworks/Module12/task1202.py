import requests

city = input("Enter municipality name: ")
request= f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=d9a98e7e8035f2480689c709bd266b6e&units=metric"

try:
    response = requests.get(request)
    if response.status_code == 200:
        response = response.json()
        description = response["weather"][0]["description"]
        temperature = response["main"]["temp"]
        print(f"Weather: {description}")
        print(f"Temperature: {temperature} Celsius")
except Exception as e:
    print(e)

