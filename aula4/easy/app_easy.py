import requests

get_url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(get_url)
print("GET response status code:", response.status_code)
print("GET response body:", response.json()[:2]) 


post_url = "https://jsonplaceholder.typicode.com/posts"
json_data = {
    "title": "If you get this, you're a hacker",
    "body": "You're not, but that's fine - It does mean that the POST worked",
    "userId": 1
}

post_response = requests.post(post_url, json=json_data)
print("\nPOST response status code:", post_response.status_code)
print("POST response body:", post_response.json())