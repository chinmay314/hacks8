from flask import Flask, render_template, request
import requests
import json
import datetime

app = Flask(__name__)

# Replace YOUR_API_KEY with your Yelp API key
API_KEY = "G0Sc2cgk4qWgBTWY4B17uUaYfaX6YbqnFBwm1KtuqQW25MzaMKPJJY50tJsybkJjnX3ZuoVsEVEK2tlsLlisA5tuV7gBFCE7rFP5_dq01VNrZZW4vgwidCFN5sjdY3Yx"

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

        return render_template("index.html", businesses=businesses, data=data, hours=hours_request)

    return render_template("index.html")

def hours_request(id):
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + API_KEY
    }
    url = "https://api.yelp.com/v3/businesses/" + id
    response_b = requests.get("https://api.yelp.com/v3/businesses/" + id, headers=headers)
    data_b = response_b.json()
    day = datetime.datetime.now().weekday()
    open = next((hour for hour in data_b['hours'][-1]['open'] if hour['day'] == day), None) #add error handling if closed
    # open = data_b['hours'][-1]['open']
    if(open != None):
        return (int(open['start']), int(open['end']))
    return 'Hours not available'

if __name__ == "__main__":
    app.run(debug=True)
