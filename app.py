from flask import Flask, render_template, request
import yaml

import conversions

app = Flask(__name__)

favourites = {}
with open("favourites.yml", "r") as fav_fp:
    favourites = yaml.safe_load(fav_fp)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", favourites=favourites)

@app.route("/apt")
def apt():
    return render_template("apt.html")

@app.route("/bash")
def bash():
    return render_template("bash.html")

@app.route("/docker")
def docker():
    return render_template("docker.html")

@app.route("/git")
def git():
    return render_template("git.html")

@app.route("/pandas")
def pandas():
    return render_template("pandas.html")

@app.route("/python")
def python():
    return render_template("python.html")

@app.route("/vscode")
def vscode():
    return render_template("vscode.html")

@app.route("/mgrs-lat-lon", methods=("GET", "POST"))
def mgrs_lat_lon():
    if request.method == "POST":
        mgrs_coord = request.form["mgrs_coord"]
        lat_coord = request.form["lat_coord"]
        lon_coord = request.form["lon_coord"]

        coordinate_vars = conversions.convert_mgrs_lat_lon(mgrs_coord, lat_coord, lon_coord)
        return render_template("mgrs-lat-lon-conversion.html", **coordinate_vars)
    else:
        return render_template("mgrs-lat-lon-conversion.html")
    
@app.route("/metres-feet", methods=("GET", "POST"))
def metres_feet():
    if request.method == "POST":
        metres = request.form["metres"]
        feet = request.form["feet"]

        distance_vars = conversions.convert_m_ft(metres, feet)
        return render_template("metres-feet-conversion.html", **distance_vars)
    else:
        return render_template("metres-feet-conversion.html")
    
@app.route("/timezones")
def timezones():
    return render_template("time-conversion.html")

@app.route("/epoch-date", methods=("GET", "POST"))
def epoch_date():
    if request.method == "POST":
        epoch_time = request.form["epoch_time"]
        date_time = request.form["date_time"]

        epoch_vars = conversions.convert_epoch_date(epoch_time, date_time)
        return render_template("epoch-date-conversion.html", **epoch_vars)
    else:
        return render_template("epoch-date-conversion.html")

if __name__ == "__main__":
    app.run(debug=True)
