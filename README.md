# Take-home-exercise
This is the take home exercise for enview technologies backend role


# Driving Alert Service
This is a simple Flask application that provides two endpoints for handling driving events and alerts related to vehicle safety. The application stores recent vehicle data and triggers alerts based on specific conditions.

## Table of Contents

- [Introduction]
- [Getting Started]
  - [Prerequisites]
  - [Installation]
- [Endpoints]
  - [POST /post_data]
  - [GET /get_alert/{alert_id}]
- [Usage]
  - [Sending a Driving Event]
  - [Retrieving an Alert]
- [Alert Logic]
- [Contributing]
- [License]

## Introduction

The Driving Alert Service is a web application built using Flask that allows IoT devices to send driving events. The service checks for specific conditions in the received data and triggers alerts when necessary. Alerts are stored and can be retrieved using the provided endpoints.

## Getting Started

### Prerequisites

Before running the application, ensure you have the following installed:

- Python (3.6 or higher)
- Flask
- Postman (or any API testing tool)

## Endpoints

### POST /post_data

This endpoint allows IoT devices to send driving event data for processing. The service checks the data for specific conditions and triggers alerts if necessary.

#### Request

- Method: POST
- URL: `/post_data`
- Content-Type: application/json

Example request body:

json
{
  "vehicle_id": 1234,
  "timestamp": "2023-05-24T05:55:00+00:00",
  "location_type": "highway",
  "is_driving_safe": true
}


#### Response

- Status Code: 201 (Created) if an alert is triggered.
- Status Code: 200 (OK) if no alert is triggered.

Example response (if an alert is triggered):

json
{
  "message": "Alert triggered!",
  "alert_id": 1
}

### GET /get_alert/{alert_id}

This endpoint allows you to retrieve a specific alert by its `alert_id`.

#### Request

- Method: GET
- URL: `/get_alert/{alert_id}`

#### Response

- Status Code: 200 (OK) if the alert is found.
- Status Code: 404 (Not Found) if the alert does not exist.

Example response (if the alert is found):

json
{
  "alert_id": 1,
  "timestamp": "2023-05-24T05:55:00+00:00",
  "vehicle_id": 1234,
  "location_type": "highway",
  "resolved": false
}

## Usage

### Sending a Driving Event

To send a driving event, use an API testing tool like Postman or send a POST request to `http://localhost:5000/post_data` with the following JSON data:

json
{
  "vehicle_id": 1234,
  "timestamp": "2023-05-24T05:55:00+00:00",
  "location_type": "highway",
  "is_driving_safe": true
}


### Retrieving an Alert

To retrieve an alert by its `alert_id`, send a GET request to `http://localhost:5000/get_alert/{alert_id}`. Replace `{alert_id}` with the ID of the alert you want to retrieve.

## Alert Logic

The application checks for alerts based on specific conditions related to the `location_type` field in the received data. If the conditions are met, an alert is triggered and stored.

- For "highway" location: At least 4 consecutive unsafe driving events in the last 5 received events.
- For "city_center" location: At least 3 consecutive unsafe driving events.
- For "commercial" location: At least 2 consecutive unsafe driving events.
- For "residential" location: At least 1 consecutive unsafe driving event.
- For other location types: At least 4 consecutive unsafe driving events.


