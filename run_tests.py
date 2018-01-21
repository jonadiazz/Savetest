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

    tsn = 'test case number'
    aat = 'average application time'
    tct = 'test case time'
    tsn, aat = 0, 0
    for test_case in testsuite:
        if test_case==[]: continue
        print(P.running+"running {0} with test case {1}\n".format(script, tsn))
        test = ''
        for x in test_case:
            test = test +x+'\n'
            print('\t\t'+x+'\n', end=' ')

        r = 'response'
        signal.alarm(2)
        itime = time.time()
        try:
            ec = subprocess.Popen(['echo', test], stdout=subprocess.PIPE)
            r = subprocess.check_output([interpreter, script], stdin=ec.stdout)
        except Exception as exc:
            r = exc
        etime = time.time()
        signal.alarm(0)

        tct = int(1000 * (etime-itime))
        aat += tct
        r = '\n' + str(r)
        print('\n\t\t'.join(r.split('\n')))
        print("\t\t{0} ms".format(tct))
        tsn += 1

    if tsn==0: aat = tct
    else: aat = aat / tsn

    ms = 'ms'
    if int(aat)>1000: ms = 'ms (not so -miliseconds- anymore!)'
    return '\nAverage application time (AAT) is {0} {1}\n'.format(aat, ms)


# TODO: to check memory usage 
# p = subprocess.Popen("./a.out")
# p.wait()
# print(resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss)
