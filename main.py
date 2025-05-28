from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route("/clima", methods=["GET"])
def clima():
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temperature = data["current_weather"]["temperature"]
        return jsonify(temperature)
    else:
        return jsonify({'error': 'No se pudo obtener el clima'}), 500

@app.route("/pais", methods=["GET"])
def pais():
    name = request.args.get("name")
    url = f'https://restcountries.com/v3.1/name/{name}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()[0]
        capital = data['capital'][0]
        lat, lon = data['capitalInfo']['latlng']
        return jsonify([capital, lat, lon])
    else:
        return jsonify({'error': 'No se pudo obtener el país'}), 500

@app.route("/consejo", methods=["GET"])
def consejo():
    response = requests.get('https://api.adviceslip.com/advice')
    if response.status_code == 200:
        data = response.json()
        consejo = data['slip']['advice']
        return jsonify({'consejo': consejo})
    else:
        return jsonify({'error': 'No se pudo obtener el consejo'}), 500

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
