from utils.bcolors import bColors as C
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
        if passing:
            if output[tsn] == expected:
                print(C.OKGREEN+"passing\t"+C.ENDC+output[tsn])
            else: print(C.FAIL+"failing\t"+C.ENDC+output[tsn]+C.FAIL+' -> expected: '+expected+C.ENDC)
        else: print(C.WARNING+"attest\t\t"+C.ENDC+output[tsn])
        print("\t\t{0} ms".format(tct))

    if tsn==0: aat = tct
    else: aat = aat / (int(tsn)+1)

    ms = 'ms'
    if int(aat)>1000: ms = 'ms (not so -miliseconds- anymore!)'
    return output, '\nAverage application time (AAT) is {0:.2f} {1}\n'.format(aat, ms)


# TODO: to check memory usage 
# p = subprocess.Popen("./a.out")
# p.wait()
# print(resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss)
