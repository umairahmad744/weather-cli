import requests
import pandas as pd
from datetime import datetime

# Your API key
API_KEY = "8b6a24d448a8347765bea052d45130ea" #use your own beacuse i delete this Thanks

# Ask user for city
city = input("Enter city name: ")

# Build URL
URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# Call API
response = requests.get(URL)

if response.status_code == 200:  # Success
    data = response.json()
    
    # Parse data
    city_name = data["name"]
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"📍 {city_name} | 🌡️ {temp}°C | ☁️ {desc}")
    
    # Save to CSV
    weather_data = pd.DataFrame([[time, city_name, temp, desc]], 
                                 columns=["Time", "City", "Temperature", "Description"])
    
    weather_data.to_csv("weather_log.csv", mode="a", index=False, header=False)
    print("Data saved to weather_log.csv")
    
else:  # Error
    print("Error:", response.json())
