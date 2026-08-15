import sqlite3

conn = sqlite3.connect("transport.db")
cursor = conn.cursor()

# Create buses table
cursor.execute("""
CREATE TABLE IF NOT EXISTS buses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bus_no TEXT,
    route TEXT,
    status TEXT,
    latitude REAL,
    longitude REAL
)
""")

# Clear old data (optional)
cursor.execute("DELETE FROM buses")

# Default buses
buses = [
    ("101", "Bus Stand → Railway Station", "Running", 11.0168, 76.9558),
    ("205", "Market → College", "Running", 11.0300, 76.9800),
    ("309", "Hospital → Airport", "Stopped", 10.9950, 76.9400),
    ("TN38-101", "Coimbatore → Ooty", "Running", 11.4064, 76.6932),
    ("TN39-201", "Tiruppur → Coimbatore", "Running", 11.1085, 77.3411),
    ("TN30-301", "Salem → Singanallur", "Running", 11.6643, 78.1460)
]

cursor.executemany("""
INSERT INTO buses
(bus_no, route, status, latitude, longitude)
VALUES (?, ?, ?, ?, ?)
""", buses)

conn.commit()
conn.close()

print("Database created successfully!")