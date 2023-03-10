from flask import Flask, render_template, request, redirect
import requests
import json
import datetime
import sys
import gen
from sys import stderr
from msg_app import send_message
from twilio.rest import Client
from msg_app import *
import time

app = Flask(__name__)

# Replace YOUR_API_KEY with your Yelp API key
API_KEY = "Kw3oLl3tz6AKaYRB-rVeDb37F_Jv_oqmll4XN7B87mMDIifOj9wMwAQxdNvj_-X8hwfb-47-LWnm1f2q03TN6PoVONJJnQg4R4cE2mEjdsNZmfQ9WWP1ZEGIAUvfY3Yx"


@app.route("/")
def rank():
    return render_template("rank.html")


phone = None
schedules=None
@app.route("/confirmation", methods=["GET", 'POST'])
def confirmation():
    global phone
    global schedules
    print(phone)
    if request.method == "POST":
        print("hello")
        myID = int(request.form.get('id'))
        print(myID)
        print(schedules[myID])
        texts = gen.to_string(schedules[myID])
        print("=============")
        # send_message(texts[0],phone)
        for t in texts:
            time.sleep(0.5)
            print(t)
            send_message(t ,phone)

            

    return render_template("confirmation.html")

@app.route("/", methods=["GET", "POST"])
def index():
    #print(request.method)
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

        return render_template("schedule.html", businesses=businesses, data=data, hours=hours_request, search_business=search_business, get_sample_schedule=get_sample_schedule)

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
            #print(data)
            results += get_info(data, cat)
    
    #print(results)
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
    return (0,0)


def get_sample_schedule(results, prefs):
    global schedules
    schedules = gen.generate(results)
    # schedules = gen.rank(schedules, ["art", "nature", "music", "bars", "history"])
    schedules = gen.rank(schedules, prefs)

    value = ""
    counter = 1
    temp = []
    for s in schedules:
        value += "Schedule " + str(counter) + ": \n"
        for e in s.getEvents():
            value += e.getName() + " from " + str(e.getTimeRange()[0]) + " to " + str(e.getTimeRange()[1]) + "\n"
            temp.append((e.getTimeRange()[0], e.getTimeRange()[1]))

        value += str(s.getPoints()) + " points total"
        value += "\n \n"
        counter += 1
    # return value
    print(schedules[0].getId())
    return schedules[0:201:100]

def get_open_hours(startHour, endHour):
    nine_am = 9 * 60
    startMins = (startHour // 100) * 60 + (startHour % 100) - nine_am
    endMins = (endHour // 100) * 60 + (endHour % 100) - nine_am
    return (startMins, endMins)

def get_info(data, cat):
    info_list = []
    counter=0
    hits=0
    # print(data["businesses"])
    try:
        for i in range(8):
            info_list.append((cat, hours_request(data["businesses"][counter]["id"]), data["businesses"][counter]["name"]))
            hits += 1
            counter+=1
        # (cat, hours_request(data["businesses"][0]["id"]), data["businesses"][0]["name"])#, data["businesses"][0]["url"])
        # print(info_list)
    except IndexError:
        pass
    return info_list

test_schedule = None

def format_time(time):
    minute=''+str(time%60)
    if(time%60<10):
        minute='0'+minute
    hour=(time-time%60)//60
    return str(int(hour+9)) +":"+minute

@app.route("/schedule", methods=["GET", "POST"])
def schedule():
    global phone
    location = request.form.get("location")
    # print(request.method)
    phone_number = request.form.get("phone")
    # print(request.method)
    # print(location)
    # print(phone_number)
    headers = {
            "accept": "application/json",
            "Authorization": "Bearer " + API_KEY
        }
    params = {
            "keyword": ['music','history','bars','nature','art'],
            "location": location
    }
    response = requests.get("https://api.yelp.com/v3/businesses/search", headers=headers, params=params)
    data = response.json()

    # Extract the relevant information from the API response
    businesses = data.get("businesses", [])
    #data = request.get_json()
    # print(request.method)
    #if request.method == "POST" or request.method == "GET":
        # Make the API request to Yelp
        
        #test_schedule = ('atlanta', [ 'music','history','bars','nature','art' ])

    location = request.form["location"]
    phone = request.form["phone_number"]
    list = [request.form["pref1"], request.form["pref2"], request.form["pref3"], request.form["pref4"], request.form["pref5"]]
    elements = {
        "6wb": "music",
        "7ax": "history",
        "7z4": "art",
        "6j7": "bars",
        "70x": "nature"
    }
    preferences = []
    for i in list:
        preferences.append(elements[i])
    print(preferences)

    # schedule_list = get_sample_schedule(search_business('new york city', ['music','history','bars','nature','art']))
    schedule_list = get_sample_schedule(search_business(location, preferences),preferences)

    print(location)
    return render_template("schedule.html",format_time=format_time, businesses=businesses,location=location, phone_number=phone_number, search_business=search_business, get_sample_schedule=get_sample_schedule, schedule_list=schedule_list)

# @app.route("/schedule", methods=["POST"])
# def schedule():
#     location = request.form["location"]
#     phone = request.form["phone_number"]
#     list = [request.form["pref1"], request.form["pref2"], request.form["pref3"], request.form["pref4"], request.form["pref5"]]
#     elements = {
#         "6wb": "music",
#         "7ax": "history",
#         "7z4": "art",
#         "6j7": "bars",
#         "70x": "nature"
#     }
#     preferences = []
#     for i in list:
#         preferences.append(elements[i])
#     print(preferences)
#     return render_template("schedule.html")

if __name__ == "__main__":
    app.run(debug=True)


