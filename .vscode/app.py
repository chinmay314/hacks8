from flask import Flask, render_template, request
import requests
import json

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

        # hours_open = {}
        # for business in businesses:
        #     # Make the API request to Yelp
            # headers = {
            #     "accept": "application/json",
            #     "Authorization": "Bearer " + API_KEY
            # }
            # response_b = requests.get("https://api.yelp.com/v3/businesses/search" + business.id, headers=headers, params=params)
            # data_b = response_b.json()
            # hours_open[business.name] = data_b

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
    open = data_b['hours'][-1]['is_open_now']
    return open

if __name__ == "__main__":
    app.run(debug=True)
