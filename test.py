import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "video/10", {'id': 10,'name': "Test Title",'views': 20,'likes': 40},)

print(response.json())

response = requests.get(BASE + "video/10", {})
print(response.json())

response = requests.patch(BASE + "video/10", {'id': 10,'name': "Final Test Title",'views': 0,'likes': 0},)
print(response.json())

response = requests.delete(BASE + "video/10")
print(response.json())


response = requests.get(BASE + "video/10", {})
print(response.json())
