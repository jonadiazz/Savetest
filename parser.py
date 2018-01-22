from commands import Commands
from options import Options
import re

def parseCommandArgs(args):
    line = ''
    is_verbose = 0
    interpreter = 'python' # 'interpreter to run app, default is python'
    which_passing = 'returns selected passing list'
    for j in args: line += str(j) + ' '

    if str(Options.VERBOSE) in args: is_verbose = 1
    if str(Commands.ATTEST) in args:
        try:
            p = re.compile('passing\s+?((?:\d\s)+)')
            m = p.search(line)
            which_passing = list(map(int, m.group(1).strip().split()))
        except:
            which_passing = []
    if str(Options.INTERPRETER) in args:
        try:
            p = re.compile('--i\s+?(\w+)')
            m = p.search(line)
            interpreter = str(m.group(1).strip())
        except Exception as e:
            print('\t\tPosibly, no interpreter provided')
            raise Exception(e)
    if str(Options.WITH_CASES) in args:
        try:
            p = re.compile('--with-cases\s+?(\d.*)+')
            m = p.search(line)
            cases = list(map(int, m.group(1).strip().split(' ')))
        except:
            cases = []
    else: cases = []

    return is_verbose, interpreter, cases, which_passing
