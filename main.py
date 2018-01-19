from options import Options
from commands import Commands
import _prompts as P
import sys
from run_tests import runTests
from add_tests import addTests
from get_suite import getSuite
from parser import parseCommandArgs

args = sys.argv

v = 'verbose flag'
cases = 'cases to include from testsuite'
v, interpreter, cases = parseCommandArgs(args)

if str(Options.VERSION) in args: print '--version'
elif len(args)<3:
    print P.savetest
    print P.usage
    print P.usage_ext+'\n'
    print P.usage_ext2+'\n'
    print P.usage_ext3+'\n'
    print P.usage_ext4+'\n'
    print P.usage_ext5+'\n'
    quit()

app_name, extension = args[2].split('.')
command = args[1]
script = args[2]

if command == str(Commands.RUN):
    testsuite = getSuite(app_name, cases)
    if testsuite is not None:
        ret = runTests(testsuite, script, interpreter)
        if v: print ret
    else:
        print P.need_tests
        print P.usage
elif command == str(Commands.ADD):
    ret = addTests(app_name)
    if v: print ret
