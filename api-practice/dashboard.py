import requests

API_KEY = "db22b4e1eb9276d53f1f5457cf69fa53"
city = "Makassar"

response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric")
data = response.json()

weather_data = {
    "city": data['name'],
    "temperatur": data['main']['temp'],
    "humidity": data['main']['humidity']

}

username = "Ssmailoo"

response = requests.get(f"https://api.github.com/users/{username}")
data = response.json()

github_data = {
    "login": data['login'],
    "company": data['company'] or "Tidak ditentukan",
    "location": data['location'] or "Tidak ditentukan",
    "public_repos": data['public_repos']
}
print(f"""
========== DAILY DASHBOARD ==========

Today's Weather
_______________
City: {weather_data['city']}
Temperature: {weather_data['temperatur']}°C
Humidity: {weather_data["humidity"]}%

GitHub User
___________
Username: {github_data["login"]}
Company: {github_data["company"]}
Location: {github_data["location"]}
Public Repositories: {github_data["public_repos"]}

====================================
""")