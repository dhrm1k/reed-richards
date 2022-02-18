import tweepy
import os

ck = os.environ["ck"]
cs = os.environ["cs"]

# Authenticate to Twitter
auth = tweepy.OAuthHandler(ck, cs)

ats = os.environ["ats"]
at = os.environ["at"]

auth.set_access_token(at, ats)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


# importing requests and json
import requests, json
# base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = "Ahmedabad"
# API key API_KEY = "Your API Key"
# upadting the URL
URL = BASE_URL + "q=" + CITY + "&appid=" + "API KEY"
# HTTP request
response = requests.get(URL)
# checking the status code of the request
if response.status_code == 200:
   # getting data in the json format
   data = response.json()
   # getting the main dict block
   main = data['main']
   # getting temperature
   tempfetched = main['temp'] - 273

  #Formatted temperature without decimal
   temperature = '{0:.2g}'.format(tempfetched)
  
   # getting the humidity
   humidity = main['humidity']
   # getting the pressure
   pressure = main['pressure']
   # weather report
   report = data['weather']
   print(f"{CITY:-^30}")
   print(f"Temperature: {temperature}")
   print(f"Humidity: {humidity}")
   print(f"Pressure: {pressure}")
   print(f"Weather Report: {report[0]['description']}")
else:
   # showing the error message
   print("Error in the HTTP request")




import schedule
import time
  
def func():
  api.update_status(
    (f"{CITY:-^30}""\n"
     f"Temperature: {temperature}""\n"
     f"Humidity: {humidity}""\n"
     f"Pressure: {pressure}""\n"
     f"Weather Report: {report[0]['description']}")
)
  
schedule.every(60).minutes.do(func)
  
while True:
    schedule.run_pending()
    time.sleep(60)
