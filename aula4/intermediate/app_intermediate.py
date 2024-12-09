import requests
import subprocess

get_url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(get_url)
print("GET response status code:", response.status_code)
print("GET response body:", response.json()[:2])

post_url = "https://jsonplaceholder.typicode.com/posts"
json_data = '{"title":"Tricky","body":"yeah that was a bit trickier overall","userId":1}'
curl_command = [
    "curl",
    "-X", "POST",
    post_url,
    "-H", "Content-Type: application/json",
    "-d", json_data
]

try:
    result = subprocess.run(curl_command, capture_output=True, text=True, check=True)
    print("\nCURL POST response (stdout):", result.stdout)
    if result.stderr:
        print("CURL POST response (stderr):", result.stderr)
except subprocess.CalledProcessError as e:
    print("CURL command failed:", e)