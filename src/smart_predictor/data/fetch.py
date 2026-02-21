import requests 

eia_url = "https://api.eia.gov/v2/electricity/rto/region-data/data/?frequency=hourly&data[0]=value&start=2024-01-01T00&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000"

response = requests.get(eia_url)

# Check request status 
if response.status_code == 200:
    data = response.json()
else:
    print(f"Request failed with status {response.status_code}")
    


