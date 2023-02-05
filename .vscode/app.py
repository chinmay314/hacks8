from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace YOUR_API_KEY with your Yelp API key
API_KEY = "G0Sc2cgk4qWgBTWY4B17uUaYfaX6YbqnFBwm1KtuqQW25MzaMKPJJY50tJsybkJjnX3ZuoVsEVEK2tlsLlisA5tuV7gBFCE7rFP5_dq01VNrZZW4vgwidCFN5sjdY3Yx"

@app.route("/index")
def rank():
    return render_template("index.html")

@app.route("/schedule", methods=["POST"])
def schedule():
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
    return render_template("schedule.html")

@app.route("/confirmation", methods=["GET"])
def confirmation():
    return render_template("confirmation.html")
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

        return render_template("index.html", businesses=businesses)

    return render_template("rank.html")

if __name__ == "__main__":
    app.run(debug=True)
