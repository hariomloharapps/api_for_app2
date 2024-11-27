import requests
import json

# API endpoint
url = "http://apiapp2hwd.pythonanywhere.com/api/chat"

# JSON payload
payload = {
    "message": "hy",
    "history": [
        {"content": "Hello! How can I help you today?", "isUser": False},
        {"content": "hy", "isUser": True}
    ],
    "userId": "user_12345"
}

# Headers
headers = {
    "Content-Type": "application/json"
}

# Send the POST request
response = requests.post(url, headers=headers, json=payload)

# Print the response
print("URL:", url)
print("Headers:", headers)
print("Payload:", json.dumps(payload))
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.text}")
