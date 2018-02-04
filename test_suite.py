import os
from _global import GlobalVars
import json

class TestSuite:
    def __init__(self, app_name):
        self.app_name = app_name
        self.json_path = str(GlobalVars.SAVED_TESTS)+app_name+str(GlobalVars.JSON)
        self._json = ''

    def getSuite(self, cases):
        if os.path.isfile(self.json_path):
            with open(self.json_path, 'r') as json_file:
                '''copy then close the file'''
                self._json = json.load(json_file)
            if cases == []:
                return self._json[self.app_name], self._json['count']
            else:
                ret = dict()
                for i in cases:
                    i = str(i)
                    try:
                        ret[i] = self._json[self.app_name][i]
                    except KeyError as e:
                        print('KeyError:',e)
                return ret, self._json['count']
        else: return None, None


    def saveOutput(self, output):
        try:
            with open(self.json_path, 'r+') as json_file:
                cpy_json = json.load(json_file)
                for k,v in output.items():
                    cpy_json[self.app_name][k]['output'] = v
                json_file.seek(0)
                json_file.write(json.dumps(cpy_json))
                json_file.truncate()
            return 'Output saved, use `attest` command to verify outputs are correct.'
        except:
            return 'An error occurred, couldn\' save output.'


    def setPassing(self, passing):
        if os.path.isfile(self.json_path):
            with open(self.json_path, 'r+') as json_file:
                cpy_json = json.load(json_file)
                for e in passing:
                    e = str(e)
                    try:
                        cpy_json[self.app_name][e]['passing'] = True
                        cpy_json[self.app_name][e]['expected'] = cpy_json[self.app_name][e]['output']
                    except KeyError as e:
                        print('Testcase does not exist',e)
                json_file.seek(0)
                json_file.write(json.dumps(cpy_json))
                json_file.truncate()
                return '\nSuccessfully set passing flags, congrats!'
        return "None test cases saved"
