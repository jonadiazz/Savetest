import json
import os, sys
import _st_symbols as sts
import _global_variables as gv

n_args = len(sys.argv)
if n_args<3:
    print sts.usage
    print sts.options+'\n'
    quit()

v = 1
if n_args>3:
    if '--v' in sys.argv[3]: v = 0

if v: print sts.tips+sts.use
app_name, extension = sys.argv[2].split('.')
filename = gv.SAVED_TESTS+app_name+gv.JSON

ui = list()

while True:
    print "{0}User input for TEST {1}\n".format(sts.prompt, len(ui))
    user_input = 'user_input_line'
    test_i = list()
    while True:
        user_input = raw_input('\t').strip().split('\n')
        if ''==user_input[0] or 'save()' in user_input[0]:
            break
        test_i.append(user_input[0])
    ui.append(test_i)
    if 'save()' in user_input: break

cases = dict()
cases[app_name] = ui

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
