import os
import sys
import json
from flask import Flask, request, jsonify

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.server.manager.data_manager import data_manager
from app.server.hubs.library.hub_list import hub_dict

app = Flask(__name__)


@app.route('/v1/<hub_uuid>')
def get_update_by_hub_uuid(hub_uuid: str):
    if hub_uuid not in hub_dict:
        print(f"NO HUB: {hub_uuid}")
        return "", 400
    app_info_list = json.loads(request.headers.get("App-Info-List"))
    return_list = data_manager.get_release_info_list(hub_uuid, app_info_list)
    return jsonify(return_list)


@app.route("/")
def hello():
    return "Hello World from Flask"


def run(debug=True):
    if debug:
        app.run(host='0.0.0.0', debug=True)
    else:
        app.run(host='0.0.0.0', debug=False, port=80)


if __name__ == "__main__":
    run(debug=False)
