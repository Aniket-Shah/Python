import requests
import json
import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")
city = input("Enter the name of the city:\n")
url = f"https://api.weatherapi.com/v1/current.json?key=2e84371dffcb4271a1a135324242503&q={city}"
r= requests.get(url)
wdic = json.loads(r.text)
temperture=wdic["current"]["temp_c"]
windSpeed=wdic["current"]["wind_kph"]
pressure=wdic["current"]["pressure_in"]
humidity=wdic["current"]["humidity"]
speak.Speak(f"Today {city} Temperature is {temperture} degrees Celsius and wind is blowing at a speed of {windSpeed} kilometer per hour and pressure is {pressure} per inche and humidity is {humidity}%")
