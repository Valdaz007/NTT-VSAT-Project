from flask import Flask, jsonify
from db import DB
import json, time

api_key = 123456
db = DB()

app = Flask(__name__)

@app.route("/betatest", methods = ['GET'])
def betatest():
    data_set = {'Page:': 'betatest', 'Msg': 'Hello', 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)
    return json_dump

@app.route("/getmapmarkerdata")
def getMapMarkerData():
    data_set = db.pull_Site(tbl_Name = "vsat")
    if data_set == False:
        return {"Msg": "DB Error!!!"}
    else:
        return jsonify(data_set)

@app.route("/getprovincedata")
def getProvinceData():
    data_set = db.pull_Site(tbl_Name = "province")
    if data_set == False:
        return {"Msg": "DB Error!!!"}
    else:
        return jsonify(data_set)

if __name__ == '__main__':
    app.run(debug=True)