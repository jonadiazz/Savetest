import _prompts as P
import subprocess
import signal
import time


# Time out handler
def _handler(self):
    print '\t\tTLE',
    raise Exception()


def runTests(testsuite, script):
    signal.signal(signal.SIGALRM, _handler)

    tsn = 'test case number'
    aat = 'average application time'
    tct = 'test case time'
    tsn, aat = 0, 0
    for test_case in testsuite:
        if test_case==[]: continue
        print P.running+"running {0} with test case {1}\n".format(script, tsn)
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
    return '\nAverage application time (AAT) is {0} {1}\n'.format(aat, ms)
