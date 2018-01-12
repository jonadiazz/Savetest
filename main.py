from options import Options
from commands import Commands
import _prompts as P
import sys
from run_tests import runTests
from add_tests import addTests
from get_suite import getSuite

args = sys.argv
v = 'verbose flag'
v = 0
if str(Options.VERBOSE) in args: v = 1
if str(Options.VERSION) in args:
    print '--version'
elif len(args)<3:
    print P.usage
    print P.usage_ext+'\n'
    print P.usage_ext2+'\n'
    print P.usage_ext3+'\n'
    quit()

app_name, extension = args[2].split('.')
command = args[1]
script = args[2]

if command == str(Commands.RUN):
    testsuite = getSuite(app_name)
    if testsuite is not None:
        ret = runTests(testsuite, script)
        if v: print ret
    else:
        print P.need_tests
        print P.usage
elif command == str(Commands.ADD):
    ret = addTests(app_name)
    if v: print ret
