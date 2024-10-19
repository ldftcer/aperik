from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/send_data', methods=['POST'])
def receive_data():
    data = request.json
    ip = data.get('ip')
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    screenshot = data.get('screenshot')

    # Вывод данных для проверки
    print(f"IP: {ip}, Latitude: {latitude}, Longitude: {longitude}")
    with open('screenshot.png', 'wb') as f:
        f.write(screenshot.split(',')[1].encode('utf-8'))

    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(debug=True)
