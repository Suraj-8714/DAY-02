import pandas as pd
import requests



def fetch_iss_data():
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        latitude = data['iss_position']['latitude']
        longitude = data['iss_position']['longitude']
        timestamp = data['timestamp'] 
        return {
            'timestamp': timestamp, 
            'longitude': longitude,
            'latitude': latitude
            }
    
    else:
        print("Failed to fetch data")


def main():
    records_needed = 100
    records_collected = 0
    iss_data =[]
    
            
