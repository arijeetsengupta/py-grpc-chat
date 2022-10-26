import json

CONFIG_PATH = "config.json"
data = {}

def get_server_config_from_json():

    with open(CONFIG_PATH) as json_file:
        data = json.load(json_file)["config"]
        return data["host"], data["port"]

