from options import Options
from commands import Commands
import _prompts as P
import sys
from run_tests import runTests
from add_tests import addTests
from test_suite import TestSuite
from parser import parseCommandArgs

args = sys.argv

v = 'verbose flag'
cases = 'cases to include from testsuite'
v, interpreter, cases, which_passing = parseCommandArgs(args)

if str(Options.VERSION) in args: print('--version')
elif len(args)<3:
    print(P.savetest)
    print(P.usage)
    print(P.usage_ext+'\n')
    print(P.usage_ext2+'\n')
    print(P.usage_ext5+'\n')
    print(P.usage_ext3+'\n')
    print(P.usage_ext4+'\n')
    quit()

path = args[2].split('/')
app_name, extension = path[-1].split('.')
command = args[1]
script = args[2]

suite = TestSuite(app_name)
if command == str(Commands.ATTEST):
    if which_passing == []:
        which_passing = list(input('Enter Test Case Number (TSN) of passing (separated by space):\n').split())
    ret = suite.setPassing(which_passing)
    print(ret)
elif command == str(Commands.RUN):
    testsuite, count = suite.getSuite(cases)
    output = dict()
    if testsuite is not None:
        output, ret = runTests(testsuite, script, interpreter)
        confirmation = suite.saveOutput(output)
        if v:
            print(ret)
            print(confirmation)
    else:
        print(P.need_tests)
        print(P.usage)
elif command == str(Commands.ADD):
    ret = addTests(app_name)
    if v: print(ret)
