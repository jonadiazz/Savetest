import os
from _global import GlobalVars
import json

def getSuite(app_name):
    json_path = str(GlobalVars.SAVED_TESTS)+app_name+str(GlobalVars.JSON)
    _json = ''
    if os.path.isfile(json_path):
        with open(json_path, 'r') as json_file:
            _json = json.load(json_file)
        return _json[app_name]
    else: return None
