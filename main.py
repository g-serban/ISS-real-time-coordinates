import requests
from time import strftime

def get_iss_position():
    # Get current ISS position
    req_iss = requests.get('http://api.open-notify.org/iss-now.json')
    dict = req_iss.json()
    lat_lng = dict['iss_position']
    # save the current ISS  possition in new variables
    lat_iss = float(lat_lng['latitude'])
    lng_iss = float(lat_lng['longitude'])
    date_time = strftime('%I:%M:%S %p')
    print(f'ISS current latitude coord: {lat_iss} at {date_time}')
    print(f'ISS Current longitute coord: {lng_iss} at {date_time}')
    
get_iss_position()
