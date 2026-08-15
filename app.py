from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# ---------------- HOME PAGE ----------------

@app.route("/")
def home():

    conn = sqlite3.connect("transport.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM buses")
    buses = cursor.fetchall()

    total = len(buses)
    running = sum(1 for bus in buses if bus["status"] == "Running")
    stopped = total - running

    conn.close()

    return render_template(
        "index.html",
        buses=buses,
        total=total,
        running=running,
        stopped=stopped
    )


# ---------------- ADMIN PAGE ----------------

@app.route("/admin")
def admin():

    conn = sqlite3.connect("transport.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM buses")
    buses = cursor.fetchall()

    conn.close()

    return render_template("admin.html", buses=buses)


# ---------------- ADD BUS ----------------

@app.route("/add", methods=["POST"])
def add():

    bus_no = request.form["bus_no"]
    route = request.form["route"]
    status = request.form["status"]
    latitude = float(request.form["latitude"])
    longitude = float(request.form["longitude"])

    conn = sqlite3.connect("transport.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO buses
        (bus_no, route, status, latitude, longitude)
        VALUES (?, ?, ?, ?, ?)
    """, (bus_no, route, status, latitude, longitude))

    conn.commit()
    conn.close()

    return redirect("/admin")


if __name__ == "__main__":
    app.run(debug=True)