from flask import Flask, render_template, request

import conversions

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/apt")
def apt():
    return render_template("apt.html")

@app.route("/bash")
def bash():
    return render_template("bash.html")

@app.route("/docker")
def docker():
    return render_template("docker.html")

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

if __name__ == "__main__":
    app.run(debug=True)