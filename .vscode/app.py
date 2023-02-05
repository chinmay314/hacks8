from flask import Flask, render_template, request
import requests
import json
import datetime
import sys
import gen
from sys import stderr

app = Flask(__name__)

# Replace YOUR_API_KEY with your Yelp API key
API_KEY = "G0Sc2cgk4qWgBTWY4B17uUaYfaX6YbqnFBwm1KtuqQW25MzaMKPJJY50tJsybkJjnX3ZuoVsEVEK2tlsLlisA5tuV7gBFCE7rFP5_dq01VNrZZW4vgwidCFN5sjdY3Yx"


@app.route("/index")
def rank():
    return render_template("index.html")

@app.route("/schedule", methods=["POST"])
def schedule():
    location = request.form['location']
    phone_number = request.form['phone_number']
    print(location)
    print(phone_number)
    return render_template("schedule.html")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        location = request.form.get("location")
        keyword = request.form.get("keyword")

        # Make the API request to Yelp
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer " + API_KEY
        }
        params = {
            "term": keyword,
            "location": location
        }
        response = requests.get("https://api.yelp.com/v3/businesses/search", headers=headers, params=params)
        data = response.json()

        # Extract the relevant information from the API response
        businesses = data.get("businesses", [])

        return render_template("index.html", businesses=businesses, data=data, hours=hours_request, search_business=search_business, get_sample_schedule=get_sample_schedule)

    return render_template("rank.html")


startTime = []
endTime = []
event_names = []
event_urls =[]

def search_business(location, cats):
    results = []
    for cat in cats:
        if request.method == "POST":
            # Make the API request to Yelp
            headers = {
                "accept": "application/json",
                "Authorization": "Bearer " + API_KEY
            }
            params = {
                "term": cat,
                "location": location
            }
            response = requests.get("https://api.yelp.com/v3/businesses/search", headers=headers, params=params)
            data = response.json()
            # file=open('file.txt', 'w')
            # file.write(str(data))
            # file.close()
            # print(data) # remove later

            # Extract the relevant information from the API response
        results += get_info(data, cat)
    
    return results


def hours_request(id):
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + API_KEY
    }
    url = "https://api.yelp.com/v3/businesses/" + id
    response_b = requests.get("https://api.yelp.com/v3/businesses/" + id, headers=headers)
    data_b = response_b.json()
    day = datetime.datetime.now().weekday()
    open = None
    if('hours' in data_b):
        open = next((hour for hour in data_b['hours'][-1]['open'] if hour['day'] == day), None) #add error handling if closed
    # open = data_b['hours'][-1]['open']
    #print(data_b["categories"])
    if(open != None):
        return get_open_hours(int(open['start']), int(open['end']))
    return (0, 0)


def get_sample_schedule(results):
    schedules = gen.generate(results)
    schedules = gen.rank(schedules, ["art", "nature", "music", "bars", "history"])
    value = ""
    counter = 1
    for s in schedules:
        points = s[0]
        s = s[1]
        value += "Schedule " + str(counter) + ": \n"
        for e in s.getEvents():
            value += e.getName() + " from " + str(e.getTimeRange()[0]) + " to " + str(e.getTimeRange()[1]) + "\n"
            startTime.append(e.getTimeRange()[0])
            endTime.append(e.getTimeRange()[1])
            event_names.append(e.getName())
            event_urls
        value += str(points) + " points total"
        value += "\n \n"
        counter += 1
    return value

def get_open_hours(startHour, endHour):
    nine_am = 9 * 60
    startMins = (startHour // 100) * 60 + (startHour % 100) - nine_am
    endMins = (endHour // 100) * 60 + (endHour % 100) - nine_am
    return (startMins, endMins)

def get_info(data, cat):
    info_list = []
    for i in range(5):
        info_list.append((cat, hours_request(data["businesses"][i]["id"]), data["businesses"][i]["name"]))
     #(cat, hours_request(data["businesses"][0]["id"]), data["businesses"][0]["name"])#, data["businesses"][0]["url"])
    #print(info_list)
    return info_list



"""
Variables needed to be pulled:
- start time, end time
- event name
- url
"""

if __name__ == "__main__":
    app.run(debug=True)


