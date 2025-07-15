from flask import Flask, request, jsonify

app = Flask(__name__)
data_store = {}

@app.route('/', methods=['GET'])
def index():
    return "API REST para ESP32 funcionando"

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        json_data = request.get_json()
        data_store.update(json_data)
        return jsonify({"status": "ok", "data": data_store})
    return jsonify(data_store)
