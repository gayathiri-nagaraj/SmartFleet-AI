# 🚌 SmartFleet-AI

### AI-Enabled Smart Public Transport Tracking & Smart Stop Request System

SmartFleet-AI is a smart public transport management system designed for small and developing cities. It helps passengers find and track buses while providing transport operators with a simple system to monitor bus locations and status.

## 🚨 Problem

Public transport users in small cities often face difficulties such as:

- Not knowing the current location of buses
- Waiting at bus stops without knowing when a bus will arrive
- Missing buses while trying to chase or catch a moving bus
- Lack of real-time transport information
- Difficulty for transport operators to monitor buses efficiently

## 💡 Our Solution

SmartFleet-AI combines **real-time bus tracking** with a unique **Smart Stop Request** feature.

Passengers can search for a required bus and use the **Identify / Smart Stop Request** feature. The request can notify the respective bus driver that a passenger is waiting at a particular stop.

This helps the driver identify the requested stop and safely stop to pick up passengers instead of passengers trying to chase or board a moving bus.

## ⭐ Key Features

### 🗺️ Real-Time Bus Tracking
Displays available buses and their locations on an interactive map.

### 🔎 Bus Search
Passengers can search for a specific bus number and view its route and status.

### 🛑 Smart Stop Request
Passengers can request a bus to stop at their selected stop, helping reduce missed buses and unsafe boarding attempts.

### 📊 Transport Dashboard
Displays:

- Total buses
- Running buses
- Stopped buses
- Bus routes
- Bus status

### 👨‍💼 Admin Panel
Transport administrators can add and manage bus information including:

- Bus number
- Route
- Status
- Latitude
- Longitude

## 🏗️ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend programming |
| Flask | Web application framework |
| SQLite | Database |
| HTML | Web page structure |
| CSS | User interface design |
| JavaScript | Interactive features |
| Leaflet.js | Interactive map |
| OpenStreetMap | Map data |

## 🔄 System Workflow

```text
Passenger
    ↓
Search for Bus
    ↓
View Route & Live Location
    ↓
Select Required Bus
    ↓
Smart Stop Request
    ↓
Driver Receives Request
    ↓
Driver Identifies Requested Stop
    ↓
Bus Stops Safely
    ↓
Passenger Boards the Bus
```
## 🎯 Benefits
Reduces uncertainty while waiting for buses
Helps passengers find buses easily
Reduces unsafe attempts to board moving buses
Helps drivers identify passenger requests
Improves public transport convenience
Suitable for small and developing cities
Provides a simple and low-cost transport management solution

## 🚀 Future Enhancements

Future versions of SmartFleet-AI can include:

AI-based bus arrival prediction
GPS integration with live vehicle tracking
Mobile application for passengers
Driver mobile application
Push notifications
Digital Smart Stop Request system
Estimated Time of Arrival (ETA)
Route optimization
Traffic-aware arrival prediction
Analytics for transport operators

## 🖥️ Project Modules
Passenger Module

Passengers can search buses, view routes, check bus status and use the Smart Stop Request feature.

Driver Module

Drivers can receive passenger stop requests and identify the requested stop.

Admin Module

Administrators can manage bus details and monitor the transport system.

## 📌 Project Status

Prototype / Working Demonstration

The current prototype demonstrates bus management, bus search, route information, bus status and map-based bus location tracking using Flask, SQLite and Leaflet.

## 👩‍💻 Project

SmartFleet-AI

Developed as a smart public transportation solution for small cities.

## 🌱 Vision

Making public transportation smarter, safer and easier to access for everyone.
