from flask import Flask, request, jsonify
from collections import defaultdict


app = Flask(__name__)

vehicle_data = defaultdict(list)
alerts = []

def check_alert(vehicle_id, location_type):
    recent_data = vehicle_data[vehicle_id]

    if location_type == "highway":
        required_false_conditions = 4
    elif location_type == "city_center":
        required_false_conditions = 3
    elif location_type == "commercial":
        required_false_conditions = 2
    elif location_type == "residential":
        required_false_conditions = 1
    else:
        required_false_conditions = 4

    if len(recent_data) >= 5 and all(data['location_type'] == location_type for data in recent_data[-5:]):
        false_condition_count = sum(1 for data in recent_data[-5:] if not data['is_driving_safe'])

        if false_condition_count >= required_false_conditions:
            return True


    return False


#post method endpoint
@app.route('/post_data', methods=['POST'])
def post_data():
    data = request.get_json()
    #fetching data from the request
    vehicle_id = data.get('vehicle_id')
    location_type = data.get('location_type')

    vehicle_data[vehicle_id].append(data)

    vehicle_data[vehicle_id] = vehicle_data[vehicle_id][-5:]

    if check_alert(vehicle_id, location_type):
        alert_id = len(alerts) + 1


        # Create an alert object
        alert = {
            'alert_id': alert_id,
            'timestamp': data.get('timestamp'),
            'vehicle_id': vehicle_id,
            'location_type': location_type,
            'resolved': False
        }
        # Add the alert to the alerts list
        alerts.append(alert)
        return jsonify({"message": "Alert triggered!", "alert_id": alert_id}), 201
    else:
        return jsonify({"message": "Data received."}), 200


# GET endpoint to retrieve an alert by alert_id
@app.route('/get_alert/<int:alert_id>', methods=['GET'])
def get_alert(alert_id):
    for alert in alerts:
        if alert['alert_id'] == alert_id:
            return jsonify(alert)
    return jsonify({"message": "Alert not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
