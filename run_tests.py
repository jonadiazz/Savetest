from checker_log import CheckerLogs
import resource
import _prompts as P
import subprocess
import signal
import time


# Time out handler
def _handler(self):
    print('\t\tTLE', end=' ')
    raise Exception()


def runTests(testsuite, script, interpreter):
    signal.signal(signal.SIGALRM, _handler)

    checker = CheckerLogs()
    output = dict()
    tsn = 'test case number'
    aat = 'average application time'
    tct = 'test case time'
    tsn, aat = 0, 0
    for tsn in testsuite:
        test_case = testsuite[tsn]['input']
        passing = testsuite[tsn]['passing']
        expected = testsuite[tsn]['expected']

        if test_case==[]: continue
        test = ''
        tmp = ''
        dump = {'Testcase':'', 'Output':'', 'Expected':''}
        for t in test_case:
            test = test+t+'\n'
            tmp += '\t'+t+'\n'
        dump['Testcase'] = tmp

        r = 'response'
        signal.alarm(2)
        itime = time.time()
        try:
            ec = subprocess.Popen(['echo', test], stdout=subprocess.PIPE)
            if interpreter=='':
                r = subprocess.check_output(["./"+script], stdin=ec.stdout)
            else:
                r = subprocess.check_output([interpreter, script], stdin=ec.stdout)
            if type(r)!=type(0) and type(r)!=type(""):
                r = r.decode("utf-8").strip()
        except subprocess.CalledProcessError as exc:
            print("\n\t\tThere was an error, verify your program runs smoothly with some basic input.")
            continue
        etime = time.time()
        signal.alarm(0)

        tct = int(1000 * (etime-itime))
        aat += tct
        output[tsn] = str(r)
        verdict = ""
        if passing:
            verdict = "OK" if output[tsn] == expected else "FAIL"
        else: verdict = "None: needs attest"

        dump['Output'] = output[tsn]
        dump['Expected'] = expected
        checker.logIt(dump, tsn, tct, verdict)

    for i in checker.logs: print(i)
    aat = checker.getAverageApplicationTime()

    ms = 'ms'
    if int(aat)>1000: ms = 'ms (not so -miliseconds- anymore!)'
    print('\nAverage application time (AAT) is {0:.2f} {1}\n'.format(aat, ms))
    return output, checker.accepted


# TODO: to check memory usage 
# p = subprocess.Popen("./a.out")
# p.wait()
# print(resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss)
