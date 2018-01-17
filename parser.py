from options import Options
import re

def parseCommandArgs(args):
    line = ''
    is_verbose = 0
    for j in args: line += str(j) + ' '

    if str(Options.VERBOSE) in args: is_verbose = 1
    if str(Options.WITH_CASES) in args:
        try:
            p = re.compile('--with-cases\s+?(\d.*)+')
            m = p.search(line)
            cases = map(int, m.group(1).strip().split(' '))
        except:
            cases = []
    else: cases = []

    return is_verbose, cases
