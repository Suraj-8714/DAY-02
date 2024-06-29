import requests

# URL
url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    # Extract 
    latitude = data['iss_position']['latitude']
    longitude = data['iss_position']['longitude']
    timestamp = data['timestamp']
    
    print("Latitude: {latitude}")
    print("Longitude: {longitude}")
    print("Timestamp: {timestamp}")
else:
    print("Error cant Fetch")
