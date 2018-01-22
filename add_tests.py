import json
import os, sys
import _prompts as P
from _global import GlobalVars
from utils.testcase import TestCase

def merge_two_dicts(x, y):
    """Given two dicts, merge them into a new dict as a shallow copy."""
    z = x.copy()
    z.update(y)
    return z

def addTests(app_name):
    filename = 'path_to_store_tests'
    ui = 'all_user_input'

    filename = str(GlobalVars.SAVED_TESTS)+app_name+str(GlobalVars.JSON)
    ui = dict()

    '''set access level, if there is no file it will create it'''
    count = 'also, get count of tests from file if it exists'
    access_level = 'r+'
    if not os.path.isfile(filename):
        access_level = 'w+'
        count = 0
    else:
        with open(filename, access_level) as storage:
            count = json.load(storage).get('count',0)


    while True:
        print("{0}User input for TEST {1}\n".format(P.prompt, len(ui)))
        user_input = 'user_input_line'
        test_i = list()
        while True:
            user_input = input('\t').strip().split('\n')
            if ''==user_input[0] or 'save()' in user_input[0]:
                break
            test_i.append(user_input[0])
        if test_i != []:
            ui[count] = TestCase.newInstance(test_i)
            count += 1
        if 'save()' in user_input: break

    cases = dict()
    cases[app_name] = ui
    cases['count'] = count


    if access_level == 'w+':
        with open(filename, access_level) as storage:
            json.dump(cases, storage)
    else:
        with open(filename, access_level) as storage:
            cpy_storage = json.load(storage)
            t = dict()
            t['count'] = count
            t[app_name] = merge_two_dicts(cpy_storage[app_name], cases[app_name])
            storage.seek(0)
            storage.write(json.dumps(t))
            storage.truncate()

    return '\n'+filename+'\n'
