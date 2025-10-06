import requests

url="https://fakestoreapi.com/products"

rq=requests.get(url)
data=rq.json()
print(data)