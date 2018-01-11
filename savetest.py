import os, sys
import subprocess
import json
import _global_variables as gv
import _st_symbols as sts
import time
import signal

args = sys.argv
app_name, extension = args[2].split('.')
command = args[1]
script = args[2]

def handler(s,f):
    print '\t\tTLE',
    raise Exception()


def get_JSON():
    json_path = gv.SAVED_TESTS+app_name+gv.JSON
    _json = ''
    if os.path.isfile(json_path):
        with open(json_path, 'r') as json_file:
            _json = json.load(json_file)
        return _json
    else: return None


signal.signal(signal.SIGALRM, handler)

tsn = 'test case number'
aat = 'average application time'
tct = 'test case time'
if get_JSON() is not None:
    tsn = 0
    aat = 0
    for test_case in get_JSON()[app_name]:
        if test_case==[]: continue
        print sts.running+"running {0} with test case {1}\n".format(script, tsn)
        test = ''
        for x in test_case:
            test = test +x+'\n'
            print '\t\t'+x+'\n',

        r = 'response'
        signal.alarm(2)
        itime = time.time()
        try:
            ec = subprocess.Popen(['echo', test], stdout=subprocess.PIPE)
            r = subprocess.check_output(['pypy', script], stdin=ec.stdout)
        except Exception, exc:
            r = exc
        etime = time.time()
        signal.alarm(0)

        tct = int(1000 * (etime-itime))
        aat += tct
        print '\t\t', r
        print "\t\t{0} ms".format(tct)
        tsn += 1

    if tsn==0: aat = tct
    else: aat = aat / tsn

ms = 'ms'
if int(aat)>1000: ms = 'ms (not so much milisecons anymore!)'
print '\nAverage application time (AAT) is {0} {1}\n'.format(aat, ms)

