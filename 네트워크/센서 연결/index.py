from flask import Flask, request,render_template, jsonify
import MariaDB
import DHT11

app = Flask(__name__)
store = MariaDB.MariaDB()
data = DHT11.DHT11()

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/api/now')
def insertdb():
    temp, hum = data.getNow()
    result = store.add(temp,hum)
    return result

@app.route('/api/record')
def selectAll():
    result = store.selectAll()
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
