import os
from _global import GlobalVars
import json

def getSuite(app_name, cases):
    json_path = str(GlobalVars.SAVED_TESTS)+app_name+str(GlobalVars.JSON)
    _json = ''
    if os.path.isfile(json_path):
        with open(json_path, 'r') as json_file:
            _json = json.load(json_file)
        if cases == []:
            return _json[app_name]
        else:
            c = -1
            ret = []
            for t in _json[app_name]:
                c += 1
                if c in cases:
                    ret.append(t)
            return ret
    else: return None
