import requests

api_key = "Y622QFPz2idteWegBpn3kRUoUXay7Dgk"
search_term = input("Enter a search term: ")

endpoint = f"http://api.giphy.com/v1/gifs/search?api_key={api_key}&q={search_term}&limit=10"

response = requests.get(endpoint)

data = response.json()

for gif in data["data"]:
    print(gif["url"])
