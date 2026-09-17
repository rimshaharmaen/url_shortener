import urllib.request
import json

data = json.dumps({"long_url": "https://example.com"}).encode()

req = urllib.request.Request(
    "http://localhost:5000/shorten",
    data=data,
    headers={"Content-Type": "application/json"},
    method="POST"
)

with urllib.request.urlopen(req) as response:
    result = json.loads(response.read())
    print(result)