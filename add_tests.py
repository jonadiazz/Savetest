import json
import os, sys
import _prompts as P
from _global import GlobalVars

def addTests(app_name):
    filename = 'path_to_store_tests'
    ui = 'all_user_input'

    filename = str(GlobalVars.SAVED_TESTS)+app_name+str(GlobalVars.JSON)
    ui = list()

    while True:
        print("{0}User input for TEST {1}\n".format(P.prompt, len(ui)))
        user_input = 'user_input_line'
        test_i = list()
        while True:
            user_input = input('\t').strip().split('\n')
            if ''==user_input[0] or 'save()' in user_input[0]:
                break
            test_i.append(user_input[0])
        if test_i != []: ui.append(test_i)
        if 'save()' in user_input: break

    cases = dict()
    cases[app_name] = ui

    '''if there is no file then create it'''
    access_level = 'r+'
    if not os.path.isfile(filename): access_level = 'w+'

    if access_level == 'w+':
        with open(filename, access_level) as storage:
            json.dump(cases, storage)
    else:
        with open(filename, access_level) as storage:
            cpy_storage = json.load(storage)
            for i in ui:
                if not i in cpy_storage[app_name]:
                    cpy_storage[app_name].append(i)
            storage.seek(0)
            storage.write(json.dumps(cpy_storage))
            storage.truncate()

    return '\n'+filename+'\n'
