import requests 

api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
res =response.json()
print(response.headers["Content-Type"])
print(res)
