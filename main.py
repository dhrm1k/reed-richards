import os
import flask
from replit import db, web
import tweepy
import os
import schedule
import time
import requests, json


# -- Create & configure Flask application.
app = flask.Flask(__name__)
app.static_url_path = "/static"

users = web.UserStore()

@app.route("/")
def index():
  return '''<h1>It works</h1>'''

web.run(app)

db["ck"] = os.environ['ck']
db["cs"] = os.environ['cs']
db["ats"] = os.environ['ats']
db["at"] = os.environ['at']
db["api_key"] = os.environ['api_key']

value1 = db["ck"] 
value2 = db["cs"]

auth = tweepy.OAuthHandler(value1, value2)

value3 = db['ats']
value4 = db['at']

auth.set_access_token(value4, value3)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = "Ahmedabad"
value5 = db['api_key']
# upadting the URL
URL = BASE_URL + "q=" + CITY + "&appid=" + value5
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
